def typography(ui, font_scheme, text='', variant='', css='', tailwind=''):
    valid_variants = ["h1", "h2", "h3", "h4", "h5", "h6", "subtitle1", "subtitle2", "body1", "body2", "caption",
                      "overline"]
    if variant not in valid_variants:
        raise ValueError("Unsupported variant: {}. Valid variants are: {}".format(variant, ', '.join(valid_variants)))

    font_style = getattr(font_scheme, variant)
    tailwind_classes = tailwind.split(' ')
    ui.label(text).style(font_style + css).tailwind(*tailwind_classes) # split big string into small strings