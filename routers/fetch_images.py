import requests
import os
from datetime import datetime, timedelta

def create_url(date, hour):
    base_url = "https://storage.roundshot.com/53aa8d33466fa9.62099805/"
    alt_base_url = "https://archive1.roundshot.com/53aa8d33466fa9.62099805/"

    url = f"{base_url}{date}/{hour}/{date}-{hour}_half.jpg"
    alt_url = f"{alt_base_url}{date}/12-00-00/{date}-12-00-00_half.jpg"

    return url, alt_url

def download_image(url, file_path):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded image: {file_path}")
        else:
            print(f"Failed to download image from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image from {url}: {str(e)}")

def download_images(date, start_hour, end_hour, save_dir):
    
    current_date = datetime.strptime(date, '%Y-%m-%d')
    hours = [f"{hour:02d}-00-00" for hour in range(start_hour, end_hour + 1)]

    for hour in hours:
        file_name = f"{current_date.strftime('%Y-%m-%d')}_{hour}.jpg"
        file_path = os.path.join(save_dir, file_name)

        if not os.path.exists(file_path):
            url, alt_url = create_url(current_date.strftime('%Y-%m-%d'), hour)
            download_image(url, file_path) or download_image(alt_url, file_path)
        else:
            print(f"Image already exists: {file_name}")

# Option 1: Herunterladen eines einzelnen Bildes
date = "2024-05-02"
start_hour = 13
end_hour = 13
save_directory = "assets/temp"

# # Option 2: Herunterladen einer Zeitspanne von Bildern
# date = "2024-04-15"
# start_hour = 10
# end_hour = 14
# save_directory = "assets/downloaded_images"

# Create the directory if it doesn't exist
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)

# # Call the function to download images
# download_images(date, start_hour, end_hour, save_directory)
