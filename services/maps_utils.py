import re
import urllib.parse

PLACE_WORDS = [
    "మాల్","mall","మాల","మాల్లు",
    "హోటల్","hotel","రెస్టారెంట్","restaurant",
    "ప్లేస్","place","పార్క్","park",
    "స్టేషన్","station","మెట్రో","metro",
    "బస్టాండ్","bus","stand","మార్కెట్","market",
    "టెంపుల్","temple","చర్చి","church","మస్జిద్","mosque",
    "హాస్పిటల్","hospital"
]

def normalize(text):
    return re.sub(r"\s+", "", text.lower())

def needs_map(text):
    t = normalize(text)
    for w in PLACE_WORDS:
        if normalize(w) in t:
            return True
    return False

def make_map_link(place):
    q = urllib.parse.quote(place + " Hyderabad")
    return f"https://www.google.com/maps/search/?api=1&query={q}"
