
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

from ui_elements.css_constants import FONT_WEIGHT, BOLD
from .elements_base import CalculatorElementBase


class CalculatorButtonBase(CalculatorElementBase):

    base_icon_folder = "ui_elements/images/"

    def __init__(self, button_name, icon_file, output_display, input_box):
        super().__init__(button_name, QPushButton(button_name))

        self.output_display = output_display
        self.input_box = input_box
        self.icon_file = icon_file

        self._set_icon()

        # Register Action methods
        self.element.clicked.connect(lambda: self.on_click_action())
        self.element.pressed.connect(lambda: self.on_press_action())
        self.element.released.connect(lambda: self.on_release_action())

    def _set_icon(self):
        print("Icon File path : {}".format(self.icon_file))
        if self.icon_file:
            self.element.setIcon(QIcon(self.base_icon_folder + self.icon_file))
            self.element.setText("")
            print("Icon set done for :{}".format(self.name))

    def on_click_action(self):
        raise NotImplementedError

    def on_press_action(self):
        pass

    def on_release_action(self):
        self.input_box.set_focus()

    def _add_button_value_to_input_box(self):
        current_input_txt = self.input_box.value
        current_input_txt = current_input_txt if current_input_txt is not None else ""

        self.input_box.update("{}{}".format(current_input_txt, self.name))

    @staticmethod
    def prepare_css_style_map(style_map):
        # All Button Texts are Bold by default
        css_style_map = {FONT_WEIGHT: BOLD}
        css_style_map.update(style_map)

        return ";".join(["{}:{}".format(k, v) for k, v in css_style_map.items()])

    def set_css_style(self, css_style):
        self.element.setStyleSheet(css_style)

    def prepare_and_set_css_style(self, style_map):
        css_style = self.prepare_css_style_map(style_map)
        self.set_css_style(css_style)

