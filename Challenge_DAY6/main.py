import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

os.system("clear")
url = "https://www.iban.com/currency-codes"


def choose_country():
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


def money_input(a_country, b_country):
    print(f"\nHow many {a_country} do you want to convert to {b_country}?")
    answer = input()
    if answer.isdigit():
        return int(answer)
    else:
        print("That wasn't number.")
        return money_input(a_country, b_country)


def change_currency(a_country, b_country, amount):
    base_url = "https://transferwise.com"
    add_url = f"/gb/currency-converter/{a_country}-to-{b_country}-rate?amount={amount}"

    fix_url = base_url + add_url
    result = requests.get(fix_url)
    soup = BeautifulSoup(result.text, "html.parser")
    currency = float(soup.find("span", {"class": "text-success"}).string)
    return amount * currency


print("Welcome to CurrencyConvert PRO 2000\n")
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

print("\nWhere are you from? Choose a country by number.\n")
one = choose_country()
a_country = print_countries[one]
print(a_country[0].string.capitalize())
print("\nNow choose another country\n")
two = choose_country()
b_country = print_countries[two]
print(b_country[0].string.capitalize())

amount = money_input(a_country[2].string, b_country[2].string)
convert_to = change_currency(a_country[2].string, b_country[2].string, amount)

a_country_amount = format_currency(amount, a_country[2].string, locale="ko_KR")
b_country_amount = format_currency(
    convert_to, b_country[2].string, locale="ko_KR")
print(f"{a_country_amount} is {b_country_amount}")
