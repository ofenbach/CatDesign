from nicegui.elements.mixins.text_element import TextElement

head_style = """
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background-color: #0A0B0C;
    margin: 0;
}

.txt_field {
    position: relative;
    border: 1px solid #323232;
    background-color: #1E1E1E;
    border-radius: 8px;
}
.txt_field input {
      width: 100%;
      padding: 0 5px;
      height: 40px;
      font-size: 16px;
      border: none;
      background: none;
      outline: none;
      color: white;
}
.txt_field label {
      position: absolute;
      top: 50%;
      left: 5px;
      color: #adadad;
      transform: translateY(-50%);
      font-size: 16px;
      pointer-events: none;
      transition: .5s;
}
.txt_field span::before{
      content: '';
      position: absolute;
      top: 40px;
      left: 0;
      width: 0%;
      height: 2px;
      background: red;
      transition: .3s;
}
.txt_field input:focus ~ label,
.txt_field input:valid ~ label{
      top: -10px;
      color: white;
}
.txt_field input:focus ~ span::before,
.txt_field input:valid ~ span::before{
      width: 100%;
}
"""


class CatDesign:

    def __init__(self, ui, color_box='#1E1E1E', color_border='#323232', color_bg='#0A0B0C',
                 h1='font-size: 48px; font-weight: medium; color: white;',
                 h2='font-size: 32px; font-weight: medium; color: white;',
                 h3='font-size: 24px; font-weight: medium; color: white;',
                 h4='font-size: 20px; font-weight: regular; color: white;',
                 p1='font-size: 20px; font-weight: 300; color: #A6A6A6;',
                 p2='font-size: 16px; font-weight: 300; color: #A6A6A6;',
                 p3='font-size: 12px; font-weight: 300; color: #A6A6A6;'):
        """ Sets up cat design with default colors, default typography."""
        self.ui = ui
        self.color_box = color_box
        self.color_border = color_border
        self.color_bg = color_bg
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.ui.add_head_html(f'<style>{head_style}</style>')
        self.ui.colors(primary=color_box)
        self.ui.colors(secondary=color_border)

    def div(self):
        return self.ui.element('div')

    def box(self, classes='', style=''):
        return self.div().classes(classes).style(
            f'background-color: {self.color_box}; border: 1px solid {self.color_border};'
            f'padding: 32px; border-radius: 8px;' + style)

    def typography(self, text="text", variant="h1", style=""):
        match variant:
            case "h1":
                self.ui.label(text).style(self.h1 + style)
            case "h2":
                self.ui.label(text).style(self.h2 + style)
            case "h3":
                self.ui.label(text).style(self.h3 + style)
            case "h4":
                self.ui.label(text).style(self.h4 + style)
            case "p1":
                self.ui.label(text).style(self.p1 + style)
            case "p2":
                self.ui.label(text).style(self.p2 + style)
            case "p3":
                self.ui.label(text).style(self.p3 + style)

    def divider(self, classes='mt-8 mb-8', style='background-color: #323232'):
        """ Divider to cut between sections """
        self.div().classes('w-full h-px ' + classes).style(style)

    def top_bar(self, logo_svg="", logo_name="Logo", background_color='#1E1E1E',
                links=[('https://github.com/zauberzeug/nicegui', 'GitHub')]):
        with self.div().classes('flex justify-between w-full p-4').style(f'background-color: {background_color}'):
            with self.div().classes('flex items-center'):
                self.ui.icon('store').classes('text-white text-5xl mr-4')
                self.ui.label(logo_name).classes('text-white text-2xl')
            with self.div().classes('flex items-center').style('border-bottom: 1px solid red;'):
                self.ui.label('Search').classes('text-white mr-4')
                self.ui.icon("search").style('color: white;')
            with self.div().classes('flex items-center'):
                for link_url, link_name in links:
                    self.ui.link(link_name, link_url).style('text-decoration: none; color: white; margin-right: 32px;')

    # todo: border color to secondary, input font color white
    def textfield(self, placeholder="Placeholder", style=""):
        with self.div().classes('txt_field').style(style):
            self.ui.element('input').props('type="text", required')
            self.ui.element('span')
            self.ui.element('label')
            TextElement(tag='label', text=placeholder)

    def card(self, img_src="", header="Heading", sub_header="Subheading"):

        with self.box(style='padding: 24px;'):

            with self.ui.row():
                self.ui.image(img_src).classes('rounded-2 w-80 h-44')

            self.divider()

            with self.ui.row():
                self.typography(header, "h4")

            with self.ui.row().classes('mt-4'):
                self.typography(sub_header, "p2")

    def status(self, type="green", message="Everything is fine!"):
        """
        :param message: message to appear in the status
        :param type: green, yellow, red
        """
        color_yellow = '#BEB82F'
        color_lightyellow = '#F7F5E5'
        color_lightred = '#F7E5E5'
        color_red = '#BE2F2F'

        match type:
            case "green":
                with self.ui.element('button').style(
                        'border-radius: 2px; background-color: #E8F7E5; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                    self.div().style(
                        'background-color: #3CBE2F; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                    self.ui.label(message).style('color: #3CBE2F;')
            case "yellow":
                with self.ui.element('button').style(
                        f'border-radius: 2px; background-color: {color_lightyellow}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                    self.div().style(
                        f'background-color: {color_yellow}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                    self.ui.label(message).style(f'color: {color_yellow};')
            case "red":
                with self.ui.element('button').style(
                        f'border-radius: 2px; background-color: {color_lightred}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                    self.div().style(
                        f'background-color: {color_red}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                    self.ui.label(message).style(f'color: {color_red};')


    def notification(self, header_message="Meow-tification", message="Time to refill the food bowl, hooman!",
                     color="#6CCAFF"):
        with self.div().style(
                f'padding-top: 16px; padding-bottom: 16px; padding-left: 32px; padding-right: 32px; background-color: {self.color_box}; border: 1px solid {self.color_border}; border-left: 8px solid {color}; border-radius: 8px;'):
            self.ui.label(header_message).style('font-size: 20px; color: white; margin-bottom: 16px;')
            self.ui.label(message).style('font-size: 16px; color: #A6A6A6;')

    def footer(self):
        with self.div().style(
                f'width: 100%; background-color: {self.color_box}; padding-top: 64px; padding-bottom: 64px; padding-left: 128px; padding-right: 128px;'):
            with self.div().classes('flex w-full justify-between items-center'):
                with self.div().classes('flex items-center'):
                    self.ui.icon('store').classes('text-white text-5xl mr-4')
                    self.ui.label("logo").classes('text-white text-2xl')
                with self.div().classes('items-center'):
                    self.ui.link('Link', 'https://github.com/zauberzeug/nicegui').style(
                        'text-decoration: none; color: white; '
                        'margin-right: 32px;')
                    self.ui.link('Link', 'https://github.com/zauberzeug/nicegui').style(
                        'text-decoration: none; color: white; '
                        'margin-right: 32px;')
                    self.ui.link('Link', 'https://github.com/zauberzeug/nicegui').style(
                        'text-decoration: none; color: white; '
                        'margin-right: 32px;')
                    self.ui.link('Link', 'https://github.com/zauberzeug/nicegui').style(
                        'text-decoration: none; color: white;')

            self.divider()

            with self.div().classes('flex w-full justify-between items-center'):
                with self.div().classes('flex items-center'):
                    self.typography("CatDesign 2023", "h4")
                with self.div().classes('items-center'):
                    self.ui.icon('home').classes('text-xl text-white mr-4')
                    self.ui.icon('home').classes('text-xl text-white mr-4')
                    self.ui.icon('home').classes('text-xl text-white')

    def avatar(self, src, style=""):
        self.ui.image(src).style('border-radius: 50%; height: 32px; width: 32px;' + style)

    def tweet_card(self, profile_src, profile_name="Profile Name", tweet="Tweet!", retweet="Retweet!"):
        with self.div().style(f'background-color: {self.color_box}; border: 1px solid {self.color_border}; box-shadow: '
                         'none; color: white; padding: 32px; border-radius: 8px;'):
            # profile avatar
            with self.ui.row().classes('flex items-center'):
                self.ui.image(profile_src).classes('rounded-full h-8 w-8')
                self.ui.label(profile_name).classes('text-white text-base font-light')

            # tweet
            with self.ui.row().classes('mt-4'):
                self.ui.label(tweet).classes('text-base font-light').style('color: #D9D9D9;')

            # date, share, like
            with self.ui.row().classes('flex justify-between items-center w-full mt-4'):
                self.ui.label("23.03.2023").classes('text-xs font-light').style('color: #A6A6A6;')
                with self.div():
                    self.ui.icon('share').classes('mr-4 text-sm')
                    self.ui.icon('thumb_up').classes('text-sm')

            # divider
            with self.ui.row().classes('w-full mt-8 mb-8'):
                self.div().classes('w-full h-px').style(f'background-color: {self.color_border}')

            # retweet profiles
            with self.ui.row().classes('flex justify-between items-center w-full'):
                with self.div():
                    self.avatar(src='images/cat1.png', style='z-index: 3;')
                    self.avatar(src='images/cat2.png', style='margin-left: -16px; z-index: 2;')
                    self.avatar(src='images/cat3.png', style='margin-left: -16px; z-index: 1;')
                    self.avatar(src='images/cat4.png', style='margin-left: -16px; z-index: 0;')

                with self.div():
                    self.ui.label("Retweets").classes('text-xs font-light')

            # retweet
            with self.ui.row().classes('flex items-center mt-6'):
                self.avatar(src='images/cat5.png')
                self.ui.label("Retweeter").classes('text-sm font-light text-white')

            with self.ui.row().classes('mt-4'):
                self.ui.label(retweet).classes('text-xs font-light').style('color: #D9D9D9')

            with self.ui.row().classes('w-full mt-8'):
                with self.ui.element("div").classes('flex w-full justify-center items-center rounded-full p-2').style(
                        f'border: 1px solid {self.color_border}; box-shadow: none; background-color: {self.color_box};'):
                    self.ui.label("Show all").classes('mr-4 text-xs text-white')
                    self.ui.icon('expand_more').classes('text-white')









def horizontal_card(ui, header="Heading", subheader="Subheading"):
    with div().classes('flex w-full justify-between').style(
            f'background-color: {color_box}; border: 1px solid {color_border}; box-shadow: '
            'none; color: white; padding: 24px; border-radius: 8px;'):
        with div().style('width: 45%'):
            ui.image('images/cat_card.png').classes('rounded-2 w-80 h-44')
        with div().style('width: 50%'):
            typography(header, variant="h3")
            typography(subheader, variant="p2")








def newsletter():
    with div().classes('flex flex-wrap w-full p-12'):
        with div().classes('w-full md:w-1/2 md:flex-1'):
            typography(text="Header Newsletter", variant="p1")
            typography(text="SubHeader Newsletter", variant="p1")

        with div().classes('w-full md:w-1/2 md:flex-1 mt-4 md:mt-0'):
            textfield(ui, "email")
            textfield(ui, "name", style="margin-top: 32px;")

