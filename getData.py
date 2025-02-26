from dotenv import load_dotenv
import os
import requests
load_dotenv("ClientID.env")
#url="https://api.myanimelist.net/v2"
client_id = os.getenv("CLIENT_ID")
headers={"X-MAL-CLIENT-ID":client_id}