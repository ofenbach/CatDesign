def status(ui, type="green", message="Everything is fine!"):
    """
    :param message: message to appear in the status
    :param type: green, yellow, red
    """
    color_yellow = '#BEB82F'
    color_lightyellow = '#F7F5E5'
    color_lightred = '#F7E5E5'
    color_red = '#BE2F2F'

    def div():
        """Create a div element."""
        return ui.element('div')

    match type:
        case "green":
            with ui.element('button').style(
                    'border-radius: 2px; background-color: #E8F7E5; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                div().style(
                    'background-color: #3CBE2F; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style('color: #3CBE2F;')
        case "yellow":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightyellow}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                div().style(
                    f'background-color: {color_yellow}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style(f'color: {color_yellow};')
        case "red":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightred}; display: flex; align-items: center; padding-left: 24px; padding-right: 24px; padding-top: 16px; padding-bottom: 16px;'):
                div().style(
                    f'background-color: {color_red}; border-radius: 50px; width: 16px; height: 16px; margin-right: 16px;')
                ui.label(message).style(f'color: {color_red};')
