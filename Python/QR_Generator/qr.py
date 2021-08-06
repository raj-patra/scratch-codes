import pyqrcode, sys

def qr():
    url = sys.argv[1:][0]

    code = pyqrcode.create(url, error='H', version=27, mode='binary')
    code.png('code.png', scale=5, module_color=[0, 0, 0, 128], background=(255, 255, 255, 255))


if __name__ == "__main__":
    qr()