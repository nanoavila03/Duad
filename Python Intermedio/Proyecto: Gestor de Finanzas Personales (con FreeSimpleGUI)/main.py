from logica import FinanceManager
from persistencia import load_data, save_data
from interfaces import UserInterface


def main():
    manager = FinanceManager()
    load_data(manager)

    ui = UserInterface(manager)
    ui.show()

    save_data(manager)


if __name__ == "__main__":
    main()