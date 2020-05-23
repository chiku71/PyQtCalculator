
from PyQt5.QtWidgets import QLineEdit

from .elements_base import CalculatorElementBase


class CalculatorInputBox(CalculatorElementBase):

    def __init__(self):
        super(CalculatorInputBox, self).__init__("input_box", QLineEdit())

    @property
    def value(self):
        return self.element.text()

    def update(self, updated_value):
        self.element.setText(updated_value)

    def clear(self):
        self.element.setText("")