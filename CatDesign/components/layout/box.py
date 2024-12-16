from components.layout.div import div


def box(ui, color_scheme, css='', tailwind=''):
    """
    Create a box with given classes and style.

    :param classes: class names for the box
    :param style: style for the box
    :return: a styled div element
    """

    return div(ui, css=f'background-color: {color_scheme.color_box}; border: 1px solid {color_scheme.color_border};'
        f'padding: 32px; border-radius: 8px;{css}', tailwind=tailwind)
