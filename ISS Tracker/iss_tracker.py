# json convert the python dictionary above into a json
import json
import turtle
# urllib.request fetch URLs using a variety of different protocols
import urllib.request
import time
# webbrowser provides a high-level interface to allow displaying Web-based documents to users
import webbrowser
# geocoder takes the data and locate these locations in the map
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " +
           str(result["number"]) + " astronauts on the ISS: \n\n")  # prints number of astronauts
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")  # prints names of crew
# print long and lat
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-190, -90, 190, 90)
screen.bgpic(
    r'C:\Users\H.P\OneDrive\Desktop\Projects\ISS Tracker\images\map.gif')
screen.title("ISS Tracker by Aditya Trivedi")
screen.register_shape(
    r"C:\Users\H.P\OneDrive\Desktop\Projects\ISS Tracker\images\iss.gif")
iss = turtle.Turtle()
iss.shape(r"C:\Users\H.P\OneDrive\Desktop\Projects\ISS Tracker\images\iss.gif")
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    resp = urllib.request.urlopen(url)
    result = json.loads(resp.read())
    location = result["iss_position"]
    latitude = location['latitude']
    longitude = location['longitude']
    latitude = float(latitude)
    longitude = float(longitude)
    iss.goto(longitude, latitude)

