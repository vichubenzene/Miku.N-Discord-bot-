from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
def get_episode_link(animeid, episode_num):
    try:
            animelink = f'https://gogoanime.cm/category/{animeid}'
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            lnk = soup.find(id="episode_page")
            source_url = lnk.find("li").a
            tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            URL_PATTERN = 'https://gogoanime.pe/{}-episode-{}'
            url = URL_PATTERN.format(animeid, episode_num)
            srcCode = requests.get(url)
            plainText = srcCode.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("li", {"class": "dowloads"}).a
            vidstream_link = source_url.get('href')
            return (vidstream_link)
    except AttributeError:
            return {"status":"400", "reason":"Invalid animeid or episode_num"}
    except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}
