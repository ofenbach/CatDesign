from nicegui.elements.mixins.text_element import TextElement

color_box = '#1E1E1E'
color_border = '#323232'
color_bg = '#0A0B0C'


def setup(ui):
    """ defines colors, adds font etc """
    ui.add_head_html('<style>body {background-color: #0A0B0C; }</style>')
    ui.add_head_html("<style>" +
                     "@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');" +
                     "body { font-family: 'Poppins', sans-serif;}</style>")
    ui.colors(primary=color_box)
    ui.colors(secondary=color_border)

    ui.add_head_html('''<style>
    .txt_field{
      position: relative;
      border: 1px solid #323232;
      background-color: #1E1E1E;
      border-radius: 8px;
      margin: 30px 0;
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
    </style>
     ''')


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
def textfield(ui, placeholder="Placeholder"):
    with ui.element('div').classes('txt_field'):
        ui.element('input').props('type="text", required')
        ui.element('span')
        ui.element('label')
        TextElement(tag='label', text='Username')


def notification(ui, header_message="Meow-tification", message="Time to refill the food bowl, hooman!", color="#6CCAFF"):

    with ui.element('div').style(f'padding-top: 16px; padding-bottom: 16px; padding-left: 32px; padding-right: 32px; background-color: {color_box}; border: 1px solid {color_border}; border-left: 8px solid {color}; border-radius: 8px;'):
        ui.label(header_message).style('font-size: 20px; color: white; margin-bottom: 16px;')
        ui.label(message).style('font-size: 16px; color: #A6A6A6;')

def divider(ui):
    with ui.row().classes('w-full mt-8 mb-8'):
        ui.element('div').classes('w-full h-px').style(f'background-color: {color_border}')


def card(ui, header="Heading", subheader="Subheading"):
    with ui.element('div').style(f'background-color: {color_box}; border: 1px solid {color_border}; box-shadow: '
                                 'none; color: white; padding: 24px; border-radius: 8px;'):
        with ui.row():
            ui.image('images/cat_card.png').classes('rounded-2 w-80 h-44')

        divider(ui)

        with ui.row():
            ui.label(header).classes('text-white text-xl')

        with ui.row().classes('mt-4'):
            ui.label(subheader).style('color: #D9D9D9; font-size: 16px; font-weight: 300;')


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
