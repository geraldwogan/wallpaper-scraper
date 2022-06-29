# wallpaper-scraper

## Overview:
Create a script that will scrape an image and programmatically set that image as a desktop wallpaper. This script will run each day using Windows Task Scheduler.

## Main functionality:
- Find appealing images online.
    - Find the top post of the day from reddit.com/r/art; these will be popular images that are frequently updated. 
- Scrape image and save image to /images folder.
- Programmatically set a wallpaper (on Windows for the moment).
- Setup for running daily through 'Task Scheduler' - add this to repo as .txt file.

### Extra functionality
- Delete the previous days image.
- Can the OS be detected? If so, run conditionl code for Windows/macOS/Linux.
- Fit image to screen aspect ratio.
    - Detect main monitor aspect ratio.
    - Detect image aspect ratio.
        - Iterate through images until matching ratio is found.
