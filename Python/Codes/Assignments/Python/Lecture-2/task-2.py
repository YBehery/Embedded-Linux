import webbrowser
import requests
def firefox(url):
    webbrowser.open_new_tab(url)
    

x = requests.get('https://api.ipify.org/?format=json')
z={}
z=x.text[7:22]
firefox('https://ipinfo.io/'+z+'/geo')
