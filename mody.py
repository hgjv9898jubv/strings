import os


class Mody(object):
    ELHYBA = os.environ.get("ELHYBA", "")

    API_ID = int(os.environ.get("API_ID", 25281175))

    API_HASH = os.environ.get("API_HASH", "6d99cb2b60a2c519fc1f99bd19565730")
    
    OWNER = int(os.environ.get("OWNER", 6581896306))
