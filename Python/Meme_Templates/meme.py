from os import name
import requests, shutil

memes = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']

print("\nTop memes from ImgFlip:\n")
for i in range(len(memes)):
    print("{} - {}".format(i+1, memes[i]["name"]))


