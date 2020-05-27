
from PyQt5.QtWidgets import QLineEdit

from .elements_base import CalculatorElementBase


class CalculatorInputBox(CalculatorElementBase):

    def __init__(self):
        super(CalculatorInputBox, self).__init__("input_box", QLineEdit())
        font = self.element.font()
        font.setPointSize(32)
        self.element.setFont(font)

    @property
    def value(self):
        return self.element.text()

    @property
    def cleaned_value(self):
        org_value = self.value

        if org_value is None:
            return org_value

        return str(org_value).strip()

    def update(self, updated_value):
        self.element.setText(updated_value)

    def clear(self):
        self.element.setText("")