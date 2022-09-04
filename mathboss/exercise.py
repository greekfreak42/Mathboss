from random import choice, randint

class Exercise:
    def __init__(self, max_result: int, possible_operators: str) -> None:
        operator = choice(possible_operators)
        if operator != '+': raise NotImplementedError(f'Der Operator \'{operator}\' wird noch nicht unterstützt')

        a = randint(0, max_result)
        b = randint(0, max_result - a)

        self.string = f'{a} + {b} = '
        self.result = a + b
    
    def __str__(self) -> str: return self.string