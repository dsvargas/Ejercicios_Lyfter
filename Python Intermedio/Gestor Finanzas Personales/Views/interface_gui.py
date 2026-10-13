from typing import List, Optional, Tuple
import FreeSimpleGUI as sg


class MainView:

    def __init__(self):
        sg.theme("DarkBlue3")

    def build_main_window(
        self, table_data: List[List], balance: float
    ) -> sg.Window:
        layout = [
            [
                sg.Text(
                    "Personal Finance Manager", font=("Helvetica", 16, "bold")
                )
            ],
            [
                sg.Text(
                    f"Balance: ${balance:.2f}",
                    key="-BALANCE-",
                    font=("Helvetica", 12, "bold"),
                )
            ],
            [sg.HSeparator()],
            [
                sg.Button("Add Category", key="-BTN-ADD-CAT-"),
                sg.Button(
                    "Add Expense",
                    key="-BTN-ADD-EXP-",
                    button_color=("white", "#a83232"),
                ),
                sg.Button(
                    "Add Income",
                    key="-BTN-ADD-INC-",
                    button_color=("white", "#2b8a3e"),
                ),
            ],
            [sg.HSeparator()],
            [
                sg.Table(
                    values=table_data,
                    headings=["Type", "Title", "Amount", "Category", "Date"],
                    auto_size_columns=True,
                    justification="center",
                    key="-TABLE-",
                    num_rows=10,
                )
            ],
            [sg.Button("Exit", key="-BTN-EXIT-")],
        ]
        return sg.Window("Finance Manager", layout, finalize=True)

    @staticmethod
    def show_error(message: str):
        sg.popup_error(message, title="Error")

    @staticmethod
    def show_info(message: str):
        sg.popup(message, title="Information")

    @staticmethod
    def open_add_category_window() -> Optional[str]:
        layout = [
            [sg.Text("Category Name:")],
            [sg.InputText(key="-CAT-NAME-")],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]
        window = sg.Window("Add Category", layout, modal=True)
        category_name = None

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            if event == "Save":
                category_name = values["-CAT-NAME-"]
                break

        window.close()
        return category_name

    @staticmethod
    def open_add_movement_window(
        movement_type: str, categories: List[str]
    ) -> Optional[Tuple[str, float, str]]:
        layout = [
            [sg.Text(f"Add New {movement_type}", font=("Helvetica", 12, "bold"))],
            [sg.Text("Title:"), sg.InputText(key="-TITLE-")],
            [sg.Text("Amount:"), sg.InputText(key="-AMOUNT-")],
            [sg.Text("Description:"), sg.InputText(key="-DESC-")],
            [
                sg.Text("Category:"),
                sg.Combo(categories, default_value=categories[0], key="-CAT-", readonly=True),
            ],
            [sg.Button("Save"), sg.Button("Cancel")],
        ]
        window = sg.Window(f"Add {movement_type}", layout, modal=True)
        result = None

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break
            if event == "Save":
                title = values["-TITLE-"].strip()
                amount_raw = values["-AMOUNT-"].strip()
                description = values["-DESC-"].strip()
                category = values["-CAT-"]

                result = (title, amount_raw, category, description)
                break

        window.close()
        return result