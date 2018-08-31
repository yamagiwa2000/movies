# 20180823

import requests
import time
from bs4 import BeautifulSoup

top_url = "https://yts.am/browse-movies/0/all/all/0/year"
dstfile = "./data.txt"
#lastpage = 3
lastpage = 418

def find_movie_links(no, url):
    page_num = no
    link_num = 1
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.find_all("a", class_="browse-movie-title")
    with open(dstfile, mode="a") as f:
        for a in movies:
            link = a.get("href")
            namae = a.get_text()
            f.write(str(page_num) + "-" + str(link_num) + ".\t" + namae + ": " + link + "\n")
            link_num += 1
        f.write("\n")

# data file initialize
with open(dstfile, mode="w") as n:
    n.write("yts.am movie torrent file lists: \n\n")

curr = 1
while curr <= lastpage:
    if curr == 1:
        print("processing page.1 ...")
        find_movie_links(1, top_url)
    else:
        print("processing page." + str(curr) + " ...")
        links = top_url + "?page=" + str(curr)
        find_movie_links(curr, links)
    curr += 1
    time.sleep(1)
