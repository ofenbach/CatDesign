
class ColorScheme:
    """
    A class to represent a dark theme color scheme for a design system.

    ...

    Attributes
    ----------
    primary : str
        primary color of the design system.
    secondary : str
        secondary color of the design system.
    success : str
        color for successful actions or notifications.
    info : str
        color for informational messages.
    warning : str
        color for warnings.
    danger : str
        color for errors or dangerous actions.
    background : str
        background color of the design system.
    text : str
        default text color.

    Methods
    -------
    get_color(name):
        Returns the color value from the scheme by its name.
    """

    def __init__(self, ui):
        """Constructs all the necessary attributes for the color scheme object."""
        self.primary = '#757575'
        self.secondary = '#607D8B'
        self.success = '#4CAF50'
        self.info = '#2196F3'
        self.warning = '#FEFF86'
        self.danger = '#F44336'
        self.background = '#212121'
        self.text = '#E0E0E0'
        self.color_box = '#131416'
        self.color_border = '#26282C'
        ui.colors(primary=self.primary)
        ui.colors(secondary=self.secondary)

    def get_color(self, name):
        """
        Retrieves the color value from the scheme by its name.

        Parameters:
        name (str): The name of the color (e.g., 'primary', 'success', etc.)

        Returns:
        str: The color value.
        """
        try:
            return getattr(self, name)
        except AttributeError:
            raise ValueError(f"No color named {name} in the color scheme.")
