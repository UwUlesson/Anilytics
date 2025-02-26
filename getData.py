from dotenv import load_dotenv
import os
import requests
load_dotenv("ClientID.env")
response = requests.get("https://api.myanimelist.net/v2")
client_id = os.getenv("CLIENT_ID")