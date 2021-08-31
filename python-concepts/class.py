class TColors:
    WARNING = '\033[93m'
    CYAN = '\033[96m'
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    DEFAULT = '\033[0m'


class Person:
    name: str
    middle_name: str
    age: int
    nationality: str

    def __init__(self, name, middle_name, age, nationality):
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.nationality = nationality

    def greets(self):
        print(f"\nHi {TColors.CYAN}{self.name}!" + f" {TColors.DEFAULT}It's a pleasure to meet you :D \n")
        print(
            f"This is what I got from you: "
            f"\n   {TColors.DEFAULT}Name: {TColors.BLUE}{self.name} "
            f"\n   {TColors.DEFAULT}Middle Name: {TColors.BLUE}{self.middle_name} "
            f"\n   {TColors.DEFAULT}Age: {TColors.BLUE}{self.age} "
            f"\n   {TColors.DEFAULT}Nationality: {TColors.BLUE}{self.nationality}")


class Astronaut(Person):
    would_be_astronaut = False

    @staticmethod
    def inspire():
        print(f"\nHere's some inspiration: {TColors.CYAN}\nNeil deGrasse Tyson - 'When I look up at the night sky "
              f"and I know that yes, we are part of this universe, we are in this universe, \nbut perhaps more "
              f"important than both of those facts is that the universe is in us.'")


def init():
    try:
        name = input("Type your first name: ").capitalize()
        middle_name = input("Type your middle name: ").capitalize()
        age = int(input("Type your age: "))
        nationality = input("Type your nationality: ").capitalize()

        yes = {"yes", "y", "Yes", "YES"}
        no = {"no", "n", "No", "NO"}

        answer = input(f"\n{TColors.DEFAULT}Just for fun: have you ever dreamed of "
                       f"being an Astronaut? [yes/no] ")

        if answer in yes:
            new_person = Astronaut(name=name, middle_name=middle_name, age=age, nationality=nationality)
            new_person.would_be_astronaut = True
            new_person.inspire()

        else:
            new_person = Person(name=name, middle_name=middle_name, age=age, nationality=nationality)
            print('OK! Thanks for answering :D')

        new_person.greets()

    except Exception as error:
        print(f"{TColors.WARNING}\nOoops, something went wrong :C! Please try again.")
        print(f"{TColors.FAIL}{error}")


init()
