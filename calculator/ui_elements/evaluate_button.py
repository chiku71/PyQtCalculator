

from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorEvaluateButton(CalculatorButtonBase):

    def on_click_action(self):
        self.input_box.calculate_and_display_output()

