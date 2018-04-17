from actors import Creature, Wizard, Dragon
import random

def main():
    print_header()
    #create_hero()
    game_loop()

def create_hero():
    name = input("Enter Hero's Name: ")
    level = random.randint(50,90)
    hero = Wizard(name, level, health=level)
    print('A level {} Wizard named {} appears!'.format(hero.level, hero.name))
    return hero

def print_header():
    print('---------------------------------')
    print('          OFF-BRAND DND GAME')
    print('---------------------------------')
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5, 5),
        Creature('Bat', 5, 5),
        Creature('Toad', 1, 1),
        Creature('Toad', 1, 1),
        Creature('Tiger', 12, 12),
        Creature('Tiger', 12, 12),
        Dragon('Black Dragon', 50, 50, scaliness=2, breaths_fire=False),
        Dragon('Red Dragon', 50, 50, scaliness=1, breaths_fire=True),
        Wizard('Evil wizard', 150, 150),
    ]

    hero = create_hero()

    while True:

        active_creature = random.choice(creatures)

        print('A {} of level {} appears from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                hero.level_up()
                hero.update_experience(active_creature)
                print("The wizard {} defeated {}".format(hero.name, active_creature.name))
            else:
                print("The wizard {} has been hurt by the powerful {}".format(hero.name, active_creature.name))
                if hero.health <= 0:
                    print("The hero {} has perished!".format(hero.name))
                    cmd = input('Do you wish to play again: [y]es or [no]?')
                    if cmd == 'y':
                        main()
                    else:
                        break
        elif cmd == 'r':
            print('The wizard {} has become unsure of his power and flees!!!'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(" * {} of level {}".format(
                    c.name, c.level
                ))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
