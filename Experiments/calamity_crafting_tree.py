import requests


url = "https://calamitymod.wiki.gg/wiki/Living_Dew"

response = requests.get(url)

html_content = response.text


print(html_content)