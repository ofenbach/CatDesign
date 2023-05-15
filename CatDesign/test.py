from fontawesome import icons

def icon(icon_name, color='#FFFFFF', css='', tailwind=''):
    svg_content = icons.get(icon_name)
    print(svg_content)

icon('share')
