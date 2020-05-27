

from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorEvaluateButton(CalculatorButtonBase):

    def on_click_action(self):
        current_input_txt = self.input_box.value

        if current_input_txt:
            try:
                # Clean the expression from replaced symbols
                current_input = str(current_input_txt).strip().replace("X", "*")

                result = round(eval(current_input), 5)
                self.output_display.last_result = result
            except Exception as ex:
                print("Exception occurred : {}".format(ex))
                result = "Invalid Expression"

            # Add the details to the output display
            self.output_display.add_result_row(current_input_txt, result)

            # Set the input box to blank
            self.input_box.clear()

