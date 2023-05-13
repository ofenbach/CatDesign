from nicegui import ui, app

from CatDesign.components.basics.divider import divider
from CatDesign.components.basics.typography import typography
from CatDesign.components.layout.box import box
from CatDesign.styles.colors import ColorScheme
from CatDesign.styles.fonts import FontScheme


class CatDesign:

    def __init__(self):
        # loading basic styles
        head_style = """
        @import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
        body {
            font-family: 'Poppins';
            background-color: #0A0B0C;
            margin: 0;
        }
        """

        # cat design setup
        self.color_scheme = ColorScheme(ui)                 # init the colors
        self.font_scheme = FontScheme(self.color_scheme)                     # init the font
        self.ui = ui
        self.ui.add_head_html(f'<style>{head_style}</style>')    # add basic style
        self.ui.run()                                            # start the UI event loop

    def typography(self, text='', variant='', css='', tailwind=''):
        typography(self.ui, self.font_scheme, text, variant, css, tailwind)

    def box(self, css='', tailwind=''):
        return box(self.ui, self.color_scheme, css, tailwind)

    def divider(self, css='', tailwind=''):
        divider(ui)