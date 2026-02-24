import random
import time

class Market:
    def __init__(self):
        # Resource prices in Credits
        self.prices = {"Food": 15, "Fuel": 25, "Gold": 250, "Minerals": 120, "Med-Supplies": 50}
        self.token_value = 60

    def get_fluctuated_price(self, item):
        # Simulates changing market prices
        return round(self.prices[item] * random.uniform(0.85, 1.3), 2)

class Starship:
    MIN_FOOD = 5
    MIN_FUEL = 10

    def __init__(self, name):
        self.name = name
        self.inventory = {"Food": 20, "Fuel": 40, "Gold": 0, "Minerals": 0, "Med-Supplies": 2}
        self.credits = 1000.0
        self.tokens = 10
        self.is_active = True

    def check_status(self):
        # Automatic termination logic
        if self.inventory["Food"] < self.MIN_FOOD or self.inventory["Fuel"] < self.MIN_FUEL:
            print("SYSTEM FAILURE: Necessities below operational threshold!")
            self.is_active = False

    def spend(self, amount, currency="Credits"):
        if currency == "Credits":
            if self.credits >= amount:
                self.credits -= amount
                return True
        elif currency == "Tokens":
            if self.tokens >= amount:
                self.tokens -= amount
                return True
        print("X Transaction Failed: Insufficient Funds")
        return False

    # --- BUY FOOD ---
    def buy_food(self, market):
        price = market.get_fluctuated_price("Food")
        print(f"\nFood Market: {price} Credits/unit")
        qty = int(input("Amount to buy: "))
        if self.spend(price * qty):
            self.inventory["Food"] += qty
            print(f"Loaded {qty} units of Food.")

    # --- BUY FUEL ---
    def buy_fuel(self, market):
        price = market.get_fluctuated_price("Fuel")
        print(f"\nFuel Depot: {price} Credits/unit")
        qty = int(input("Liters to buy: "))
        if self.spend(price * qty):
            self.inventory["Fuel"] += qty
            print(f"Refueled with {qty} L.")

    # --- BUY MEDICAL SUPPLIES ---
    def buy_med_supplies(self, market):
        price = market.get_fluctuated_price("Med-Supplies")
        print(f"\nMedical Bay: {price} Credits/unit")
        qty = int(input("Kits to buy: "))
        if self.spend(price * qty):
            self.inventory["Med-Supplies"] += qty
            print(f"Stocked {qty} Medical Kits.")

    # --- TRADE MINERALS FOR TOKENS ---
    def trade_minerals(self, market):
        print(f"\nMineral Exchange: 1 Mineral = 2 Tokens")
        if self.inventory["Minerals"] > 0:
            qty = int(input(f"Amount to trade (Max {self.inventory['Minerals']}): "))
            if qty <= self.inventory["Minerals"]:
                self.inventory["Minerals"] -= qty
                self.tokens += (qty * 2)
                print(f"Traded {qty} Minerals for {qty * 2} Tokens.")
        else:
            print("X No Minerals in cargo.")

    # --- BUYING GOLD WITH TOKENS ---
    def buy_gold_with_tokens(self):
        cost = 4
        if self.spend(cost, "Tokens"):
            self.inventory["Gold"] += 1
            print(f"Gold acquired for {cost} Tokens.")

    # --- MINING EXPEDITION ---
    def mining_expedition(self):
        self.inventory["Food"] -= 4
        self.inventory["Fuel"] -= 8
        found_m = random.randint(1, 3)
        self.inventory["Minerals"] += found_m
        print(f"Mining successful! Found {found_m} Minerals.")
        self.check_status()

    def display_ui(self):
        print(f"\n\033[1mSHIP: {self.name}\033[0m")
        print(f"Credits: {self.credits:.2f} | Tokens: {self.tokens}")
        print(f"Cargo: {self.inventory}")
        print(f"MIN REQUIRED: Food > {self.MIN_FOOD}, Fuel > {self.MIN_FUEL}")
        print("-" * 45)

# Main Application Logic
market = Market()
ship = Starship("GQT-EXCELSIOR")

while ship.is_active:
    ship.display_ui()
    print("1. Buy Food (Credits)     2. Buy Fuel (Credits)")
    print("3. Trade Minerals->Tokens 4. Buy Gold (Tokens)")
    print("5. Mining Expedition      6. Buy Medical Supplies (Credits)")
    print("7. Exit")
    
    choice = input("\nSelect Command: ")
    
    if choice == "1": ship.buy_food(market)
    elif choice == "2": ship.buy_fuel(market)
    elif choice == "3": ship.trade_minerals(market)
    elif choice == "4": ship.buy_gold_with_tokens()
    elif choice == "5": ship.mining_expedition()
    elif choice == "6": ship.buy_med_supplies(market)
    elif choice == "7": break

print("GAME OVER: Mission Terminated.")
