from nicegui import ui, app
from pathlib import Path
import cat_design as cat

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

cat.setup(ui)
cat.tweet_card(ui=ui, profile_src='images/cat0.png', profile_name="Cat")
cat.divider(ui)
cat.status(ui, "green", "Everything cool.")
cat.status(ui, "yellow", "Be careful.")
cat.status(ui, "red", "Cat's hungry!")
cat.divider(ui)
cat.card(ui, "Hi! I am your cat.", "Feed me or I get angry.")
cat.divider(ui)
cat.textfield(ui)

ui.run()
