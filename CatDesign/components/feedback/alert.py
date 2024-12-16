from components.layout.div import div


def alert(ui, type="success", message="Operation successful!", css='', tailwind=''):
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

    match type:
        case "success":
            with div(ui, css=f'border-radius: 2px; background-color: {color_lightgreen};'
                    f' display: flex; align-items: center; padding: 8px 16px;'+css, tailwind=tailwind):
                ui.icon('task_alt').classes('text-3xl').style(f'color: {color_green}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_green};')
        case "info":
            with div(ui, css=f'border-radius: 2px; background-color: {color_lightblue};'
                             f' display: flex; align-items: center; padding: 8px 16px;' + css, tailwind=tailwind):
                ui.icon('info').classes('text-3xl').style(f'color: {color_blue}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_blue};')
        case "warning":
            with div(ui, css=f'border-radius: 2px; background-color: {color_lightyellow};'
                             f' display: flex; align-items: center; padding: 8px 16px;' + css, tailwind=tailwind):
                ui.icon('warning_amber').classes('text-3xl').style(f'color: {color_yellow}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_yellow};')
        case "error":
            with div(ui, css=f'border-radius: 2px; background-color: {color_lightred};'
                             f' display: flex; align-items: center; padding: 8px 16px;' + css, tailwind=tailwind):
                ui.icon('report_gmailerrorred').classes('text-3xl').style(f'color: {color_red}; margin-right: 0.5em;')
                ui.label(message).style(f'color: {color_red};')
