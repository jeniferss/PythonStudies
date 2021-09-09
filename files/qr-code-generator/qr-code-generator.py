import pyqrcode
from PIL import Image


def generate(file_name, link):
    file_name = f'{file_name}.png'
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    Image.open(file_name)


generate('youtube', 'https://www.youtube.com')
