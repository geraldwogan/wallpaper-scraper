import ctypes
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.request import urlopen

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)

def get_image_link():
    htmldata = urlopen("https://www.reddit.com/r/art/top/?t=day")
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img') # data-url="https://i.redd.it/l9gjoxwomz891.jpg"
    
    for item in images:
        print(item['src'])


def main():
    # image_name = "greenbluebg.jpg"
    # image_path = Path.cwd() / 'wallpaper-scraper' / 'images' / image_name
    # set_wallpaper(str(image_path))
    get_image_link()

if __name__ == '__main__':
    main()


