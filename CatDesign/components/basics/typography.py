def typography(ui, font_scheme, text="text", variant="h1", style=""):
    """
    Apply typography to a text label based on the variant.

    :param ui: user interface object nicegui
    :param font_scheme: FontScheme object containing the font styles for different variants
    :param text: text to display
    :param variant: typography variant (supports 'h1', 'h2', 'h3', 'h4', 'p1', 'p2', 'p3', and 'caption')
    :raises ValueError: if an unsupported variant is provided
    """

    # Apply the style to the text label
    if variant == "h1":
        ui.label(text).style(font_scheme.h1).style(style)
    elif variant == "h2":
        ui.label(text).style(font_scheme.h2).style(style)
    elif variant == "h3":
        ui.label(text).style(font_scheme.h3).style(style)
    elif variant == "h4":
        ui.label(text).style(font_scheme.h4).style(style)
    elif variant == "p1":
        ui.label(text).style(font_scheme.p1).style(style)
    elif variant == "p2":
        ui.label(text).style(font_scheme.p2).style(style)
    elif variant == "p3":
        ui.label(text).style(font_scheme.p3).style(style)
    elif variant == "caption":
        ui.label(text).style(font_scheme.caption).style(style)
    else:
        raise ValueError("Unsupported variant: {}".format(variant))
