#RIVZOR quote (https://lolz.guru/members/3043646/):
# The part with the creation of the code is borrowed from the user SerdarAD
# I just tweaked this so that I don't have to constantly restart
# And made a convenient entry to the file, if necessary, you can change everything, unless, of course, the hands are from the right place.

# The code is the simplest, as for me.
# Successful use.

#I modified the modified rivzor script
# Removed everything that is not needed, made it possible to use under Linux
import random
import httpx
import os
import time

# Removed external dependency - using built-in key generation
gkeys = []
os.system('cls' if os.name == "nt" else 'clear')
# The most important line of code, nothing will work without it!
print("\n█░█░█ ▄▀█ █▀█ █▀█ ▄█▄\n▀▄▀▄▀ █▀█ █▀▄ █▀▀ ░▀░\n")
print(
    'CREEPER (https://lolz.guru/creeper/) AND RIVZOR (https://lolz.guru/members/3043646/)'
)
# Window Title
print()

# Getting a value for a loop
value_int = int(
    input(
        "Welcome to the WARP+ key generator\nEnter the desired number of keys: "
    ))
a = 0
# The most common cycle while
while a < value_int:
    a += 1
    print(
        "<======================================WARP+ Generate=============================================>"
    )
    print("key number:", a)

    try:
        # Header with variables
        headers = {
            "CF-Client-Version": "a-6.11-2223",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }

        with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                          headers=headers,
                          timeout=30.0) as client:

            r = client.post("/reg")
            id = r.json()["id"]
            license = r.json()["account"]["license"]
            token = r.json()["token"]

            r = client.post("/reg")
            id2 = r.json()["id"]
            token2 = r.json()["token"]

            headers_get = {"Authorization": f"Bearer {token}"}
            headers_get2 = {"Authorization": f"Bearer {token2}"}
            headers_post = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}",
            }

            json = {"referrer": f"{id2}"}
            client.patch(f"/reg/{id}", headers=headers_post, json=json)

            client.delete(f"/reg/{id2}", headers=headers_get2)

            json = {"license": f"{license}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            r = client.get(f"/reg/{id}/account", headers=headers_get)
            account_type = r.json()["account_type"]
            referral_count = r.json()["referral_count"]
            license = r.json()["license"]

            client.delete(f"/reg/{id}", headers=headers_get)
            gkeys.append(license)
            print(
                f"License Key:{license}\nData:{referral_count}gb\nType:{account_type}"
            )

    # Error
    except:
        print("Error.")
        time.sleep(15)
    if a % 2 == 0:
        time.sleep(60)

os.system('cls' if os.name == 'nt' else 'clear')
for x in gkeys:
    print(x)
print('Output a list? separated by commas,Options [y\\n]')
a = input()
if a == "y":
    for z in range(10):
        print()
    for z in gkeys:
        print(f"\"{z}\",")

input('\nPress Enter to exit\n')
