import pyqrcode, sys

def qr():
    if sys.argv[1:]:
        url = sys.argv[1:][0]

        code = pyqrcode.create(url, error='H', version=27, mode='binary')
        code.png('code.png', scale=5, module_color=[0, 0, 0, 128], background=(255, 255, 255, 255))
    else:
        print("Pass the input text/url as command line argument")
        print("Sample Usage: py qr.py www.google.com")

if __name__ == "__main__":
    qr()