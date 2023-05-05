import spotipy, json, time, random, signal, os
from instagrapi import Client
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

#Don't forget to run login.py if you're running this for the first time

#Instagram login from json file
print("Spotinotes : Spotify now playing to instagram new notes")
cl = Client(json.load(open('login.json')))
current_note = ""
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                               redirect_uri="http://localhost",
                                               scope="user-read-currently-playing",
                                               open_browser=False))
def Wait(random):   
    print("Waiting " + str(random) + "s")
    time.sleep(random)  
    
def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
signal.signal(signal.SIGINT, handler)
  
while True:
    track = sp.current_user_playing_track()
    try: 
        np = track['item']['name'] + " 🎶 " + track['item']['album']['artists'][0]['name']
    except: 
        np = None
    if np != None: 
        if np != current_note:
            try: 
                current_note = np
                cl.send_note(np,0)
                print("Sent")
                Wait(random.randint(200,230))
            except Exception as e:
                print("Can't Add :")
                print(e)
                print("You might need to login again with login.py")
                break
        else: 
            print("Same song")
            Wait(random.randint(30,50))
    else:
        print('Nothing playing')
        Wait(random.randint(30,100))