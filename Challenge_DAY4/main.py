import requests
import os


def check_url(url):
    try:
        requests.get(url).status_code
        return True

    except:
        return False


def restart():
    while True:
        answer = input("Do you want to start over y/n?")
        if answer == "y":
            return True

        elif answer == "n":
            return False

        else:
            print("That's not a valid answer")


while True:
    print("Welcome to IsItDown.py!")
    urls = input(
        "please write a URL or URLs you want to check. (seperate by comma)\n")

    urls = urls.split(",")

    for url in urls:
        url = url.strip()

        if "http://" not in url:
            url = f"http://{url}"

        url = url.lower()

        if check_url(url):
            print(f"{url} is up!")

        else:
            print(f"{url} is down!")

    if restart():
        os.system('clear')

    else:
        print("ok bye")
        break
