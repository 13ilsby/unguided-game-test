class Settlement:
    def __init__(self, name):
        self.name = name
        self.population = 30

        self.buildings = [
            Building("House", "Increases population cap.", 1),
            Building("Stockpile", "Stores up to 1000 raw resources.", 1),
            Building("Granary", "Stores up to 1000 food.", 2)
        ]

        self.resources = {
            "Wood": Resource("Wood", 100),
            "Stone": Resource("Stone", 50),
            "Food": Resource("Food", 500)
        }

        self.jobs = {
            "Lumberjack": 5,
            "Stoneminer": 5,
        }

        self.months_elapsed = 0

    def end_turn(self):
        self.months_elapsed += 1

        for building in self.buildings:
            if not building.constructed:
                building.construct()

        self.resources["Wood"].gather(self.jobs["Lumberjack"] * 10)
        self.resources["Stone"].gather(self.jobs["Stoneminer"] * 5)

        self.print_status()

    def print_status(self):

        print(f"Month: {self.months_elapsed}")
        print(f"Settlement: {self.name}")
        print(f"Population: {self.population}")

        for building in self.buildings:
            status = "Constructed" if building.constructed else f"Building ({building.construct_time} months left)"
            print(f"- {building.name}: {status}")

        for resource in self.resources.values():
            print(f"- {resource.name}: {resource.quantity}")

        print("\n")

class Building:
    def __init__(self, name, description, construct_time, construct_cost):
        self.name = name
        self.description = description
        self.construct_cost = construct_cost
        self.construct_time = construct_time
        self.constructed = False

    def construct(self):
        if self.construct_time > 0:
            self.construct_time -= 1
        else:
            self.constructed = True

class Resource:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def gather(self, amount):
        self.quantity += amount

    def consume(self, amount):
        if self.quantity > amount:
            self.quantity -= amount
        else:
            print("Not enough resources.")

class Job:
    def __init__(self, name):
        self.name = name


def main():
    print("Welcome to Realmscape!")
    settlement_name = input("Enter your settlement's name: ")

    player = Settlement(settlement_name)

    print(f"The settlement of {player.name} has been founded! It has a population of {player.population}.")

    while True:
        action = input("Press 'n' to end turn: ").lower()
        if action == 'n':
            player.end_turn()

main()

#class Settlement:
#    def __init__(self, name):
#        self.name = name

#        self.resources = {
#            "Wood": Resource("Wood", 100),
#            "Stone": Resource("Stone", 50),
#            "Food": Resource("Food", 500)
#        }

#    def consume_resources(self, cost):
#        for resource, amount in cost.items():
#            if self.resources[resource].quantity < amount:
#                raise Exception(f"Insufficient {self.resources[resource]}")

#        for resource, amount in cost.items():
#            self.resources[resource].consume(amount)

#    def construct_building(self, Building):
#        self.consume_resources(Building.cost)

#class Resource:
#    def __init__(self, name, quantity):
#        self.name = name
#        self.quantity = quantity

#    def gather(self, amount):
#        self.quantity += amount

#    def consume(self, amount):
#        if self.quantity >= amount:
#            self.quantity -= amount
#        else:
#            print(f"Insufficient {self.name}.")

#class Building:
#    def __init__(self, name, description, cost):
#        self.name = name
#        self.description = description
#        self.cost = cost

#class House(Building):
#    def __init__(self):
#        super().__init__("House", "Increases population cap by 10.", [Resource("Wood", 50), Resource("Stone", 10)])
        


#def main():
    
#    print("~.________.~ Welcome to Realmscape! ~.________.~")

#    settlement_name = "Draftown"

#    player = Settlement(settlement_name)

#    print(f"The settlement of {player.name} has been founded!")

#    player.construct_building(House)
#    print(player.resources)

#main()