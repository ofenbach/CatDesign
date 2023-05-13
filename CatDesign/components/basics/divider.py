def divider(ui, tailwind='mt-8 mb-8', css='background-color: #26282C'):
    """
    Creates a divider between sections.

    :param classes: CSS classes for the divider
    :param style: CSS styles for the divider
    """
    def div():
        """Create a div element."""
        return ui.element('div')
    div().classes('w-full h-px ' + tailwind).style(css)