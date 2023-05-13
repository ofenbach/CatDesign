from nicegui import ui, app
from pathlib import Path

from CatDesign.components.notification import notification
from components.card import card

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

from components.box import box
from components.divider import divider
from components.status import status
from components.typography import typography
from styles.colors import Colors
from styles.fonts import FontScheme

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

    This function creates a label in the UI and runs the UI loop.
    """

    # cat design setup
    color_scheme = Colors(ui)       # init the colors
    font_scheme = FontScheme()
    ui.add_head_html(f'<style>{head_style}</style>')

    # status
    status(ui)
    status(ui, type="yellow")
    status(ui, type="red")

    # typography
    with box(ui, color_scheme):
        typography(ui, font_scheme, text="H1 Heading", variant="h1")
        typography(ui, font_scheme, text="H2 Heading", variant="h2")
        typography(ui, font_scheme, text="H3 Heading", variant="h3")
        typography(ui, font_scheme, text="H4 Heading", variant="h4")
        typography(ui, font_scheme, text="p1", variant="p1")
        typography(ui, font_scheme, text="p2", variant="p2")
        typography(ui, font_scheme, text="p3", variant="p3")
        typography(ui, font_scheme, text="caption", variant="caption")

    divider(ui)

    with ui.element('div').classes('flex flex-wrap w-full justify-between'):
        card(ui, font_scheme, color_scheme, "images/cat_card.png", "Hi! I am your cat.", "Feed me or I get angry.")
        card(ui, font_scheme, color_scheme, "images/cat_card2.png", "Hi! I am your cat.", "Feed me or I get angry.")
        card(ui, font_scheme, color_scheme, "images/cat_card3.png", "Hi! I am your cat.", "Feed me or I get angry.")

    divider(ui)

    notification(ui, font_scheme, color_scheme)
    # start the UI event loop
    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    """
    Entry point for the script. 

    This condition checks if the script is being run directly or imported as a module.
    If run directly, it calls the main function to initiate the UI.
    """
    main()
