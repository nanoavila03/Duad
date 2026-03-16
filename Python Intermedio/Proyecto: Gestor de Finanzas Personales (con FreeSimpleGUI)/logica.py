from datetime import date, datetime


class Category:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Movement:
    def __init__(self, title: str, amount: float, category: str, type: str, date: str = None):
        self.title    = title
        self.amount   = amount
        self.category = category
        self.type     = type
        self.date     = date if date else globals()["date"].today().strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.date} | {self.title} | ${self.amount} | {self.category} | {self.type}"


class FinanceManager:
    def __init__(self):
        self._categories: list[Category] = []
        self._movements:  list[Movement] = []

    def add_category(self, name: str):
        self._categories.append(Category(name))

    def get_categories(self) -> list[str]:
        return [c.name for c in self._categories]

    def add_movement(self, title: str, amount: float, category: str, type: str, date: str = None):
        movement = Movement(title, amount, category, type, date)
        self._movements.append(movement)

    def get_movements(self) -> list[Movement]:
        return self._movements

    def calculate_balance(self) -> float:
        total = 0.0
        for m in self._movements:
            if m.type == "Income":
                total += m.amount
            else:
                total -= m.amount
        return total

    def filter_by_dates(self, from_date: str, to_date: str) -> list:
        date_from = datetime.strptime(from_date, "%d/%m/%Y").date()
        date_to   = datetime.strptime(to_date,   "%d/%m/%Y").date()
        return [
            m for m in self._movements
            if date_from <= datetime.strptime(m.date, "%d/%m/%Y").date() <= date_to
        ]

    def delete_movement(self, index: int):
        if 0 <= index < len(self._movements):
            self._movements.pop(index)

    def delete_category(self, name: str):
        self._categories = [c for c in self._categories if c.name != name]

    def save(self):
        from persistencia import save_data
        save_data(self)


def validate_date(date_str: str) -> tuple[bool, str]:
    try:
        parsed = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        return False, "Invalid date format (use dd/mm/yyyy)."
    if parsed > date.today():
        return False, "Date cannot be in the future."
    return True, ""