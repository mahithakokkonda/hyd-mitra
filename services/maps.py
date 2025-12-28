import urllib.parse

def maps_link(place):
    base = "https://www.google.com/maps/search/?api=1&query="
    return base + urllib.parse.quote(place + " Hyderabad")
