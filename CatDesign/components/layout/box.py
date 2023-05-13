def box(ui, color_scheme, classes='', style=''):
    """
    Create a box with given classes and style.

    :param classes: class names for the box
    :param style: style for the box
    :return: a styled div element
    """

    def div():
        """Create a div element."""
        return ui.element('div')

    return div().style(
        f'background-color: {color_scheme.color_box}; border: 1px solid {color_scheme.color_border};'
        f'padding: 32px; border-radius: 8px;{style}').classes(classes)
