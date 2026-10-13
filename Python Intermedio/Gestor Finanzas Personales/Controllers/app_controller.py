import FreeSimpleGUI as sg
from Models.finance_manager import Finance_manager
from Models.transaction import Expense, Income
from Views.interface_gui import MainView


class AppController:

    def __init__(self):
        self.finance_manager = Finance_manager()
        self.interface_gui = MainView()
        # Intentamos cargar los datos y verificamos si hubo errores
        load_error = self.finance_manager.load_data()
        if load_error:
            # Mostramos el error en la interfaz gráfica en lugar de un print en consola
            self.interface_gui.show_error(
                f"Advertencia de carga:\n{load_error}\n\nSe iniciará con datos vacíos para proteger tu información."
            )

    def get_table_data(self):
        """Formatea los movimientos de finance_manager para cargarlos en la tabla."""
        return [
            [
                m.get_movement_type(),
                m.title,
                f"${m.amount:.2f}",
                m.category,
                m.date,
            ]
            for m in self.finance_manager.movements
        ]

    def run(self):
        # 1. Crear la ventana principal una sola vez fuera del bucle
        window = self.interface_gui.build_main_window(
            self.get_table_data(), self.finance_manager.get_balance()
        )

        # 2. Event Loop principal
        while True:
            event, values = window.read()

            # Salir de la aplicación
            if event in (sg.WINDOW_CLOSED, "-BTN-EXIT-"):
                break

            # Evento: Agregar Categoría
            elif event == "-BTN-ADD-CAT-":
                cat_name = self.interface_gui.open_add_category_window()
                if cat_name:
                    if self.finance_manager.add_category(cat_name):
                        self.interface_gui.show_info(
                            f"Category '{cat_name}' added successfully!"
                        )
                    else:
                        self.interface_gui.show_error(
                            "Invalid or duplicate category name."
                        )

            # Evento: Agregar Gasto o Ingreso
            elif event in ("-BTN-ADD-EXP-", "-BTN-ADD-INC-"):
                # Requisito: Validar existencia de categorías
                if not self.finance_manager.categories:
                    self.interface_gui.show_error(
                        "No categories available! Please add a category first."
                    )
                    continue

                is_expense = event == "-BTN-ADD-EXP-"
                mov_type = "Expense" if is_expense else "Income"

                data = self.interface_gui.open_add_movement_window(
                    mov_type, self.finance_manager.categories
                )

                if data:
                    title, amount, category, description = data

                    # Crear la instancia correspondiente según la herencia de Transaction
                    new_movement = (
                        Expense(
                            title=title,
                            amount=amount,
                            category=category,
                            description=description
                        )
                        if is_expense
                        else Income(
                            title=title,
                            amount=amount,
                            category=category,
                            description=description
                        )
                    )

                    # Guardar la transacción
                    self.finance_manager.add_movement(new_movement)

                    # 3. Actualizar la interfaz gráfica dinámicamente
                    window["-TABLE-"].update(values=self.get_table_data())
                    window["-BALANCE-"].update(
                        f"Balance: ${self.finance_manager.get_balance():.2f}"
                    )

        # 4. Destruir la ventana al salir
        window.close()