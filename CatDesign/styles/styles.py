from nicegui import ui
from colors import ColorScheme
from fonts import FontScheme

# Initialize the ui and style objects
ui_obj = ui
color_scheme = ColorScheme(ui_obj)
font_scheme = FontScheme()

# Add the basic styles to the head
head_style = """
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
body {
    font-family: 'Poppins';
    background-color: #0A0B0C;
    margin: 0;
}
"""
ui_obj.add_head_html(f'<style>{head_style}</style>')
