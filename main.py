import ctypes
from pathlib import Path

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)

def main():
    image_name = "greenbluebg.jpg"
    image_path = Path.cwd() / 'wallpaper-scraper' / 'images' / image_name
    set_wallpaper(str(image_path))

if __name__ == '__main__':
    main()
