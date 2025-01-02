# -*- coding: utf-8 -*-


#Libraries
import instaloader
from dotenv import load_dotenv
import os



import instaloader
from dotenv import load_dotenv
import os
import time
import random

#%%Input Credentials Securely
# Load credentials from .env file
load_dotenv()

# Specify the path to the .env file in the credentials folder
env_path = os.path.join("credentials", ".env")
load_dotenv(dotenv_path=env_path)

username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

# Initialize Instaloader
loader = instaloader.Instaloader()

try:
    # Load existing session if available
    loader.load_session_from_file(username)
    print("Session loaded successfully!")
except FileNotFoundError:
    # Log in and save session if no session exists
    print("No session file found. Logging in...")
    loader.login(username, password)
    loader.save_session_to_file()
    print("Session saved successfully!")


#%% Fetch Followed Accounts and Data

try:
    # Get profile data
    profile = instaloader.Profile.from_username(loader.context, username)

    # Fetch accounts you follow with delays
    print("\nAccounts you follow:")
    for followed in profile.get_followees()[:10]:  # Limit to first 10 accounts
        print(f"Username: {followed.username}, Full Name: {followed.full_name}, Bio: {followed.biography}")
        time.sleep(random.uniform(3, 8))  # Random delay between 3-8 seconds

    # Save fetched data to a file
    with open("followed_accounts.csv", "w", encoding="utf-8") as file:
        file.write("Username,Full Name,Bio\n")
        for followed in profile.get_followees()[:10]:  # Match the fetch limit
            file.write(f'"{followed.username}","{followed.full_name}","{followed.biography}"\n')
    print("Data saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
