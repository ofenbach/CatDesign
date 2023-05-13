def avatar(ui, src, style=""):
    ui.image(src).style('border-radius: 50%; height: 32px; width: 32px;' + style)