from CatDesign.components.basics.typography import typography


def notification(ui, font_scheme, color_scheme, header_message="Meow-tification", message="Time to refill the food bowl, hooman!",
                 color="#6CCAFF"):
    """ Note this still uses Poppins, todo: typography update """

    def div():
        """Create a div element."""
        return ui.element('div')

    with div().style(
            f'padding-top: 16px; padding-bottom: 16px; padding-left: 32px; padding-right: 32px; background-color: {color_scheme.color_box}; border: 1px solid {color_scheme.color_border}; border-left: 8px solid {color}; border-radius: 8px;'):
        typography(ui, font_scheme, header_message, variant="h2", style="margin-bottom: 16px;")
        ui.label(message).style('font-size: 16px; color: #A6A6A6;')

