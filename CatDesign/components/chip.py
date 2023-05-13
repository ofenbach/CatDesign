from CatDesign.components.box import box
from CatDesign.components.typography import typography


def chip(ui, font_scheme, color_scheme, variant="filled", text="Chip"):

    if variant == "filled":
        with box(ui, color_scheme, style="border-radius: 100px; padding: 16px; border: 0;"):
            typography(ui, font_scheme, text=text, variant="h4")

    if variant == "outlined":
        with box(ui, color_scheme, style="border-radius: 100px; padding: 16px; background-color: rgba(0,0,0,0);"):
            typography(ui, font_scheme, text=text, variant="h4")