def typography(ui, font_scheme, text="text", variant="h1"):
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
        ui.label(text).style(font_scheme.h1)
    elif variant == "h2":
        ui.label(text).style(font_scheme.h2)
    elif variant == "h3":
        ui.label(text).style(font_scheme.h3)
    elif variant == "h4":
        ui.label(text).style(font_scheme.h4)
    elif variant == "p1":
        ui.label(text).style(font_scheme.p1)
    elif variant == "p2":
        ui.label(text).style(font_scheme.p2)
    elif variant == "p3":
        ui.label(text).style(font_scheme.p3)
    elif variant == "caption":
        ui.label(text).style(font_scheme.caption)
    else:
        raise ValueError("Unsupported variant: {}".format(variant))
