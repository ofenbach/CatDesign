from nicegui import ui, app
from pathlib import Path
import cat_design as cat

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

cat.setup(ui)
cat.top_bar(ui)
cat.typography_examples(ui)
cat.tweet_card(ui=ui, profile_src='images/cat0.png', profile_name="Cat")
cat.divider(ui)
cat.status(ui, "green", "Everything cool.")
cat.status(ui, "yellow", "Be careful.")
cat.status(ui, "red", "Cat's hungry!")
cat.divider(ui)
with ui.element('div').classes('w-full flex justify-between'):
    cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
    cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
    cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
    cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
cat.divider(ui)
with ui.element('div').style('width: 50%;'):
    cat.horizontal_card(ui, "Hi! I am your cat.", "Message below. Important information. Message below. Important information. Message below. Important information. Message below. Important information.")
cat.divider(ui)
cat.textfield(ui)
cat.divider(ui)
cat.notification(ui)
cat.notification(ui, color="#92FF6C")
cat.notification(ui, color="#FF6C6C")
cat.notification(ui, color="#FCFF6C")

ui.run()
