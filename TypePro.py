import random
import time

class SpeedTypingGame:
    def __init__(self):
        self.words = ["python", "coding", "challenge", "programming", "speed", "typing", "game", "developer", "keyboard", "application", "forever", "simple", "Movie", "routine", "horoscopes", "conspiracy", "cookies", "couch", "biology", "butterfly", "System"]
        self.rounds = 3
        self.difficulty_levels = {"easy": 5, "medium": 3, "hard": 2}

        self.score = 0

    def get_random_word(self):
        return random.choice(self.words)

    def display_intro(self):
        print("Welcome to the Advanced Speed Typing Game!")
        input("Press Enter to start...")

    def get_user_input(self):
        return input("Your input: ")

    def play_round(self, word, difficulty):
        print(f"\nType the word: {word}")

        start_time = time.time()
        user_input = self.get_user_input()
        end_time = time.time()
        elapsed_time = end_time - start_time

        if user_input.lower() == word:
            score_increment = max(0, difficulty - elapsed_time)
            self.score += score_increment
            print(f"Correct! Time taken: {elapsed_time:.2f} seconds. Score: {self.score}")
        else:
            print("Sorry, you made a mistake. No points awarded for this round.")

    def play_game(self):
        self.display_intro()

        for round_num in range(1, self.rounds + 1):
            print(f"\nRound {round_num}/{self.rounds}")
            difficulty = self.get_difficulty()
            word_to_type = self.get_random_word()
            self.play_round(word_to_type, difficulty)

        print(f"\nGame Over! Your final score is: {self.score}")

    def get_difficulty(self):
        print("\nSelect difficulty level:")
        for i, level in enumerate(self.difficulty_levels.keys(), 1):
            print(f"{i}. {level}")

        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                difficulty = list(self.difficulty_levels.values())[choice - 1]
                break
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")

        return difficulty

if __name__ == "__main__":
    game = SpeedTypingGame()
    game.play_game()
    
