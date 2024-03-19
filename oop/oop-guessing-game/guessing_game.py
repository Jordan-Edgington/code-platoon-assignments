class GuessingGame():
    def __init__(self, answer, last_guess=None):
        self.answer = answer
        self.last_guess = last_guess
        pass

    def guess(self, user_guess):
        if user_guess < self.answer:
            self.last_guess = user_guess
            return "low"
        elif user_guess > self.answer:
            self.last_guess = user_guess
            return "high"
        else:
            self.last_guess = user_guess
            return "correct"

    def solved(self):
        if self.last_guess == self.answer:
            return True
        else:
            return False


game = GuessingGame(20)
print(game.guess(10))
print(game.guess(20))
print(game.guess(30))
print(game.solved())
