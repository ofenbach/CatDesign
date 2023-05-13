from nicegui import ui, app
from pathlib import Path

from CatDesign.components.basics.chip import chip
from CatDesign.components.basics.rating import rating
from CatDesign.components.feedback.alert import alert
from CatDesign.components.layout.div import div
from CatDesign.components.custom.notification import notification
from CatDesign.components.custom.tweet_card import tweet_card
from CatDesign.components.custom.card import card

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

from CatDesign.components.layout.box import box
from CatDesign.components.basics.divider import divider
from CatDesign.components.feedback.status import status
from CatDesign.components.basics.typography import typography
from styles.colors import Colors
from styles.fonts import FontScheme

# loading basic styles
head_style = """
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
body {
    font-family: 'Poppins';
    background-color: #0A0B0C;
    margin: 0;
}
"""

def main():
    """
    The main function to initiate the UI.
    """

    # cat design setup
    color_scheme = Colors(ui)       # init the colors
    font_scheme = FontScheme()
    ui.add_head_html(f'<style>{head_style}</style>')

    # typography
    typography(ui, font_scheme, text="Typography (in a box)", variant="h1")
    with box(ui, color_scheme):
        typography(ui, font_scheme, text="H1 Heading", variant="h1")
        typography(ui, font_scheme, text="H2 Heading", variant="h2")
        typography(ui, font_scheme, text="H3 Heading", variant="h3")
        typography(ui, font_scheme, text="H4 Heading", variant="h4")
        typography(ui, font_scheme, text="p1", variant="p1")
        typography(ui, font_scheme, text="p2", variant="p2")
        typography(ui, font_scheme, text="p3", variant="p3")
        typography(ui, font_scheme, text="caption", variant="caption")

    # tweet card
    divider(ui)
    typography(ui, font_scheme, text="Tweet card", variant="h1")
    tweet_card(ui, color_scheme, profile_src="./images/cat0.png")
    divider(ui)

    # card
    typography(ui, font_scheme, text="Card", variant="h1")
    with div(ui).classes('flex flex-wrap w-full justify-between'):
        card(ui, font_scheme, color_scheme, "images/cat_card.png", "Hi! I am your cat.", "Feed me or I get angry.")
        card(ui, font_scheme, color_scheme, "images/cat_card2.png", "Hi! I am your cat.", "Feed me or I get angry.")
        card(ui, font_scheme, color_scheme, "images/cat_card3.png", "Hi! I am your cat.", "Feed me or I get angry.")
    divider(ui)

    # notification
    typography(ui, font_scheme, text="Notification", variant="h1")
    with div(ui).classes('flex flex-wrap w-full justify-between'):
        notification(ui, font_scheme, color_scheme)     # header_message and message param possible (string)
        notification(ui, font_scheme, color_scheme)
        notification(ui, font_scheme, color_scheme)
    divider(ui)

    typography(ui, font_scheme, text="Chip", variant="h1")
    with div(ui).classes('flex flex-wrap w-80 justify-between'):
        chip(ui, font_scheme, color_scheme)
        chip(ui, font_scheme, color_scheme, variant="outlined")
    divider(ui)

    typography(ui, font_scheme, text="Rating", variant="h1")
    rating(ui, color_scheme, stars=4)
    divider(ui)

    typography(ui, font_scheme, text="Alerts", variant="h1")
    with div(ui).classes('flex flex-wrap w-full justify-between'):
        alert(ui, type="info", message="This is an info alert — check it out!")
        alert(ui, type="warning", message="This is a warning alert — check it out!")
        alert(ui, type="error", message="Please enter correct e-mail")
        alert(ui, type="success")
    divider(ui)

    # status
    typography(ui, font_scheme, text="Status", variant="h1")
    with div(ui).classes('flex flex-wrap w-full justify-between'):
        status(ui)                                                  # default is green
        status(ui, type="yellow", message="Custom text message")    # custom message param
        status(ui, type="red")                                      # every state has its own default message if param empty
    divider(ui)

    ui.run()    # start the UI event loop


if __name__ in {"__main__", "__mp_main__"}:
    """
    Entry point for the script. 

    This condition checks if the script is being run directly or imported as a module.
    If run directly, it calls the main function to initiate the UI.
    """
    main()
