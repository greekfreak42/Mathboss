
class Score:
    def __init__(self, initial_correct=0, initial_incorrect=0) -> None:
        self.correct = initial_correct
        self.incorrect = initial_incorrect
    
    def __repr__(self) -> str:
        result = 'Du hast '

        if self.correct == 0: result += 'keine Aufgabe'
        elif self.correct == 1: result += 'eine Aufgabe'
        else: result += f'{self.correct} Aufgaben'

        result += ' richtig und '

        if self.incorrect == 0: result += 'keine Aufgabe'
        elif self.incorrect == 1: result += 'eine Aufgabe'
        else: result += f'{self.incorrect} Aufgaben'

        result += ' falsch beantwortet.'

        return result