
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, Qt

from .elements_base import CalculatorElementBase


class CalculatorInputBox(CalculatorElementBase):

    def __init__(self, output_display):
        super(CalculatorInputBox, self).__init__("input_box", QLineEdit())
        self.output_display = output_display

        # Set Up the UI
        self._set_up_ui()

        # Set up the validators
        self._set_up_validators()

        self.element.setFocusPolicy(Qt.StrongFocus)
        self.element.returnPressed.connect(lambda: self.calculate_and_display_output())

    def _set_up_ui(self):
        font = self.element.font()
        font.setPointSize(32)
        self.element.setFont(font)

    def _set_up_validators(self):
        pattern = r"[0-9. Xx\*\-\+/]+"
        rx = QRegExp(pattern)
        validator = QRegExpValidator(rx, self.element)
        self.element.setValidator(validator)

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
        self.set_focus()

    def set_focus(self):
        self.element.setFocus()

    def clear(self):
        self.element.setText("")
        self.set_focus()

    def calculate_and_display_output(self):
        current_input_txt = self.cleaned_value

        if current_input_txt:
            try:
                # Clean the expression from replaced symbols
                current_input = str(current_input_txt).strip().replace("X", "*")
                current_input = str(current_input).strip().replace("x", "*")

                result = round(eval(current_input), 5)
                self.output_display.last_result = result
            except Exception as ex:
                print("Exception occurred : {}".format(ex))
                result = "Invalid Expression"

            # Add the details to the output display
            self.output_display.add_result_row(current_input_txt, result)

            # Set the input box to blank
            self.clear()