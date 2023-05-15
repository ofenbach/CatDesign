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
    h5 : str
        styles for H5 headers.
    h6 : str
        styles for H6 headers.
    subtitle1 : str
        styles for first level subtitles.
    subtitle2 : str
        styles for second level subtitles.
    body1 : str
        styles for primary body text.
    body2 : str
        styles for secondary body text.
    caption : str
        styles for captions.
    overline : str
        styles for overlines.
    """

    def __init__(self, color_scheme):
        """Constructs all the necessary attributes for the typography scheme object."""
        self.primary_font = 'Poppins'
        self.secondary_font = 'Roboto'

        # Headers
        self.h1 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '2em', 'bold', 'white; ')
        self.h2 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1.5em', 'bold', 'white; ')
        self.h3 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1.17em', 'bold', 'white; ')
        self.h4 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1em', 'bold', 'white; ')
        self.h5 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '0.875em', 'bold', 'white; ')
        self.h6 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '0.75em', 'bold', 'white; ')

        # Subtitles
        self.subtitle1 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1em', 'medium', 'white; ')
        self.subtitle2 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '0.875em', 'medium', '#D9D9D9; ')

        # Body text
        self.body1 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '1em', 'normal', 'white; ')
        self.body2 = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.secondary_font, '0.875em', 'normal', 'white; ')

        # Caption & Overline
        self.caption = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '0.75em', 'light', 'white; ')
        self.overline = "font-family: {}; font-size: {}; font-weight: {}; color: {}".format(self.primary_font, '0.625em', 'light', 'white; ')
