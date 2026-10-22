"""
Week 1: Python Basics - Personal Introduction Program
File: personal_intro.py
Description: An interactive CLI program that asks for the user's name, age,
             hobby, city, and favorite food, then displays a friendly
             welcome message and bio-data summary card.
"""


def main():
    # Day 1: Setup & First Program - Greeting Header
    print("=" * 55)
    print("👋 Hello, World! Welcome to the Personal Intro Program")
    print("=" * 55)
    print("Please answer a few quick questions to build your profile:\n")

    # Day 2 & Day 4: Add User Input & Enhance Program (5 Questions)
    # Using input() to collect answers and variables to store them
    name = input("What is your name? ").strip()
    age = input("How old are you? ").strip()
    hobby = input("What is your favorite hobby? ").strip()
    city = input("Which city do you live in? ").strip()
    favorite_food = input("What is your favorite food? ").strip()

    # Fallback defaults if the user presses Enter without typing
    name = name if name else "Friend"
    age = age if age else "N/A"
    hobby = hobby if hobby else "exploring Python"
    city = city if city else "your city"
    favorite_food = favorite_food if favorite_food else "good food"

    # Day 3 & Day 4: Welcome Message & Enhanced Formatting with f-strings
    print(f"\n🎉 Welcome {name}! 🎉")
    print(f"You are {age} years old and love {hobby}.")
    print(f"It's awesome that you're tuning in from {city} and enjoy {favorite_food}!")

    # Day 5: Finalize & Test - Summary Bio-Data Card
    print("\n" + "-" * 55)
    print("📋 YOUR PERSONAL BIO-DATA SUMMARY")
    print("-" * 55)
    print(f"  • Name          : {name}")
    print(f"  • Age           : {age} years old")
    print(f"  • Favorite Hobby: {hobby}")
    print(f"  • City          : {city}")
    print(f"  • Favorite Food : {favorite_food}")
    print("-" * 55)
    print("🚀 Happy coding on your Week 1 Python journey!\n")


if __name__ == "__main__":
    main()
