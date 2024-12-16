from components.layout.div import div


def rating(ui, color_scheme, stars=4, css='', tailwind=''):
    """ 1-5 Stars display """
    with div(ui, css=css, tailwind='flex flex-wrap justify-between'+tailwind):
        for i in range(5):
            if i < stars:
                ui.icon('star').classes('text-3xl').style(f'color: {color_scheme.warning}')
            else:
                ui.icon('star_border').classes('text-3xl').style(f'color: {color_scheme.warning}')
