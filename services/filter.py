from services.hyd_places import HYD_PLACES

def normalize(t):
    return t.lower().replace(" ", "")

def hyd_filter(text):
    t = normalize(text)

    # Direct Hyderabad mention
    if "హైదరాబాద్" in t or "hyderabad" in t:
        return True

    # Count how many Hyderabad places appear
    count = 0
    for p in HYD_PLACES:
        if normalize(p) in t:
            count += 1
            if count >= 1:      # >=1 makes any local query valid
                return True

    return False
