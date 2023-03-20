from nicegui.elements.mixins.text_element import TextElement

style = """
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background-color: #0A0B0C;
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

color_box = '#1E1E1E'
color_border = '#323232'
color_bg = '#0A0B0C'

font = 'font-family: Poppins;'
h1 = 'font-size: 48px; font-weight: medium; color: white;'
h2 = 'font-size: 32px; font-weight: medium; color: white;'
h3 = 'font-size: 24px; font-weight: medium; color: white;'
h4 = 'font-size: 20px; font-weight: regular; color: white;'
p1 = 'font-size: 20px; font-weight: 300; color: #A6A6A6;'
p2 = 'font-size: 16px; font-weight: 300; color: #A6A6A6;'
p3 = 'font-size: 12px; font-weight: 300; color: #A6A6A6;'

ui = ""


def setup(ui_):
    global ui
    ui = ui_
    """ defines colors, adds font etc """
    ui.add_head_html(f'<style>{style}</style>')
    ui.colors(primary=color_box)
    ui.colors(secondary=color_border)


def typography_examples():
    with ui.element('div').classes('w-full p-12 flex justify-center'):
        with ui.element('div').classes('justify-center mr-12'):
            typography(ui, "H1 - XL Heading", variant="h1")
            typography(ui, "H2 - L Heading", variant="h2")
            typography(ui, "H3 - M Heading", variant="h3")
            typography(ui, "H4 - S Heading", variant="h4")

        with ui.element('div').classes('justify-center'):
            typography(ui, "P1 - Large Text", variant="p1")
            typography(ui, "P2 - Medium Text", variant="p2")
            typography(ui, "P3 - Small Text", variant="p3")


def typography(ui, text, variant="h1"):
    match variant:
        case "h1":
            ui.label(text).style(h1)
        case "h2":
            ui.label(text).style(h2)
        case "h3":
            ui.label(text).style(h3)
        case "h4":
            ui.label(text).style(h4)
        case "p1":
            ui.label(text).style(p1)
        case "p2":
            ui.label(text).style(p2)
        case "p3":
            ui.label(text).style(p3)


def top_bar(ui, logo_svg="", logo_name="Logo"):
    with ui.element('div').classes('flex justify-between w-full p-4').style(f'background-color: {color_box}'):
        with ui.element('div').classes('flex items-center'):
            ui.icon('store').classes('text-white text-5xl mr-4')
            ui.label(logo_name).classes('text-white text-2xl')
        with ui.element('div').classes('flex items-center').style('border-bottom: 1px solid red;'):
            ui.label('Search').classes('text-white mr-4')
            ui.icon("search").style('color: white;')
        with ui.element('div').classes('flex items-center'):
            ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                           'margin-right: 32px;')
            ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                           'margin-right: 32px;')
            ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                           'margin-right: 32px;')
            ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                           'margin-right: 32px;')


# todo: border color to secondary, input font color white
def textfield(ui, placeholder="Placeholder", style=""):
    with ui.element('div').classes('txt_field').style(style):
        ui.element('input').props('type="text", required')
        ui.element('span')
        ui.element('label')
        TextElement(tag='label', text=placeholder)


def notification(ui, header_message="Meow-tification", message="Time to refill the food bowl, hooman!",
                 color="#6CCAFF"):
    with ui.element('div').style(
            f'padding-top: 16px; padding-bottom: 16px; padding-left: 32px; padding-right: 32px; background-color: {color_box}; border: 1px solid {color_border}; border-left: 8px solid {color}; border-radius: 8px;'):
        ui.label(header_message).style('font-size: 20px; color: white; margin-bottom: 16px;')
        ui.label(message).style('font-size: 16px; color: #A6A6A6;')


def divider():
    with ui.row().classes('w-full mt-8 mb-8'):
        ui.element('div').classes('w-full h-px').style(f'background-color: {color_border}')


def card(ui, header="Heading", subheader="Subheading"):
    with ui.element('div').style(f'background-color: {color_box}; border: 1px solid {color_border}; box-shadow: '
                                 'none; color: white; padding: 24px; border-radius: 8px;'):
        with ui.row():
            ui.image('images/cat_card.png').classes('rounded-2 w-80 h-44')

        divider()

        with ui.row():
            ui.label(header).classes('text-white text-xl')

        with ui.row().classes('mt-4'):
            ui.label(subheader).style('color: #D9D9D9; font-size: 16px; font-weight: 300;')


def horizontal_card(ui, header="Heading", subheader="Subheading"):
    with ui.element('div').classes('flex w-full justify-between').style(
            f'background-color: {color_box}; border: 1px solid {color_border}; box-shadow: '
            'none; color: white; padding: 24px; border-radius: 8px;'):
        with ui.element('div').style('width: 45%'):
            ui.image('images/cat_card.png').classes('rounded-2 w-80 h-44')
        with ui.element('div').style('width: 50%'):
            typography(ui, header, variant="h3")
            typography(ui, subheader, variant="p2")


def status(ui, type="green", message="Everything is fine!"):
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
            with ui.element('button').style(
                    'border-radius: 2px; background-color: #E8F7E5; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                ui.element('div').style(
                    'background-color: #3CBE2F; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style('color: #3CBE2F;')
        case "yellow":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightyellow}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                ui.element('div').style(
                    f'background-color: {color_yellow}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style(f'color: {color_yellow};')
        case "red":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightred}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                ui.element('div').style(
                    f'background-color: {color_red}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style(f'color: {color_red};')


def avatar(ui, src, style=""):
    ui.image(src).style('border-radius: 50%; height: 32px; width: 32px;' + style)


def tweet_card(ui, profile_src, profile_name="Profile Name", tweet="Tweet!", retweet="Retweet!"):
    with ui.element('div').style(f'background-color: {color_box}; border: 1px solid {color_border}; box-shadow: '
                                 'none; color: white; padding: 32px; border-radius: 8px;'):
        # profile avatar
        with ui.row().classes('flex items-center'):
            ui.image(profile_src).classes('rounded-full h-8 w-8')
            ui.label(profile_name).classes('text-white text-base font-light')

        # tweet
        with ui.row().classes('mt-4'):
            ui.label(tweet).classes('text-base font-light').style('color: #D9D9D9;')

        # date, share, like
        with ui.row().classes('flex justify-between items-center w-full mt-4'):
            ui.label("23.03.2023").classes('text-xs font-light').style('color: #A6A6A6;')
            with ui.element('div'):
                ui.icon('share').classes('mr-4 text-sm')
                ui.icon('thumb_up').classes('text-sm')

        # divider
        with ui.row().classes('w-full mt-8 mb-8'):
            ui.element('div').classes('w-full h-px').style(f'background-color: {color_border}')

        # retweet profiles
        with ui.row().classes('flex justify-between items-center w-full'):
            with ui.element('div'):
                avatar(ui=ui, src='images/cat1.png', style='z-index: 3;')
                avatar(ui=ui, src='images/cat2.png', style='margin-left: -16px; z-index: 2;')
                avatar(ui=ui, src='images/cat3.png', style='margin-left: -16px; z-index: 1;')
                avatar(ui=ui, src='images/cat4.png', style='margin-left: -16px; z-index: 0;')

            with ui.element('div'):
                ui.label("Retweets").classes('text-xs font-light')

        # retweet
        with ui.row().classes('flex items-center mt-6'):
            avatar(ui=ui, src='images/cat5.png')
            ui.label("Retweeter").classes('text-sm font-light text-white')

        with ui.row().classes('mt-4'):
            ui.label(retweet).classes('text-xs font-light').style('color: #D9D9D9')

        with ui.row().classes('w-full mt-8'):
            with ui.element("div").classes('flex w-full justify-center items-center rounded-full p-2').style(
                    f'border: 1px solid {color_border}; box-shadow: none; background-color: {color_box};'):
                ui.label("Show all").classes('mr-4 text-xs text-white')
                ui.icon('expand_more').classes('text-white')


def div():
    return ui.element('div')


def newsletter():
    with div().classes('flex flex-wrap w-full p-12'):
        with div().classes('w-full md:w-1/2 md:flex-1'):
            typography(ui, text="Header Newsletter", variant="p1")
            typography(ui, text="SubHeader Newsletter", variant="p1")

        with div().classes('w-full md:w-1/2 md:flex-1 mt-4 md:mt-0'):
            textfield(ui, "email")
            textfield(ui, "name", style="margin-top: 32px;")


def footer():

    with div().style(f'width: 100%; background-color: {color_box}; padding-top: 64px; padding-bottom: 64px; padding-left: 128px; padding-right: 128px;'):

        with div().classes('flex w-full justify-between items-center'):
            with ui.element('div').classes('flex items-center'):
                ui.icon('store').classes('text-white text-5xl mr-4')
                ui.label("logo").classes('text-white text-2xl')
            with ui.element('div').classes('items-center'):
                ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                               'margin-right: 32px;')
                ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                               'margin-right: 32px;')
                ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white; '
                                                                               'margin-right: 32px;')
                ui.link('Link', 'https://github.com/zauberzeug/nicegui').style('text-decoration: none; color: white;')

        divider()

        with div().classes('flex w-full justify-between items-center'):
            with ui.element('div').classes('flex items-center'):
                typography(ui, "CatDesign 2023", "h4")
            with ui.element('div').classes('items-center'):
                ui.icon('home').classes('text-xl text-white mr-4')
                ui.icon('home').classes('text-xl text-white mr-4')
                ui.icon('home').classes('text-xl text-white')