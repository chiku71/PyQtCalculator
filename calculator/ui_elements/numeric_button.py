
from .buttons_base import CalculatorButtonBase


class CalculatorNumberButton(CalculatorButtonBase):
    """ Class for handling action for numeric buttons. """

    def on_click_action(self):
        current_input_txt = self.input_box.cleaned_value

        if current_input_txt:
            last_index = len(current_input_txt) - 1
            last_item = current_input_txt[last_index]
            if not (last_item.isnumeric() or last_item == "."):
                current_input_txt = current_input_txt + " "
        else:
            current_input_txt = ""

        self.input_box.update("{}{}".format(current_input_txt, self.name))



