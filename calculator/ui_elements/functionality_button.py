

from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorACButton(CalculatorButtonBase):
    """ """

    def on_click_action(self):
        self.input_box.clear()


class CalculatorDelButton(CalculatorButtonBase):
    """ """

    def on_click_action(self):
        current_input_txt = self.input_box.value
        current_input_txt = current_input_txt if current_input_txt is not None else ""

        if current_input_txt:
            new_input_txt = str(current_input_txt)[:len(current_input_txt)-1]
            self.input_box.update(new_input_txt)


class CalculatorClearButton(CalculatorButtonBase):

    def on_click_action(self):
        print("Clear button clicked ...")
        self.output_display.clear()