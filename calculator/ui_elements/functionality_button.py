

from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorCEButton(CalculatorButtonBase):
    """ Class for handling action from CE button. """

    def on_click_action(self):
        self.input_box.clear()


class CalculatorDelButton(CalculatorButtonBase):
    """ Class for handling action for Delete button. """

    def on_click_action(self):
        current_input_txt = self.input_box.cleaned_value

        if current_input_txt:
            current_input_txt = str(current_input_txt)
            last_index = len(current_input_txt) - 1
            self.input_box.update(current_input_txt[:last_index].strip())


class CalculatorClearButton(CalculatorButtonBase):
    """ Class for handling action for Clear button."""

    def on_click_action(self):
        """ Clears out all the history entry for the session. """
        self.output_display.clear()