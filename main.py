import ctypes

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)

def main():
    set_wallpaper("C:\\Users\\Gerald\\Documents\\Personal\\Coding\\Projects\\wallpaper-scraper\\images\\darjeeling.jpg")

if __name__ == '__main__':
    main()
