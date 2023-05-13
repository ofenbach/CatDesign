class FontScheme:
    """
    A class to represent a typography scheme for a modern UI design system.

    ...

    Attributes
    ----------
    primary_font : str
        primary font of the design system.
    secondary_font : str
        secondary font of the design system.
    h1 : str
        styles for H1 headers.
    h2 : str
        styles for H2 headers.
    h3 : str
        styles for H3 headers.
    h4 : str
        styles for H4 headers.
    p1 : str
        styles for primary body text.
    p2 : str
        styles for secondary body text.
    p3 : str
        styles for tertiary body text.
    caption : str
        styles for captions.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the typography scheme object."""
        self.primary_font = 'Poppins, sans-serif'
        self.secondary_font = 'Roboto, sans-serif'

        # Headers
        self.h1 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '2em', 'bold', 'white')
        self.h2 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1.5em', 'bold', 'white')
        self.h3 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1.17em', 'bold', 'white')
        self.h4 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1em', 'bold', 'white')

        # Body text
        self.p1 = "font-family: {}; font-size: {}; font-weight: {};".format(self.primary_font, '1em', 'normal')
        self.p2 = "font-family: {}; font-size: {}; font-weight: {};".format(self.primary_font, '0.875em', 'normal')
        self.p3 = "font-family: {}; font-size: {}; font-weight: {};".format(self.secondary_font, '0.75em', 'normal')

        # Caption
        self.caption = "font-family: {}; font-size: {}; font-weight: {};".format(self.secondary_font, '0.75em', 'light')
