from nicegui import ui, app

from CatDesign.components.basics.chip import chip
from CatDesign.components.basics.divider import divider
from CatDesign.components.basics.rating import rating
from CatDesign.components.basics.typography import typography
from CatDesign.components.custom.card import card
from CatDesign.components.custom.notification import notification
from CatDesign.components.feedback.alert import alert
from CatDesign.components.layout.box import box
from CatDesign.components.layout.div import div
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

    def div(self, css='', tailwind=''):
        return div(self.ui, css, tailwind)

    def typography(self, text='', variant='', css='', tailwind=''):
        typography(self.ui, self.font_scheme, text, variant, css, tailwind)

    def box(self, css='', tailwind=''):
        return box(self.ui, self.color_scheme, css, tailwind)

    def divider(self, css='', tailwind=''):
        divider(self.ui)

    def card(self, img_src='./images/cat_card.png', header='Header', sub_header='Subheader', css='', tailwind=''):
        card(self.ui, self.font_scheme, self.color_scheme, img_src, header, sub_header, css, tailwind)

    def notification(self, header="Meow-tification", sub_header="Time to refill the food bowl, hooman!", css='', tailwind=''):
        notification(ui, self.font_scheme, self.color_scheme, header, sub_header, css, tailwind)

    def chip(self, variant='filled', css='', tailwind=''):
        chip(self.ui, self.font_scheme, self.color_scheme, variant=variant, css=css, tailwind=tailwind)

    def rating(self, stars=4, css='', tailwind=''):
        rating(self.ui, self.color_scheme, stars, css, tailwind)

    def alert(self, type='success', message='Success'):
        alert(self.ui, type, message)   # todo: use font scheme + color scheme