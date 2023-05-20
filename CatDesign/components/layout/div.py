def div(ui, css='', tailwind=''):
    """Create a div element."""
    return ui.element('div').style(css).classes(tailwind)