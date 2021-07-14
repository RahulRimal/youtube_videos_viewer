from os import close
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

# Initiate the browser
browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

channel_id = "UCOVqNzeei1g-abluX8ub62w"


def open_youtube_channel(channel_id):
    browser.get('https://www.youtube.com/channel/' + channel_id + '/videos')


def get_videos_links():
    videos_links = []
    videos = browser.find_elements_by_id('thumbnail')

    for video in videos:
        video_link = video.get_attribute('href')
        videos_links.append(video_link)

    return videos_links


def open_videos_new_tab(videos_links):
    for x in range(len(videos_links) - 1):
        browser.execute_script("window.open('"+videos_links[x]+"');")
        time.sleep(3)


def close_tab(index):
    browser.switch_to_window(browser.window_handles[index])
    browser.close()


open_youtube_channel(channel_id)
links = get_videos_links()
open_videos_new_tab(links)

close_tab(0)
