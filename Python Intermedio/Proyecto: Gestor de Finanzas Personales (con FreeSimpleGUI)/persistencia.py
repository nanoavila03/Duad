import json
import os

CATEGORIES_FILE = "categories.json"
MOVEMENTS_FILE  = "movements.json"


class SaveDataInterface:
    def save_data(self, data):
        raise NotImplementedError("Subclasses must implement this method")


class LoadDataInterface:
    def load_data(self):
        raise NotImplementedError("Subclasses must implement this method")


class PersistenceManager(SaveDataInterface, LoadDataInterface):

    def save_data(self, manager):
        with open(CATEGORIES_FILE, "w", encoding="utf-8") as f:
            json.dump(manager.get_categories(), f, ensure_ascii=False, indent=2)

        movements = [
            {
                "title":    m.title,
                "amount":   m.amount,
                "category": m.category,
                "type":     m.type,
                "date":     m.date
            }
            for m in manager.get_movements()
        ]
        with open(MOVEMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(movements, f, ensure_ascii=False, indent=2)

    def load_data(self, manager):
        if os.path.exists(CATEGORIES_FILE):
            with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
                for name in json.load(f):
                    manager.add_category(name)

        if os.path.exists(MOVEMENTS_FILE):
            with open(MOVEMENTS_FILE, "r", encoding="utf-8") as f:
                for m in json.load(f):
                    manager.add_movement(m["title"], m["amount"], m["category"], m["type"])
                    manager.get_movements()[-1].date = m["date"]


def save_data(manager):
    PersistenceManager().save_data(manager)


def load_data(manager):
    PersistenceManager().load_data(manager)