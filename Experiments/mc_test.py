import requests
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# Load Minecraft text image
minecraft_image = cv2.imread('sample.png')

# Perform OCR
minecraft_text = pytesseract.image_to_string(minecraft_image)

# Output the recognized text
print(minecraft_text)


userInput = input("player name: ")
url = f"https://stats.pika-network.net/api/profile/{userInput}"
bedwarsUrl = f"https://stats.pika-network.net/api/profile/{userInput}/leaderboard?type=bedwars&interval=lifetime"

# Send an HTTP GET request to the URL to fetch the data
response = requests.get(url)
responseBedwars = requests.get(bedwarsUrl)

if response.status_code == 200:
    data = response.json()
    dataBedwars = responseBedwars.json()

    username = data.get("username")
    level = data.get("rank", {}).get("level")
    finalKills = dataBedwars.get("Final kills", {}).get("entries", [])[0].get("value")
    losses = dataBedwars.get("Losses", {}).get("entries", [])[0].get("value")
    wins = dataBedwars.get("Wins", {}).get("entries", [])[0].get("value")

    if username:
        print(f"username: {username}")
        print(f"level: {level}")
        print(f"fkdr: {int(finalKills) / int(losses):.2f}")
        print(f"wins: {wins}")
    else:
        print("No username found in the data.")
else:
    print(f"Request failed with status code: {response.status_code}")
