def greet(bot_name: str, birth_year: str) -> None:
    """Greets with the bot's name and birth year."""
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name() -> None:
    """Asks for user's name and compliments it."""
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age() -> None:
    """Guesses user's age based on remainders."""
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5, and 7.')
    rem3 = int(input("Remainder when dividing by three: "))
    rem5 = int(input("Remainder when dividing by five: "))
    rem7 = int(input("Remainder when dividing by seven: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count() -> None:
    """Counts up to a number provided by the user."""
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    for curr in range(num + 1):
        print(f'{curr}!')


def test() -> None:
    """Tests user's programming knowledge."""
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while (answer := input()) != "2":
        print("Please, try again.")
    end()


def end() -> None:
    """Ends the conversation."""
    print('Congratulations, have a nice day!')


def main() -> None:
    """Main function to run all the tasks."""
    greet('Malvi', '2024')
    remind_name()
    guess_age()
    count()
    test()


if __name__ == "__main__":
    main()