
from .buttons_base import CalculatorButtonBase


class CalculatorNumberButton(CalculatorButtonBase):
    """ """

    def on_click_action(self):
        print("Inside on click Numeric button : {}".format(self.name))
        self._add_button_value_to_input_box()



