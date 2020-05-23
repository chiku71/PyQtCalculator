
# Standard Python Imports
import sys
from importlib import reload

# PyQt imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout

# Tool Specific Import
from ui_elements import buttons_layout, buttons_base, elements_base, numeric_button, input_box, output_display, evaluate_button
reload(elements_base)
reload(buttons_base)
reload(numeric_button)
reload(buttons_layout)
reload(input_box)
reload(output_display)
reload(evaluate_button)

from ui_elements.buttons_layout import BUTTON_ROW_LAYOUT_MAPS, HANDLER_CLASS, CSS_STYLE_MAP
from ui_elements.buttons_base import CalculatorButtonBase
from ui_elements.input_box import CalculatorInputBox
from ui_elements.output_display import CalculatorOutputDisplay


class ApplicationWindow(QWidget):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setWindowTitle("Basic Calculator")

        self.display_results = dict()

        self.button_objects_map = dict()
        self.output_display = CalculatorOutputDisplay()
        self.input_box = CalculatorInputBox()

        self.g_layout = QGridLayout()

        self.initiate_gui()

    def initiate_gui(self):

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.output_display.element)
        main_layout.addWidget(self.input_box.element)

        # Create the grid
        self._set_up_buttons_to_grid()
        main_layout.addLayout(self.g_layout)

        self.setLayout(main_layout)
        self.show()

    def _set_up_buttons_to_grid(self):
        max_columns = 0
        for r, row_layout_map in enumerate(BUTTON_ROW_LAYOUT_MAPS):
            row_items = row_layout_map.keys()
            total_row_items = len(row_items)
            max_columns = total_row_items if max_columns < total_row_items else max_columns
            for c, btn_item in enumerate(row_items):
                row_width = 1
                col_width = (max_columns - total_row_items + 1) \
                    if c == total_row_items - 1 and c != max_columns - 1 else 1

                # Now set the buttons to their positions
                button_details = row_layout_map[btn_item]
                handler_class = button_details.get(HANDLER_CLASS, CalculatorButtonBase)
                
                button = handler_class(btn_item, self.output_display, self.input_box)
                button.prepare_and_set_css_style(button_details.get(CSS_STYLE_MAP, dict()))

                self.g_layout.addWidget(button.element, r, c, row_width, col_width)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Starting window application")
    window = ApplicationWindow()

    print("Closing application")

    sys.exit(app.exec_())