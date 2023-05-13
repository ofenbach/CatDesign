from CatDesign.components.layout.div import div


def rating(ui, color_scheme, stars=4):
    """ 1-5 Stars display """
    with div(ui).classes('flex flex-wrap justify-between'):
        for i in range(5):
            if i < stars:
                ui.icon('star').classes('text-5xl').style(f'color: {color_scheme.warning}')
            else:
                ui.icon('star_border').classes('text-5xl').style(f'color: {color_scheme.warning}')
