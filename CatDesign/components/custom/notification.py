from CatDesign.components.basics.typography import typography
from CatDesign.components.layout.div import div


def notification(ui, font_scheme, color_scheme, header, subheader, css='', tailwind='', color="#6CCAFF"):
    """ Note this still uses Poppins, todo: typography update """

    with div(ui, css=css, tailwind=tailwind):
        with ui.element('div').style(
                f'padding-top: 16px; padding-bottom: 16px; padding-left: 32px; padding-right: 32px; background-color: {color_scheme.color_box}; border: 1px solid {color_scheme.color_border}; border-left: 8px solid {color}; border-radius: 8px;'):
            typography(ui, font_scheme, header, variant="h2", css="margin-bottom: 16px;")
            ui.label(subheader).style('font-size: 16px; color: #A6A6A6;')

