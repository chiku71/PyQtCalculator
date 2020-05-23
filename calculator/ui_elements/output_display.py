# PyQt imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLineEdit, QVBoxLayout, QScrollArea, QLabel

from ui_elements.elements_base import CalculatorElementBase
from ui_elements.css_constants import BG_COLOR, BOLD, FONT_SIZE, FONT_WEIGHT, BORDER_WIDTH


class CalculatorOutputDisplay(CalculatorElementBase):
    """ """

    odd_result_row_color = "#60C4F5"
    even_result_row_color = "#FEFEAD"

    def __init__(self):
        super(CalculatorOutputDisplay, self).__init__("output_display", QScrollArea())

        self.output_results = dict()
        self.output_vbox = QVBoxLayout()
        self.display_widget = QWidget()

        self.odd_row_flag = True

        self._set_up_display()

    def _set_up_display(self):
        self.output_vbox.setSpacing(0)

        self.element.setAlignment(Qt.AlignTop)
        self.output_vbox.setAlignment(Qt.AlignTop)

        self.display_widget.setLayout(self.output_vbox)

        # Scroll Area Properties
        self.element.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.element.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.element.setWidgetResizable(True)
        self.element.setWidget(self.display_widget)
        self.element.setFixedHeight(200)

        # Register activities
        scroll_bar = self.element.verticalScrollBar()
        scroll_bar.rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))

    def add_result_row(self, input_expression, result):
        row_color = self.odd_result_row_color if self.odd_row_flag else self.even_result_row_color

        # Add the input Expression
        input_exp_css = "{}: 0px;{}: {};{}:20px;".format(BORDER_WIDTH, BG_COLOR, row_color, FONT_SIZE)
        label = QLabel(str(input_expression))
        label.setStyleSheet(input_exp_css)
        self.output_vbox.addWidget(label)

        # Add the result
        result_css = "{}: 0px;{}: {};{}: {}; {}:30px;".format(BORDER_WIDTH, BG_COLOR, row_color,
                                                              FONT_WEIGHT, BOLD, FONT_SIZE)
        label = QLabel(str(result))
        label.setStyleSheet(result_css)
        self.output_vbox.addWidget(label)

        self.odd_row_flag = False if self.odd_row_flag else True

    def clear(self):
        for i in reversed(range(self.output_vbox.count())):
            self.output_vbox.itemAt(i).widget().deleteLater()

        self.odd_row_flag = True


