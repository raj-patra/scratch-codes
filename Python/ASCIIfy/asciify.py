import sys

from PIL import Image, ImageDraw

ASCII_SET = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = old_height / old_width
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image, new_width, new_height

def pixel_to_ascii(image, buckets=25):
    pixels = list(image.getdata())
    new_pixels = [ASCII_SET[pixel_value // buckets] for pixel_value in pixels]
    return "".join(new_pixels)

def save_image(ascii_str, new_width, new_height):
    image = Image.new(mode="RGB", size=(new_width * 11, new_height * 11), color="white")
    draw = ImageDraw.Draw(image)
    draw.multiline_text((0, 0), ascii_str, fill=(0, 0, 0), align="center", spacing=0)
    image.save("output.png")

def asciify(img_path):
    try:
        image = Image.open(img_path)
    except Exception:
        print("Unable to find image in", img_path)
        return
    
    image, new_width, new_height = resize(image)
    gray_image = image.convert("L")
    ascii_char_list = pixel_to_ascii(gray_image)

    len_ascii_list = len(ascii_char_list)
    ascii_str = ""
    ascii_str = "".join([ascii_str + i + i for i in ascii_char_list])

    ascii_str = [
        ascii_str[index : index + 2 * new_width]
        for index in range(0, 2 * len_ascii_list, 2 * new_width)
    ]
    ascii_str = "\n".join(ascii_str)

    save_image(ascii_str, new_width, new_height)
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = str(" ".join(sys.argv[1:]))
    asciify(img_path)
