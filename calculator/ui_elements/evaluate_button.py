

from ui_elements.buttons_base import CalculatorButtonBase


class CalculatorEvaluateButton(CalculatorButtonBase):

    def on_click_action(self):
        print("Inside on click Evaluation Button")
        current_input_txt = self.input_box.value
        print("Evaluating : '{}'".format(current_input_txt))

        if current_input_txt:
            try:
                # Clean the expression from replaced symbols
                current_input_txt = str(current_input_txt).strip().replace("X", "*")

                result = eval(current_input_txt)
            except Exception as ex:
                print("Exception occurred : {}".format(ex))
                result = "Invalid Expression"

            # Add the details to the output display
            self.output_display.add_result_row(current_input_txt, result)

            # Set the input box to blank
            self.input_box.clear()