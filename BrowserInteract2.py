import webbrowser #Makes it possible to interract with webbrowser
import requests
import os #Imports operating system hints "OS"
from bs4 import BeautifulSoup #bs4 = packet, BeautifulSoup = Class
#Used for analysing HTML and XML - Typical for web scraping


URL = "https://www.youtube.com/watch?v=w5S6vKgjeRY" #Specifies a URL - Enter whatever youtube link

webbrowser.open(URL) #Tells to open the set URL - Can be removed and code still works if you don't wonna open the browser

output = requests.get(URL) #Gets the HTML code from the specified site
soup = BeautifulSoup(output.text, 'html.parser') #Makes the HTML searchable

title = soup.find('title').text #Defines title and makes it find title, and .text makes sure it only takes the title and not the <title>*Video title*</title>


if " - YouTube" in title:
    title = title.replace(" - YouTube", "") #Removes the "- youtube" from the title

with open("output.txt", "a") as file: #Opens output.txt instead of overwriting or reading
    file.write("Video Title: " + title + "\n") #Automaticly saves the video title

print("Title saved:", title) #Prints to confirm that it has saved
