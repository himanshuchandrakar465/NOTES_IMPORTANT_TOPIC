import requests

url = "https://thispersondoesnotexist.com"

img = requests.get(url).content

with open("fake_person.jpg", "wb") as f:
    f.write(img)

print("Image saved")