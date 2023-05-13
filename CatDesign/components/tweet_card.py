from CatDesign.components.avatar import avatar


def tweet_card(ui, color_scheme, profile_src, profile_name="Profile Name", tweet="Tweet!", retweet="Retweet!"):

    def div():
        """Create a div element."""
        return ui.element('div')

    with div().style(f'background-color: {color_scheme.color_box}; border: 1px solid {color_scheme.color_border}; box-shadow: '
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
            with div():
                ui.icon('share').classes('mr-4 text-sm')
                ui.icon('thumb_up').classes('text-sm')

        # divider
        with ui.row().classes('w-full mt-8 mb-8'):
            div().classes('w-full h-px').style(f'background-color: {color_scheme.color_border}')

        # retweet profiles
        with ui.row().classes('flex justify-between items-center w-full'):
            with div():
                avatar(ui, src='images/cat1.png', style='z-index: 3;')
                avatar(ui, src='images/cat2.png', style='margin-left: -16px; z-index: 2;')
                avatar(ui, src='images/cat3.png', style='margin-left: -16px; z-index: 1;')
                avatar(ui, src='images/cat4.png', style='margin-left: -16px; z-index: 0;')

            with div():
                ui.label("Retweets").classes('text-xs font-light')

        # retweet
        with ui.row().classes('flex items-center mt-6'):
            avatar(ui, src='images/cat5.png')
            ui.label("Retweeter").classes('text-sm font-light text-white')

        with ui.row().classes('mt-4'):
            ui.label(retweet).classes('text-xs font-light').style('color: #D9D9D9')

        with ui.row().classes('w-full mt-8'):
            with ui.element("div").classes('flex w-full justify-center items-center rounded-full p-2').style(
                    f'border: 1px solid {color_scheme.color_border}; box-shadow: none; background-color: {color_scheme.color_box};'):
                ui.label("Show all").classes('mr-4 text-xs text-white')
                ui.icon('expand_more').classes('text-white')

