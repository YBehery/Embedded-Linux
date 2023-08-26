
import webbrowser

def firefox(str):
    webbrowser.open_new_tab(str)

sites_menu={'google':'www.google.com',
            'facebook':'www.facebook.com',
            'youtube':'www.youtube.com',
            'linkedin':'www.linkedin.com'}
print(sites_menu.keys())
choice=input('choose site\n')
firefox(sites_menu[choice])