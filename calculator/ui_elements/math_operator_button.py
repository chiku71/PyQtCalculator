
from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorMathOperatorButton(CalculatorButtonBase):

    def on_click_action(self):
        current_input_txt = self.input_box.cleaned_value

        if current_input_txt:
            current_input_txt = current_input_txt
        elif self.output_display.last_result:
            current_input_txt = self.output_display.last_result
        else:
            current_input_txt = ""

        self.input_box.update("{} {}".format(current_input_txt, self.name))
