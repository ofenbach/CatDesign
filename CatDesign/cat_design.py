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


# todo: border color to secondary, input font color white
def textfield(ui, placeholder="Placeholder"):
    ui.input().props(f'dark borderless v-model="text" label-color="white" label={placeholder}')


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
