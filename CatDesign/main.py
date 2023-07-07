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

    with cat.div(tailwind='ml-16 mr-16'):

        # typography
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Typography (in a box)', variant='h1', css='margin-top: 2em;', tailwind='ml-8')

        with cat.div(tailwind='flex w-full justify-center mt-8'):
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

        # card
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Card', variant='h1')
        # Card 1
        with cat.div(tailwind='flex w-full justify-center mt-8'):
            cat.card(header="Feline Facts", sub_header="Explore the fascinating world of cats.", tailwind='mr-0 lg:mt-0 lg:mr-8')

            # Card 2
            cat.card(img_src='./images/cat_card2.png', header="Purr-fect Companions",
                     sub_header="Discover why cats make such great pets.", tailwind='mr-0 mt-8 lg:mt-0 lg:mr-8')

            # Card 3
            cat.card(img_src='./images/cat_card3.png', header="Cats of the World",
                     sub_header="Learn about the various breeds of cats.", tailwind='mr-0 mt-8 lg:mt-0 lg:mr-8')

        cat.divider()

        # notification
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Notification', variant='h1')
        with cat.div(tailwind='flex w-full justify-center mt-8'):
            cat.notification()     # header and sub_header param possible (string)
            cat.notification(header="Cat Food Recall",
                             sub_header="Brand X has issued a recall for their tuna flavored cat food.", tailwind='mr-8 ml-8')
            cat.notification(header="Vet Appointment Reminder",
                             sub_header="Don't forget your cat's annual check-up appointment next week.", tailwind='mt-8')

        cat.divider()

        # chip
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Chip', variant='h1')
        with cat.div(tailwind='flex w-full justify-center mt-4'):
            cat.typography(text="Chips are compact elements that represent an input, attribute, or action.",
                           variant='body1')
        with cat.div(tailwind='flex w-full justify-center mt-8'):
            cat.chip(variant='outlined')
            cat.chip(variant='filled', css='margin-left: 64px;')

        cat.divider()


        # rating
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Rating', variant='h1')
        with cat.div(tailwind='flex w-full justify-center mt-4'):
            cat.typography(text="Ratings provide insight regarding others' opinions and experiences, and can allow the user to submit a rating of their own.",
                           variant='body1')

        with cat.div(tailwind='flex w-full justify-center mt-8'):
            cat.rating()

        cat.divider()

        # alerts
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Alerts', variant='h1')

        with cat.div(tailwind='flex w-full justify-center mt-4'):
            cat.typography(text="An alert displays a short, important message in a way that attracts the user's attention without interrupting the user's task.",
                           variant='body1')
        with cat.div(tailwind='flex flex-wrap w-full justify-between mt-8'):
            cat.alert(type='info', message='This is an info alert — check it out!', css="border-radius: 100px;")
            cat.alert(type='warning', message='This is a warning alert — check it out!', css="border-radius: 100px;")
            cat.alert(type='error', message='Please enter correct e-mail', css="border-radius: 100px;")
            cat.alert(type='success',  css="border-radius: 100px;", tailwind='mr-8')        # css and tailwind works

        cat.divider()

        # icons
        with cat.div(tailwind='flex w-full justify-center'):
            cat.typography(text='Icons', variant='h1')

        with cat.div(tailwind='flex w-full justify-center mt-4'):
            cat.typography(text='To incorporate icons, invoke the "icon" method, specifying the name of the icon as well as'
                                'your preferred style variant. The icon names correspond to those found on the Heroicons'
                                'website (https://heroicons.com/).', variant='body1')

        """cat.typography(text='If no variant is specified, the default is "outlined".', variant='body1')
        cat.typography(text='Example:', variant='body2')
        cat.typography(text="cat.icon('share', variant='filled')", variant='body2')
        cat.icon('share', variant='filled')
        cat.typography(text="This will create a filled 'share' icon.", variant='body2')
        cat.typography(text="You can also change the color of the icon.", variant='body2')
        cat.typography(text="Example:", variant='body2')
        cat.typography(text="cat.icon('share', color='red')", variant='body2')
        cat.icon('share', color='red')
        cat.typography(text="This will create a 'share' icon in red color.", variant='body2')"""

        with cat.div(tailwind='flex justify-between w-full mt-16'):
            cat.icon('share')
            cat.icon('like')
            cat.icon('star')
            cat.icon('settings')
            cat.icon('hamburger')
            cat.icon('refresh')
            cat.icon('bell')
            cat.icon('chevron-left')
            cat.icon('chevron-right')

        with cat.div(tailwind='flex justify-between w-full mt-16 mb-16'):
            cat.icon('cloud')
            cat.icon('minus-circle')
            cat.icon('ellipsis')
            cat.icon('envelope')
            cat.icon('envelope-open')
            cat.icon('trash')
            cat.icon('map')
            cat.icon('map-pin')
            cat.icon('hand-thumb-up')

        with cat.div(tailwind='flex justify-between w-full mt-16 mb-16'):
            cat.icon('arrow-down')
            cat.icon('arrow-left')
            cat.icon('arrow-right')
            cat.icon('arrow-up')
            cat.icon('arrow-up-left')
            cat.icon('arrow-up-right')
            cat.icon('arrow-down-left')
            cat.icon('arrow-down-right')


        cat.divider()

    cat.bar_chart()

    cat.line_chart(css='margin-top: 200px; margin-bottom: 200px; width: 80%;', tailwind='ml-16')

    cat.avatar(css='width: 64px; height: 64px;')


    cat.tweet_card(profile_src='./images/cat0.png')


if __name__ in {'__main__', '__mp_main__'}:
    """
    Entry point for the script. 

    This condition checks if the script is being run directly or imported as a module.
    If run directly, it calls the main function to initiate the UI.
    """
    main()
