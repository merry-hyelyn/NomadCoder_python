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
