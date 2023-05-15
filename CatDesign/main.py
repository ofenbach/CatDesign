from nicegui import app
from pathlib import Path

from CatDesign.cat_design import CatDesign

folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)  # serve all files in this folder


def main():
    """
    The main function to initiate the UI.
    """

    cat = CatDesign()

    # typography
    cat.typography(text='Typography (in a box)', variant='h1', css='margin-top: 2em;', tailwind='ml-8')
    with cat.box():
        cat.typography(text='H1 Heading', variant='h1')
        cat.typography(text='H2 Heading', variant='h2')
        cat.typography(text='H3 Heading', variant='h3')
        cat.typography(text='H4 Heading', variant='h4')
        cat.typography(text='H5 Heading', variant='h5')
        cat.typography(text='H6 Heading', variant='h6')
        cat.typography(text='Subtitle 1', variant='subtitle1')
        cat.typography(text='Subtitle 2', variant='subtitle2')
        cat.typography(text='Body 1', variant='body1')
        cat.typography(text='Body 2', variant='body2')

    cat.divider()
    cat.card()
    cat.divider()

    cat.typography(text='Notification', variant='h1')
    with cat.div(tailwind='flex flex-wrap w-full justify-between'):
        cat.notification()     # header_message and message param possible (string)
        cat.notification()
        cat.notification()

    cat.divider()

    cat.typography(text='Chip', variant='h1')
    with cat.div(tailwind='flex flex-wrap w-full'):
        cat.chip(variant='outlined')
        cat.chip(variant='filled', css='margin-left: 64px;')

    cat.divider()
    cat.typography(text='Rating', variant='h1')
    cat.rating()
    cat.divider()

    cat.typography(text='Alerts', variant='h1')
    with cat.div(tailwind='flex flex-wrap w-full justify-between'):
        cat.alert(type='info', message='This is an info alert — check it out!')
        cat.alert(type='warning', message='This is a warning alert — check it out!')
        cat.alert(type='error', message='Please enter correct e-mail')
        cat.alert(type='success',  css="border-radius: 100px;", tailwind='mr-8')        # css and tailwind works
    cat.divider()

    cat.typography(text='Icons', variant='h1')
    cat.typography(text='To use icons, use the icon method with the name of the icon and the desired variant.', variant='body1')
    cat.typography(text='If no variant is specified, the default is "outlined".', variant='body1')
    cat.typography(text='Example:', variant='body2')
    cat.typography(text="cat.icon('share', variant='filled')", variant='body2')
    cat.icon('share', variant='filled')
    cat.typography(text="This will create a filled 'share' icon.", variant='body2')
    cat.typography(text="You can also change the color of the icon.", variant='body2')
    cat.typography(text="Example:", variant='body2')
    cat.typography(text="cat.icon('share', color='red')", variant='body2')
    cat.icon('share', color='red')
    cat.typography(text="This will create a 'share' icon in red color.", variant='body2')


    cat.typography('List of all icons:')
    with cat.div(tailwind='flex justify-between w-full'):
        cat.icon('share')
        cat.icon('like')
        cat.icon('star')
        cat.icon('settings')
        cat.icon('hamburger')
        cat.icon('refresh')
        cat.icon('bell')
        cat.icon('chevron-left')
        cat.icon('chevron-right')

    with cat.div(tailwind='flex justify-between w-full mt-4'):
        cat.icon('cloud')
        cat.icon('minus-circle')
        cat.icon('ellipsis')
        cat.icon('envelope')
        cat.icon('envelope-open')
        cat.icon('trash')
        cat.icon('map')
        cat.icon('map-pin')
        cat.icon('hand-thumb-up')

    cat.divider()


    cat.tweet_card(profile_src='./images/cat0.png')


if __name__ in {'__main__', '__mp_main__'}:
    """
    Entry point for the script. 

    This condition checks if the script is being run directly or imported as a module.
    If run directly, it calls the main function to initiate the UI.
    """
    main()
