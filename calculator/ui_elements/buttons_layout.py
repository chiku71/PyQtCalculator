from collections import OrderedDict
from ui_elements.css_constants import BG_COLOR, FONT_SIZE
from ui_elements.numeric_button import CalculatorNumberButton
from ui_elements.math_operator_button import CalculatorMathOperatorButton
from ui_elements.evaluate_button import CalculatorEvaluateButton
from ui_elements.functionality_button import CalculatorCEButton, CalculatorDelButton, CalculatorClearButton


HANDLER_CLASS = "handler_class"
CSS_STYLE_MAP = "css_style_map"
ICON_PATH = "icon_path"

# [("CE", "Del", "Clear", "/", "Sqr"),
#  ("7", "8", "9", "X", "Sqrt"),
#  ("4", "5", "6", "-", "Pow"),
#  ("1", "2", "3", "+", "Root"),
#  (".", "0", "%", "=")]
BUTTON_ROW_LAYOUT_MAPS = [
    OrderedDict((
        ("CE", {
            HANDLER_CLASS: CalculatorCEButton,
            CSS_STYLE_MAP: {BG_COLOR: "#4578EF"}}),
        ("Del", {
            HANDLER_CLASS: CalculatorDelButton,
            CSS_STYLE_MAP: {BG_COLOR: "red"}}),
        ("Clear", {
            HANDLER_CLASS: CalculatorClearButton,
            CSS_STYLE_MAP: {BG_COLOR: "#FA2DAC"}}),
        ("/", {
            HANDLER_CLASS: CalculatorMathOperatorButton,
            ICON_PATH: "Divide_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#7BE2D5"}})
    )),
    OrderedDict((
        ("7", {HANDLER_CLASS: CalculatorNumberButton}),
        ("8", {HANDLER_CLASS: CalculatorNumberButton}),
        ("9", {HANDLER_CLASS: CalculatorNumberButton}),
        ("X", {
            HANDLER_CLASS: CalculatorMathOperatorButton,
            ICON_PATH: "Multiply_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#7BE2D5"}})
    )),
    OrderedDict((
        ("4", {HANDLER_CLASS: CalculatorNumberButton}),
        ("5", {HANDLER_CLASS: CalculatorNumberButton}),
        ("6", {HANDLER_CLASS: CalculatorNumberButton}),
        ("-", {
            HANDLER_CLASS: CalculatorMathOperatorButton,
            ICON_PATH: "Minus_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#7BE2D5"}})
    )),
    OrderedDict((
        ("1", {HANDLER_CLASS: CalculatorNumberButton}),
        ("2", {HANDLER_CLASS: CalculatorNumberButton}),
        ("3", {HANDLER_CLASS: CalculatorNumberButton}),
        ("+", {
            HANDLER_CLASS: CalculatorMathOperatorButton,
            ICON_PATH: "Plus_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#7BE2D5"}})
    )),
    OrderedDict((
        (".", {
            HANDLER_CLASS: CalculatorNumberButton,
            ICON_PATH: "Dot_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#7BE2D5"}}),
        ("0", {HANDLER_CLASS: CalculatorNumberButton}),
        ("=", {
            HANDLER_CLASS: CalculatorEvaluateButton,
            ICON_PATH: "Equal_T.png",
            CSS_STYLE_MAP: {BG_COLOR: "#158F24", FONT_SIZE: "15px"}})
    ))
]