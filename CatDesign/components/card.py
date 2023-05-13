from CatDesign.components.divider import divider
from CatDesign.components.typography import typography


def card(ui, font_scheme, color_scheme, img_src="", header="Heading", sub_header="Subheading"):
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
                    border: 0px;
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

    with ui.element('div').classes('card'):
        with ui.row().classes('image_card_hover'):
            ui.image(img_src).classes('rounded-2 w-80 h-44')

        divider(ui)

        with ui.row():
            typography(ui, font_scheme, header, "h4")

        with ui.row().classes('mt-4'):
            typography(ui, font_scheme, sub_header, "p2")


