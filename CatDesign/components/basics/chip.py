from components.layout.box import box
from components.basics.typography import typography


def chip(ui, font_scheme, color_scheme, css, tailwind, variant="filled", text="Chip"):

    if variant == "filled":
        css = "border-radius: 100px; padding: 16px; border: 0; " + css
        with box(ui, color_scheme, css=css):
            typography(ui, font_scheme, text=text, variant="h4")

    if variant == "outlined":
        css = "border-radius: 100px; padding: 16px; background-color: rgba(0,0,0,0); " + css
        with box(ui, color_scheme, css=css):
            typography(ui, font_scheme, text=text, variant="h4")