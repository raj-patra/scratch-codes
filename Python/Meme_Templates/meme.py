from os import name, terminal_size
import requests, shutil

memes = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']

print("\nTop memes from ImgFlip:\n")
for i in range(len(memes)):
    print("{} - {}".format(i+1, memes[i]["name"]))

index = int(input("\nEnter the serial number you want to download: "))

url = memes[index-1]["url"]
filename = memes[index-1]["name"] + "." + url.split('.')[-1]

image_data = requests.get(url, stream=True)

if image_data.status_code == 200:
    image_data.raw.decode_content = True

    with open(filename, 'wb') as f:
        shutil.copyfileobj(image_data.raw, f)
        print("Meme successfully downloaded: {}".format(filename))
else:
    print("Could not retrieve meme")
