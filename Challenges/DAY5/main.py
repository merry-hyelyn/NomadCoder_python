import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"


def check():
    while True:
        answer = input("#: ")
        if answer.isdigit():
            answer = int(answer)
            try:
                print_countries[answer]
                return answer

            except:
                print("Choose a number of list.")

        else:
            print("That wasn't a number")


print("Hello Please choose select a counrtry by number")
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
table = soup.find("table")
tbody = table.find("tbody")
trs = tbody.find_all("tr")

print_countries = []
countries = []
for tr in trs:
    countries.append(tr.find_all("td"))

for country in countries:
    if country[2].string != None:
        print_countries.append(country)

for index, value in enumerate(print_countries):
    print(f"#{index} {value[0].string.capitalize()}")

answer = check()
result = print_countries[answer]

print(f"You choose {result[0].string.capitalize()}")
print(f"The currency code is {result[2].string}")


os.system("clear")


url = "https://www.iban.com/currency-codes"


countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name': name.capitalize(),
                'code': code
            }
            countries.append(country)


def ask():
    try:
        choice = int(input("#: "))
        if choice > len(countries):
            print("Choose a number from the list.")
            ask()
        else:
            country = countries[choice]
            print(
                f"You chose {country['name']}\nThe currency code is {country['code']}")
    except ValueError:
        print("That wasn't a number.")
        ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")

ask()
