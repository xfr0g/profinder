#======================================#
#                                      #
#                                      #
#    Author is not responsible for     #
#       any misuse of the tool.        #
#                                      #
#                                      #
#======================================#

# Type: OSINT
# Author: Semiii
# Contact: r3moved777@protonmail.com 
# Github: github.com/semiiixyz
# Language/s: Python3
# Note: This project is depracated and is no longer considered efficient. Consider using BROSINT: Best of Philippines.

# Install all required modules
import requests, time, sys
from termcolor import cprint
from bs4 import BeautifulSoup

# Interface
def banner():
    cprint('                        _____ .__             .___               ', 'green')
    cprint('______ _______   ____ _/ ____\|__|  ____    __| _/ ____ ________  ', 'green')
    cprint('\____ \ \_  __ \ /  _ \ \   __\ |  | /    \  / __ |_/ __ \ \___\ ', 'green')
    cprint('|  |_> >|  | \/(  <_> )|  |   |  ||   |  \/ /_/ |\  ___/ |  | \/ ', 'green')
    cprint('|   __/ |__|    \____/ |__|   |__||___|  /\____ | \___  >|__|    ', 'green')
    cprint('|__|                                   \/      \/     \/         ', 'green')
    cprint('[*]===========================================================[*]', 'red', attrs=['bold'])
    cprint('[#]             Profile Finder | Username Generator           [#]', 'red', attrs=['bold'])
    cprint('[#]                       based on inputs                     [#]', 'red', attrs=['bold'])
    cprint('[#]                     Coded by: Semiiixyz                   [#]', 'red', attrs=['bold'])
    cprint('[*]===========================================================[*]', 'red', attrs=['bold'])
banner()
print('')

# Username generator (based on inputs)
def generate_usernames(first_name, last_name, birth_year):
    # Generate username variations
    usernames = [
        first_name + last_name,
        first_name + str(birth_year)[-2:],
        last_name + first_name,
        last_name + str(birth_year)[-2:],
        first_name[0] + last_name,
        first_name + last_name[0],
        first_name[0] + last_name[0],
        first_name + "_" + last_name,
        last_name + "_" + first_name,
        first_name + str(birth_year)[-2:],
        last_name + str(birth_year)[-2:],
        first_name[0] + last_name + str(birth_year)[-2:],
        last_name + first_name + str(birth_year)[-2:],
        first_name + str(birth_year) + last_name
    ]

    return usernames

# Request sender
def check_social_media(username, platform_url):
    # Construct the URL for the social media platform
    url = f"{platform_url}/{username}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response status code indicates success (e.g., 200 OK)
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for specific elements indicating the existence of a profile
        profile_indicator = soup.find('meta', attrs={'name': 'description', 'content': platform_url})

        if profile_indicator:
            print(f"[+] Profile found for {username} on {platform_url}")
        else:
            print(f"[-] No profile found for {username} on {platform_url}")
    else:
        print(f"[x] Failed to fetch data for {username} on {platform_url}")

# Example usage
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
birth_year = int(input("Enter birth year: "))  # Assuming birth year is entered as a year

# Call the function to generate usernames
usernames = generate_usernames(first_name, last_name, birth_year)

# Specify the file name
file_name = "usernames.txt"

# Save the generated usernames to a text file
with open(file_name, "w") as file:
    for username in usernames:
        file.write(username + "\n")

print(f"Usernames saved to {file_name}")

# Social media platforms to check
platforms = {
    "Instagram": "https://www.instagram.com",
    "Twitter": "https://twitter.com",
    "Facebook": "https://www.facebook.com",
    "Reddit": "https://www.reddit.com/user",
    "Github": "https://github.com",
    "LinkedIn": "https://linkedin.com/in",
    "Telegram": "https://t.me/",
    "TikTok": "https://tiktok.com/",
    "Pinterest": "https://pinterest.com",
    "Snapchat": "https://snapchat.com/add"
    # Add more social media platforms as needed
}

# Check profiles on social media platforms
for username in usernames:
    print(f"\nChecking profiles for {username} on different platforms:")
    for platform, url in platforms.items():
        check_social_media(username, url)
        time.sleep(3)

print('')
print('Finished. Exiting now')
sys.exit