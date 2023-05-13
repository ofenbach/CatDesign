from nicegui import app
from pathlib import Path

from CatDesign.cat_design import CatDesign

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder


def main():
    """
    The main function to initiate the UI.
    """

    cat = CatDesign()

    # typography
    cat.typography(text="Typography (in a box)", variant="h1", css='margin-top: 2em;', tailwind='ml-8')
    with cat.box():
        cat.typography(text="H1 Heading", variant="h1")
        cat.typography(text="H2 Heading", variant="h2")
        cat.typography(text="H3 Heading", variant="h3")
        cat.typography(text="H4 Heading", variant="h4")
        cat.typography(text="H5 Heading", variant="h5")
        cat.typography(text="H6 Heading", variant="h6")
        cat.typography(text="Subtitle 1", variant="subtitle1")
        cat.typography(text="Subtitle 2", variant="subtitle2")
        cat.typography(text="Body 1", variant="body1")
        cat.typography(text="Body 2", variant="body2")

    cat.divider()


if __name__ in {"__main__", "__mp_main__"}:
    """
    Entry point for the script. 

    This condition checks if the script is being run directly or imported as a module.
    If run directly, it calls the main function to initiate the UI.
    """
    main()
