# Made White By Raka Andrian Tara

import random
import time

class SniperGame:
    def __init__(self):
        self.target_position = random.randint(1, 10)
        self.attempts = 0

    def shoot(self, guess):
        self.attempts += 1
        if guess < self.target_position:
            return "Too low!"
        elif guess > self.target_position:
            return "Too high!"
        else:
            return f"Hit! You found the target in {self.attempts} attempts."

    def play(self):
        print("Welcome to the Sniper Game!")
        print("Try to hit the target located between 1 and 10.")
        while True:
            try:
                guess = int(input("Enter your shot (1-10): "))
                if 1 <= guess <= 10:
                    result = self.shoot(guess)
                    print(result)
                    if "Hit!" in result:
                        break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = SniperGame()
    game.play()
