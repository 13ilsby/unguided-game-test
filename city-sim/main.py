import os
import random

class Settlement:
    def __init__(self, name):
        self.name = name

        self.resources = {
            "Food": 300,
            "Wood": 100,
            "Stone": 50,
            "Gold": 0
        }
        
        self.buildings = {
            "House": 3
        }
       
        self.population = 30
        self.population_limit = 15 + 10*self.buildings["House"]
        self.growth_rate = 0.2
        self.months_elapsed = 0
        self.year = 0
        self.seasons = ["Spring", "Summer", "Autumn", "Winter"]
        self.current_season_index = 0
        self.current_season = self.seasons[self.current_season_index]
        

    def use_resources(self, cost):
        for resource, amount in cost.items():
            if self.resources[resource] < amount:
                set_text(f"Not enough {resource}!")
                return False
         
        for resource, amount in cost.items():
                self.resources[resource] -= amount
        return True

    def construct_building(self, building_class):
        building = building_class()
        if self.use_resources(building.cost):
            if building.name in self.buildings:
                self.buildings[building.name] += 1
            
            else:
                self.buildings[building.name] = 1
            set_text("House constructed!")

    def population_growth(self):   
        population = self.population
        growth_rate = self.growth_rate
        population_limit = self.population_limit
        change = growth_rate * population * (1 - population / population_limit)
        return int(population + change)

    def end_turn(self):
        self.resources['Food'] -= (self.population*2)
        self.resources['Wood'] -= (self.population)
        self.population = self.population_growth()
        self.months_elapsed += 3

        if self.months_elapsed % 12 == 0:
            self.year += 1

        self.current_season_index = (self.months_elapsed % 12) // 3

        self.current_season = self.seasons[self.current_season_index]

class Building:
     def __init__(self, name, description, cost):
          self.name = name
          self.description = description
          self.cost = cost

class House(Building):
     def __init__(self):
          super().__init__("House", "Increases population limit by 10.", {"Wood": 50, "Stone": 50})

#|--------------------------------|UI AND MENU|--------------------------------|#

class Menu:
    def __init__(self, options):
        self.options = options

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self, lines):
        self.clear_console()
        print(".~._______.~ Welcome to Realmscape! ~._______.~.")
        print("||============================================||")
        for line in lines:
            print(f"||{line.ljust(44)}||")
        print("||============================================||")
        print(f"|| {show_text.ljust(43)}||")
        print(f"||============================================||")
        for option in self.options:
            print(f"|[{option.ljust(44)}||")
        print("||============================================||")
        print()
        set_text("")


main_menu = Menu(
    ["1. View settlement", "2. Construct building", "3. End turn", "4. Quit"]
)

view_menu = Menu(
    ["1. Back"]
)

construct_menu = Menu(
    ["1. House", "2. Back"]
)

end_menu = Menu(
    ["1. Back"]
)

show_text = ""

def set_text(new_text):
    global show_text
    show_text = str(new_text)

def main():
    player = Settlement("Realmscape")
    current_menu = main_menu

    while True:

        if current_menu == main_menu:
            lines = [
                f"Year {player.year}, {player.current_season}",
                f"Population: {player.population}",  
                f"",
                f"",
                f"",
                f"Food: {player.resources['Food']}, Wood: {player.resources['Wood']}, Stone: {player.resources['Stone']}, Gold: {player.resources['Gold']}"
            ]

        elif current_menu == view_menu:
            lines = [
                "",
                "",
                "",
                "",
                "",
                ""
            ]
            
        elif current_menu == construct_menu:
            lines = [
                "",
                "",
                "",
                "",
                "",
                "Choose a building to construct:"
            ]

        elif current_menu == end_menu:
            lines = [
                "",
                "",
                "",
                "",
                "",
                ""
            ]
        
        current_menu.display_menu(lines)
        choice = input("Enter choice: ")
        
        if current_menu == main_menu:
            if choice == "1":
                current_menu = view_menu
            elif choice == "2":
                current_menu = construct_menu
            elif choice == "3":
                current_menu = end_menu
            elif choice == "4":
                print(f"Abandoning {player.name}...")
                break

        elif current_menu == view_menu:
            if choice == "1":
                current_menu = main_menu

        elif current_menu == construct_menu:
            if choice == "1":
                player.construct_building(House)
            elif choice == "2":
                current_menu = main_menu

        elif current_menu == end_menu:
            if choice == "1":
                player.end_turn()
                current_menu = main_menu
main()
               
               
                 