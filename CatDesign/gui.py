from nicegui import ui, app
from pathlib import Path
import cat_design

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder

cat = cat_design.CatDesign(ui)

cat.top_bar(links=[('https://google.com', 'Google'), ('https://ebay.com', 'eBay')])   # default links is just nicegui website

with cat.box(classes='mt-8 ml-8 w-1/2'):                             # box is a div with cat styling applied
    cat.typography("H1 - XL Heading", "h1")           # label element with cat styling
    cat.typography("H2 - L Heading", "h2")
    cat.typography("H3 - M Heading", "h3")
    cat.typography("H4 - S Heading", "h4")

with cat.box(classes='mt-8 ml-8 w-1/2'):  # box is a div with cat styling applied
    cat.typography("P1 - XL Heading", "p1")  # label element with cat styling
    cat.typography("P2 - L Heading", "p2")
    cat.typography("P3 - M Heading", "p3")

cat.divider()                               # default cat divider
#cat.divider(classes='mt-12')                # custom tailwind possible
#cat.divider(style='background-color: red;') # custom css possible

cat.typography("Textfield / Input", variant="h1")
cat.typography("Input field styled with css animation.", variant="p1")
cat.textfield()

cat.divider()

cat.typography("Card", variant="h1")
cat.typography("Card Element with picture, heading and subheader", variant="p1")
with ui.element('div').classes('flex flex-wrap w-full justify-between'):
    cat.card("images/cat_card.png", "Hi! I am your cat.", "Feed me or I get angry.")
    cat.card("images/cat_card2.png", "Hi! I am your cat.", "Feed me or I get angry.")
    cat.card("images/cat_card3.png", "Hi! I am your cat.", "Feed me or I get angry.")

cat.divider()

cat.typography("Status", variant="h1")
cat.typography("Displays state of e.g. servers, three states", variant="p1")
with cat.div().classes('flex flex-wrap w-full justify-between'):
    cat.status("green", "Everything cool.")
    cat.status("yellow", "Be careful.")
    cat.status("red", "Cat's hungry!")

cat.divider()

cat.typography("Box", variant="h1")
cat.typography("A box is a styled div using cat theme colors.", variant="p1")
with cat.box():
    cat.typography("I am a typography element inside a box element!", "h1")

cat.divider()
cat.typography("Notification", variant="h1")
cat.typography("Notification Banner with message and submessage", variant="p1")
with cat.div().classes('flex flex-wrap w-full justify-between'):
    cat.notification()
    cat.notification(color="#92FF6C")
    cat.notification(color="#FF6C6C")
    cat.notification(color="#FCFF6C")
cat.divider()

cat.typography("Tweetcard", variant="h1")
cat.typography("WIP, needs updated font and updated elements using cat elements", variant="p1")
cat.tweet_card(
    profile_src='images/cat0.png', profile_name="Cat")

cat.footer()


"""
cat.typography("Horizontal Card", variant="h1")
cat.typography("Card Element with picture, heading and subheader", variant="p1")
with ui.element('div').style('width: 50%;'):
    cat.horizontal_card(ui, "Hi! I am your cat.", "Message below. Important information. Message below. Important information. Message below. Important information. Message below. Important information.")

cat.newsletter()
"""

ui.run()
