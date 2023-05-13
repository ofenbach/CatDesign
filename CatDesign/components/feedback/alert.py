def alert(ui, type="success", message="Operation successful!"):
    """
    :param message: message to appear in the alert
    :param type: success, info, warning, error
    """
    color_blue = '#2196F3'
    color_lightblue = '#E5F1F7'
    color_lightyellow = '#F7F5E5'
    color_yellow = '#BEB82F'
    color_lightred = '#F7E5E5'
    color_red = '#BE2F2F'
    color_lightgreen = '#E8F7E5'
    color_green = '#3CBE2F'

    def div():
        """Create a div element."""
        return ui.element('div')

    match type:
        case "success":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightgreen};'
                    f' display: flex; align-items: center; padding: 8px 16px;'):
                ui.icon('task_alt').classes('text-3xl').style(f'color: {color_green}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_green};')
        case "info":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightblue}; display: flex; align-items: center; padding: 8px 16px;'):
                ui.icon('info').classes('text-3xl').style(f'color: {color_blue}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_blue};')
        case "warning":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightyellow}; display: flex; align-items: center; padding: 8px 16px;'):
                ui.icon('warning_amber').classes('text-3xl').style(f'color: {color_yellow}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_yellow};')
        case "error":
            with ui.element('button').style(
                    f'border-radius: 2px; background-color: {color_lightred}; display: flex; align-items: center; padding: 8px 16px;'):
                ui.icon('report_gmailerrorred').classes('text-3xl').style(f'color: {color_red}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_red};')
