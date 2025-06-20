import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("FREECURRENCY_API_KEY")
BASE_URL =f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD","CAD","EUR","AUD","INR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
    
def display_menu():
    print("""
        M to see the menu of the commands again
        Q to Quit the program
        A to seee all currencies in our options
        """)

print("Welcome to the currency converter")
display_menu()
while True:
    b = input("Enter a base currency:").upper()
    if b == "Q":
        break
    elif b == "M":
        display_menu()
        continue
    elif b not in CURRENCIES:
        print("That's an invalid currency, try again")
        continue
    else:
        while True:
            target = input("Enter a target currency : ").upper()
            if target in CURRENCIES:
                break
            elif target == "A":
                break
            else:
                continue
        money = None
        while not isinstance(money,(int,float)):
            try:
                i = input("Enter an amount : ")
                money = float(i)
            except ValueError:
                print("Invalid input. Please enter a valid number")
            except Exception as e:
                print(f"An unexpected error occured: {e}")
        data = convert_currency(b.upper())
        if target == "A":
            for k,v in data.items():
                 print(f"{k} : {round(v*money,2)}")
        else:
            print(f"{target.upper()} : {round(data[target.upper()]*money,2)}")
