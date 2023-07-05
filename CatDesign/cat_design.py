import os

from nicegui import ui

from CatDesign.components.basics.avatar import avatar
from CatDesign.components.basics.chip import chip
from CatDesign.components.basics.divider import divider
from CatDesign.components.basics.rating import rating
from CatDesign.components.basics.typography import typography
from CatDesign.components.custom.card import card
from CatDesign.components.custom.bar_chart import bar_chart
from CatDesign.components.custom.line_chart import line_chart
from CatDesign.components.custom.notification import notification
from CatDesign.components.feedback.alert import alert
from CatDesign.components.layout.box import box
from CatDesign.components.layout.div import div
from CatDesign.styles.colors import ColorScheme
from CatDesign.styles.fonts import FontScheme


class CatDesign:
    """
        CatDesign is a class for creating UI components with a specific design.
    """

    def __init__(self):
        """
            Initializes the CatDesign with a specific color scheme, font scheme, and UI.
        """
        head_style = """
        @import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
        body {
            font-family: 'Poppins';
            background-color: #0A0B0C;
            margin: 0;
        }
        """

        self.color_scheme = ColorScheme(ui)                      # init the colors
        self.font_scheme = FontScheme(self.color_scheme)         # init the font
        self.ui = ui
        self.ui.add_head_html(f'<style>{head_style}</style>')    # add basic style
        self.ui.run(title="CatDesign")                           # start the UI event loop

    def div(self, css='', tailwind=''):
        return div(self.ui, css, tailwind)

    def typography(self, text='', variant='h1', css='', tailwind=''):
        typography(self.ui, self.font_scheme, text, variant, css, tailwind)

    def box(self, css='', tailwind=''):
        return box(self.ui, self.color_scheme, css, tailwind)

    def divider(self, css='background-color: #26282C', tailwind='mt-8 mb-8'):
        divider(self.ui, css, tailwind)

    def avatar(self, img_src='./images/cat0.png', css='', tailwind=''):
        avatar(self.ui, img_src=img_src, css=css, tailwind=tailwind)

    def card(self, img_src='./images/cat_card.png', header='Header', sub_header='Subheader', css='', tailwind=''):
        card(self.ui, self.font_scheme, self.color_scheme, img_src, header, sub_header, css, tailwind)

    def notification(self, header='Meow-tification', sub_header='Time to refill the food bowl, hooman!', css='', tailwind=''):
        notification(ui, self.font_scheme, self.color_scheme, header, sub_header, css, tailwind)

    def chip(self, variant='filled', css='', tailwind=''):
        chip(self.ui, self.font_scheme, self.color_scheme, variant=variant, css=css, tailwind=tailwind)

    def rating(self, stars=4, css='', tailwind=''):
        rating(self.ui, self.color_scheme, stars, css, tailwind)

    def alert(self, type='success', message='Success', css='', tailwind=''):
        alert(self.ui, type, message, css, tailwind)   # todo: use font scheme + color scheme

    def icon(self, icon_name, color='#FFFFFF', variant='outlined', css='', tailwind=''):
        # validate variant
        if variant not in ['outlined', 'filled']:
            raise ValueError(f"Invalid variant '{variant}'. Expected 'outlined' or 'filled'.")

        # adjust icon name based on variant
        icon_file_name = f'{icon_name}_{variant}.svg'

        # adjust path to the icon file
        icon_path = os.path.join('components', 'icons', icon_name, icon_file_name)

        try:
            with open(icon_path, 'r') as file:
                svg_content = file.read().replace('currentColor', color)
            self.ui.html(svg_content).style(css)
        except FileNotFoundError:
            print(f"Icon '{icon_name}' not found in the '{variant}' variant.")

    def tweet_card(self, profile_src, profile_name='Profile Name', tweet='Tweet!', tweet_date='23.05.2023', retweet='Retweet!', liked=False):

        with div(ui, css=f'background-color: {self.color_scheme.color_box}; border: 1px solid {self.color_scheme.color_border};'
                     f'box-shadow: none; color: white; padding: 32px; border-radius: 8px;'):

            # profile avatar
            with ui.row().classes('flex items-center'):
                ui.image(profile_src).classes('rounded-full h-8 w-8')
                self.typography(profile_name, variant='subtitle1')

            # tweet
            with ui.row().classes('mt-4'):
                self.typography(tweet, variant='h3')

            # date, share_outlined.svg, like
            with ui.row().classes('flex justify-between items-center w-full mt-4'):
                self.typography(tweet_date, variant='subtitle2', css='color: #A6A6A6;')
                with div(ui, tailwind='flex'):
                    self.icon('share', css='margin-right: 16px;')
                    self.icon('like', variant='filled' if liked else 'outlined')

            # divider
            self.divider()

            # retweet profiles
            with ui.row().classes('flex justify-between items-center w-full'):
                with div(ui):
                    avatar(ui, img_src='images/cat1.png', css='z-index: 3;')
                    avatar(ui, img_src='images/cat2.png', css='margin-left: -16px; z-index: 2;')
                    avatar(ui, img_src='images/cat3.png', css='margin-left: -16px; z-index: 1;')
                    avatar(ui, img_src='images/cat4.png', css='margin-left: -16px; z-index: 0;')

                with div(ui):
                    self.typography('Retweets', variant='subtitle2', css='color: white;')

            # retweet
            with ui.row().classes('flex items-center mt-6'):
                avatar(ui, img_src='images/cat5.png')
                self.typography('Retweeter', variant='subtitle1')

            with ui.row().classes('mt-4'):
                self.typography(text=retweet, variant='subtitle2')

            with ui.row().classes('w-full mt-8'):
                ui.button('Show all').props('size=md icon-right=expand_more no-caps outline text-color=white').classes('rounded-full w-full ')

    def bar_chart(self, data=None, labels=None, css='', tailwind=''):
        bar_chart(self.ui, self.color_scheme, data, labels, css, tailwind)

    def line_chart(self, data=None, labels=None, css='', tailwind=''):
        line_chart(self.ui, self.color_scheme, data, labels, css, tailwind)