import requests
import argparse
from bs4 import BeautifulSoup


def get_lyrics(artist, song):
    artist = "".join(artist.lower().split())
    song = "".join(song.lower().split())
    song_url = "http://www.azlyrics.com/lyrics/{}/{}.html".format(artist, song)

    response = requests.get(song_url)

    soup = BeautifulSoup(response.content, "html.parser")
    try:
        lyrics = soup.find("div", class_="col-xs-12 col-lg-8 text-center").find_all("div")[5].text
        print(lyrics)
    except AttributeError:
        print("Couldn't find lyrics")


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("--artist", action="store", type=str, required=True, help="Enter the name of the artist/ band")
    my_parser.add_argument("--song", action="store", type=str, required=True, help="Enter the name of the song")

    args = my_parser.parse_args()
    
    artist = args.artist
    song = args.song
    
    get_lyrics(artist, song)