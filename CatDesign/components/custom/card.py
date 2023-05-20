from CatDesign.components.basics.divider import divider
from CatDesign.components.basics.typography import typography
from CatDesign.components.layout.div import div


def card(ui, font_scheme, color_scheme, img_src="", header="Heading", sub_header="Subheading", css="", tailwind=""):
    style = f"""
                .card {{
                    padding: 24px;
                    background-color: {color_scheme.color_box};
                    border: 1px solid {color_scheme.color_border};
                    border-radius: 8px;
                    transition: 0.3s;
                }}
                .card:hover {{
                    transition: 0.3s;
                    box-shadow: 0px 0px 24px rgba(255,255,255,0.06);
                    border: 1px solid rgba(0,0,0,0);
                }}
                .image_card_hover {{
                    transition: 0.3s;
                }}
                .image_card_hover:hover {{
                    transition: 0.3s;
                    transform: scale(1.1);
                    cursor: pointer;
                }}
                """
    ui.add_head_html(f'<style>{style}</style>')

    with div(ui, css=css, tailwind=tailwind):
        with ui.element('div').classes('card'):

            with ui.row().classes('image_card_hover'):
                ui.image(img_src).classes('rounded-2 w-80 h-44')

            divider(ui)

            with ui.row():
                typography(ui, font_scheme, header, "h4")

            with ui.row().classes('mt-4'):
                typography(ui, font_scheme, sub_header, "body1")


