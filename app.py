

import smtplib
import time

from routers.fetch_images import *

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

now = datetime.datetime.now()
#Bild herunterladen
date = now.strftime("%Y-%m-%d")
start_hour = now.hour
end_hour = now.hour
print(start_hour);
download_images("2024-04-30", 12, 12, "assets/downloaded_images")


# Hauptfunktion
def main():
  
    # recipient_email = 'empfaenger_email@example.com'
    #webcam_url = 'https://storage.roundshot.com/53aa8e920dd9e7.40757090/2024-04-30/12-30-00/2024-04-30-12-30-00_thumbnail.jpg'
    #webcam_url = 'https://archive1.roundshot.com/53aa8e920dd9e7.40757090/2023-12-02/12-30-00/2023-12-02-12-30-00_thumbnail.jpg'
    #fetch_webcam_image(webcam_url)
    #weather_info = detect_weather(tempURL)
    #print(weather_info)c
    #return weather_info
    # send_email(weather_info, recipient_email)

    if __name__ == '__main__':
        main()

