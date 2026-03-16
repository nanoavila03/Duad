import csv
import FreeSimpleGUI as sg
from datetime import date
from logica import FinanceManager, validate_date


class UserInterface:
    def __init__(self, manager: FinanceManager):
        self.manager = manager
        self.window = self._create_main_window()

    def _create_main_window(self):
        today = date.today().strftime("%d/%m/%Y")
        headers = ["Date", "Title", "Amount", "Category", "Type"]
        layout = [
            [sg.Text("Personal Finance Manager", font=("Arial", 14))],
            [
                sg.Text("From:"), sg.InputText(key="-FROM-", size=12),
                sg.Text("To:"), sg.InputText(today, key="-TO-", size=12),
                sg.Button("Filter"),
                sg.Button("Show All")
            ],
            [sg.Table(
                values=[],
                headings=headers,
                key="-TABLE-",
                expand_x=True,
                num_rows=10,
                auto_size_columns=True
            )],
            [
                sg.Button("Add Category"),
                sg.Button("Add Expense"),
                sg.Button("Add Income"),
                sg.Button("Delete Selected"),
                sg.Button("Delete Category"),
                sg.Button("Export to CSV"),
                sg.Button("Exit")
            ]
        ]
        return sg.Window("Finance Manager", layout, finalize=True)

    def _refresh_table(self, movements=None):
        if movements is None:
            movements = self.manager.get_movements()
        rows = [
            [m.date, m.title, m.amount, m.category, m.type]
            for m in movements
        ]
        self.window["-TABLE-"].update(values=rows)

    def show(self):
        self._refresh_table()
        while True:
            event, values = self.window.read()

            if event in ("Exit", sg.WIN_CLOSED):
                break
            elif event == "Add Category":
                self._window_add_category()
            elif event == "Add Expense":
                self._window_add_movement(type="Expense")
            elif event == "Add Income":
                self._window_add_movement(type="Income")
            elif event == "Delete Selected":
                self._delete_movement(values["-TABLE-"])
            elif event == "Delete Category":
                self._delete_category()
            elif event == "Filter":
                self._filter(values["-FROM-"], values["-TO-"])
            elif event == "Show All":
                self._refresh_table()
            elif event == "Export to CSV":
                self._export_csv()

        self.window.close()

    def _filter(self, from_date: str, to_date: str):
        for date_str in [from_date, to_date]:
            valid, error = validate_date(date_str)
            if not valid:
                sg.popup_error(f"Invalid date: {error}")
                return

        filtered = self.manager.filter_by_dates(from_date, to_date)
        if not filtered:
            sg.popup("No movements found in that date range.")
        self._refresh_table(filtered)

    def _window_add_category(self):
        layout = [
            [sg.Text("Category name"), sg.InputText(key="-NAME-")],
            [sg.Button("Save"), sg.Button("Cancel")]
        ]
        window = sg.Window("New Category", layout)
        while True:
            event, values = window.read()
            if event in ("Cancel", sg.WIN_CLOSED):
                break
            elif event == "Save":
                name = values["-NAME-"].strip()
                if not name:
                    sg.popup_error("Name cannot be empty.")
                else:
                    self.manager.add_category(name)
                    self.manager.save()
                    sg.popup(f'Category "{name}" added.')
                    break
        window.close()

    def _window_add_movement(self, type: str):
        categories = self.manager.get_categories()
        if not categories:
            sg.popup_error("No categories available. Please add one first.")
            return

        today = date.today().strftime("%d/%m/%Y")
        layout = [
            [sg.Text("Title"),    sg.InputText(key="-TITLE-")],
            [sg.Text("Amount"),   sg.InputText(key="-AMOUNT-")],
            [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
            [sg.Text("Date"),     sg.InputText(today, key="-DATE-"), sg.Text("(dd/mm/yyyy)")],
            [sg.Button("Save"),   sg.Button("Cancel")]
        ]
        window = sg.Window(f"Add {type}", layout)

        while True:
            event, values = window.read()
            if event in ("Cancel", sg.WIN_CLOSED):
                break
            elif event == "Save":
                title      = values["-TITLE-"].strip()
                amount_raw = values["-AMOUNT-"].strip()
                category   = values["-CATEGORY-"]
                date_str   = values["-DATE-"].strip()

                if not title:
                    sg.popup_error("Title cannot be empty.")
                    continue
                if not category:
                    sg.popup_error("Please select a category.")
                    continue
                try:
                    amount = float(amount_raw)
                    if amount <= 0:
                        raise ValueError
                except ValueError:
                    sg.popup_error("Amount must be a number greater than 0.")
                    continue

                valid, error = validate_date(date_str)
                if not valid:
                    sg.popup_error(error)
                    continue

                self.manager.add_movement(title, amount, category, type, date_str)
                self.manager.save()
                self._refresh_table()
                sg.popup(f"{type} recorded successfully.")
                break

        window.close()

    def _delete_movement(self, selection: list):
        if not selection:
            sg.popup_error("Please select a movement from the table first.")
            return

        index = selection[0]
        movement = self.manager.get_movements()[index]

        confirm = sg.popup_yes_no(
            f"Delete this movement?\n\n"
            f"{movement.date} | {movement.title} | ${movement.amount}"
        )
        if confirm == "Yes":
            self.manager.delete_movement(index)
            self.manager.save()
            self._refresh_table()
            sg.popup("Movement deleted.")

    def _delete_category(self):
        categories = self.manager.get_categories()
        if not categories:
            sg.popup_error("No categories to delete.")
            return

        layout = [
            [sg.Text("Select category to delete:")],
            [sg.Combo(categories, key="-CATEGORY-", readonly=True)],
            [sg.Button("Delete"), sg.Button("Cancel")]
        ]
        window = sg.Window("Delete Category", layout)

        while True:
            event, values = window.read()
            if event in ("Cancel", sg.WIN_CLOSED):
                break
            elif event == "Delete":
                category = values["-CATEGORY-"]
                if not category:
                    sg.popup_error("Please select a category.")
                    continue
                confirm = sg.popup_yes_no(f'Delete category "{category}"?')
                if confirm == "Yes":
                    self.manager.delete_category(category)
                    self.manager.save()
                    sg.popup(f'Category "{category}" deleted.')
                    break

        window.close()

    def _export_csv(self):
        movements = self.manager.get_movements()
        if not movements:
            sg.popup_error("No movements to export.")
            return

        path = sg.popup_get_file(
            "Save as",
            save_as=True,
            default_extension=".csv",
            file_types=(("CSV", "*.csv"),)
        )
        if not path:
            return

        total_income  = sum(m.amount for m in movements if m.type == "Income")
        total_expense = sum(m.amount for m in movements if m.type == "Expense")
        balance       = total_income - total_expense

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Title", "Amount", "Category", "Type"])
            for m in movements:
                writer.writerow([m.date, m.title, m.amount, m.category, m.type])
            writer.writerow([])
            writer.writerow(["Totals:"])
            writer.writerow(["Income:",  f"${total_income}"])
            writer.writerow(["Expense:", f"${total_expense}"])
            writer.writerow(["Net Balance:", f"${balance}"])

        sg.popup(f"Exported successfully to:\n{path}")