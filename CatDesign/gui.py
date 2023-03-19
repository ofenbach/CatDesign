from nicegui import ui, app
from pathlib import Path
import cat_design as cat

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

cat.setup(ui)
cat.top_bar(ui)

# typography
with ui.element('div').classes('justify-center p-12'):
    ui.label('H1').classes('text-white text-6xl')
    ui.label('H2').classes('text-white text-4xl')
    ui.label('H3').classes('text-white text-2xl')
    ui.label('H4').classes('text-white text-xl')
with ui.element('div').classes('justify-center p-12'):
    ui.label('P1').classes('text-white text-base')
    ui.label('P2').classes('text-white text-sm')

cat.tweet_card(ui=ui, profile_src='images/cat0.png', profile_name="Cat")
cat.divider(ui)
cat.status(ui, "green", "Everything cool.")
cat.status(ui, "yellow", "Be careful.")
cat.status(ui, "red", "Cat's hungry!")
cat.divider(ui)
cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
cat.divider(ui)
cat.textfield(ui)
cat.divider(ui)
cat.notification(ui)
cat.notification(ui, color="#92FF6C")
cat.notification(ui, color="#FF6C6C")
cat.notification(ui, color="#FCFF6C")

ui.run()
