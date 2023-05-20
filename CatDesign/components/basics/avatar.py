def avatar(ui, img_src, css='', tailwind=''):
    ui.image(img_src).style('border-radius: 50%; height: 32px; width: 32px;' + css).tailwind(tailwind)