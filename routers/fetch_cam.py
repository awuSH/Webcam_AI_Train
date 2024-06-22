import requests
from io import BytesIO
import datetime
import numpy as np
from PIL import Image, ImageDraw, ImageFont

tempURL = "assets/temp_image.jpg"

def fetch_webcam_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    add_info_image_and_save(image, tempURL)
    print("Image saved to:", tempURL)

def add_info_image_and_save(image, output_path):
    draw = ImageDraw.Draw(image)
    current_datetime = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    txt = f"{output_path} | {current_datetime}"
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 40)
    draw.text((100, 100), txt, fill=(0, 0, 0), font=fnt)
    image.save(output_path)
    image.show()
