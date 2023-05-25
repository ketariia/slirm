import random

from fairytale import Visitor


class Creature:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def accept(self, visitor):
        visitor.visit(self)

    def get_weapon(self):
        pass


class Dwarf(Creature):
    def get_weapon(self):
        self.weapon = random.choice(["Jargon", "Play"])


class Elf(Creature):
    def get_weapon(self):
        self.weapon = random.choice(["InventFeature", "SellImaginaryProduct"])


class Troll(Creature):
    def get_weapon(self):
        self.weapon = random.choice(["Edict", "Schedule"])


class Weapon:
    def __init__(self, name, wins_against):
        self.name = name
        self.wins_against = wins_against

    def __str__(self):
        return self.name


class WeaponVisitor:
    def __init__(self):
        self.weapons = []

    def visit(self, creature):
        creature.get_weapon()
        weapon = Weapon(creature.weapon, None)
        self.weapons.append(weapon)


class Project:
    def __init__(self):
        self.weapons = {}
        self.employees = []
        self.groups = {}

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_group(self, group_name, group):
        self.groups[group_name] = group

    def interact(self, visitor):
        for employee in self.employees:
            employee.accept(visitor)

    def battle(self, fighter1, fighter2):
        weapon1 = fighter1.weapon
        weapon2 = fighter2.weapon

        if weapon1 == weapon2:
            print(f"{fighter1.name} ({weapon1}) and {fighter2.name} ({weapon2}) tied!")
            return None
        elif self.weapons[weapon1].wins_against == weapon2:
            print(f"{fighter1.name} ({weapon1}) beats {fighter2.name} ({weapon2})!")
            return fighter1
        else:
            print(f"{fighter2.name} ({weapon2}) beats {fighter1.name} ({weapon1})!")
            return fighter2

    def meeting(self, dwarf_count, elf_count, troll_count):
        dwarf_list = [Dwarf(f"Dwarf {i}") for i in range(1, dwarf_count + 1)]
        elf_list = [Elf(f"Elf {i}") for i in range(1, elf_count + 1)]
        troll_list = [Troll(f"Troll {i}") for i in range(1, troll_count + 1)]

        self.add_group("Dwarf", dwarf_list)
        self.add_group("Elf", elf_list)
        self.add_group("Troll", troll_list)

        creatures = dwarf_list + elf_list + troll_list

        while True:
            winners = []
            for creature in creatures:
                if creature in winners:
                    continue
                opponents = [c for c in creatures if c != creature and c not in winners]
                if opponents:
                    random_opponent = random.choice(opponents)
                    winner = self.battle(creature, random_opponent)
                    if winner:
                        winners.append(winner)

            for group_name, group in self.groups.items():
                self.groups[group_name] = [c for c in group if c in winners]

            winner_groups = [group for group in self.groups.values() if len(group) > 0]
            if len(winner_groups) == 1:
                print(f"{winner_groups[0][0].name} from {winner_groups[0][0].__class__.__name__} wins!")
                break

        for weapon in Visitor.weapons:
            if weapon.name not in self.weapons:
                if weapon.name == "Jargon":
                    wins_against = "Edict"
                elif weapon.name == "Play":
                    wins_against = "Schedule"
                elif weapon.name == "InventFeature":
                    wins_against = "Edict"
                elif weapon.name == "SellImaginaryProduct":
                    wins_against = "Schedule"
                elif weapon.name == "Edict":
                    wins_against = "Play"
                elif weapon.name == "Schedule":
                    wins_against = "SellImaginaryProduct"
                weapon.wins_against = wins_against
                self.weapons[weapon.name] = weapon











