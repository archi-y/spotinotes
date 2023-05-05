from instagrapi import Client
import json

print("Instagram Login :")
username = input("Username : ")
password = input("Password : ")
choice = input("Are you using TOTP ? (SMS won't work) [Y] / [N] : ")
if choice =="Y":
    print("Login using password and username with TOTP")
    totp = input("TOTP : ")
    try:
        cl = Client()
        cl.login(username,password,verification_code=totp)
        json.dump(
            cl.get_settings(),
            open('login.json', 'w')
        )
    except:
        print("Can't login to instagram, please verify your username/password")
else: 
    print("Login using password and username")
    try:
        cl = Client()
        cl.login(username,password)
        json.dump(
            cl.get_settings(),
            open('login.json', 'w')
        )
    except:
        print("Can't login to instagram, please verify your username/password")
cl = Client(json.load(open('login.json')))
print("Spotify keys :")
print("To do this you must first create an application on developer.spotify.com with 'http://localhost' as a redirect url - More info in README")
