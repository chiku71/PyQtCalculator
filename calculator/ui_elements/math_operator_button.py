
from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorMathOperatorButton(CalculatorButtonBase):

    def on_click_action(self):
        print("Inside on click Math Operator button : {}".format(self.name))
        self._add_button_value_to_input_box()
