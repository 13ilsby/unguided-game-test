class Character:
    def __init__(self, name):
        self.name = name
        self.class_type = ""
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intellect = 0
        self.wisdom = 0
        self.charisma = 0

    def get_modifier(self, stat_value):
        return (stat_value - 10) // 2
    
class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.class_type = "Wizard"
        self.strength = 8
        self.dexterity = 12
        self.constitution = 12
        self.intellect = 16
        self.wisdom = 14
        self.charisma = 8

class Fighter(Character):
    def __init__(self, name):
        super().__init__(name)
        self.class_type = "Fighter"
        self.strength = 16
        self.dexterity = 12
        self.constitution = 14
        self.intellect = 8
        self.wisdom = 8
        self.charisma = 12

def main():
    print("Welcome to Text RPG!")
    char_name = input("Enter your character's name: ")

    valid_classes = {
        "Wizard": Wizard,
        "Fighter": Fighter
    }

    char_class = input(f"Choose your character's class - {', '.join(valid_classes.keys())}: ").capitalize()
    while char_class not in valid_classes:
        char_class = input(f"Invalid class. Choose a class from the following - {', '.join(valid_classes.keys())}: ").capitalize()

    player = valid_classes[char_class](char_name)

    print(f"Character created: {player.name} the {player.class_type}")
    print(f"Strength: {player.strength}, Dexterity: {player.dexterity}, Constitution: {player.constitution}, Intellect: {player.intellect}, Wisdom: {player.wisdom}, Charisma: {player.charisma}")

main()