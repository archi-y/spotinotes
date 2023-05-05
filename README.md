Show what you're listening to on spotify in instagram notes

![size](https://shields.io/github/repo-size/archi-y/spotinotes)
![license](https://shields.io/github/license/archi-y/spotinotes)
![issues](https://img.shields.io/github/issues-raw/archi-y/spotinotes)
![release](https://img.shields.io/github/v/release/archi-y/spotinotes)
![commit](https://img.shields.io/github/last-commit/archi-y/spotinotes)
![stars](https://img.shields.io/github/stars/archi-y/archi-y/spotinotes)


# Table of Contents
- How to install 
- Usage
- It's not working 😭

## How to install

### Requirements

First, you will need to have [Python 3](https://www.python.org/) installed, a free spotify account, and an instagram account.

Then go to https://developer.spotify.com/ and login with your spotify account.
Enter the dashboard using the menu in the right top corner.

You will get to this screen : 
![Pasted image 20230505204420](https://user-images.githubusercontent.com/26002863/236556393-b530c66e-ba41-4dd8-bd4c-b69961f154c4.png)

Press the blue button **"Create App"**

Fill the blanks with the following (feel free to change it but you need to do it in the code as well) : 
- App Name : **Instagram**
- App Description : **Instagram for Spotify**
- Website : **None**
- Redirect URL : http://localhost/

![Pasted image 20230505204526](https://user-images.githubusercontent.com/26002863/236556437-de49ddd2-b870-4c3d-9630-5749b5c97f29.png)
You will then land on this page :
![Pasted image 20230505213116](https://user-images.githubusercontent.com/26002863/236556468-14249dba-5213-4d5d-bdc7-a9709afd5b72.png)
Create a .env file with this content (Don't forget to replace ClientID and ClientSecret by what you get on the dashboard)

	CLIENT_ID="ClientID"
	CLIENT_SECRET="ClientSecret"

# Installation 

Install requirements with these 3 commands :

	python3 -m venv venv
	. venv/bin/activate
	pip3 install -r requirements.txt

Connect your instagram account by launching login.py

	python3 login.py

# Usage

Simply start the program with :

	python3 spotinotes.py

# It's not working 😭

Please make sure that :
- You have requirements installed with python3 etc
- Your instagram account is not disconnected

# Legal

This project is not associated with Spotify or Instagram
