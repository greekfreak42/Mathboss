from random import choice, randint

class Exercise:
    def __init__(self, max_result: int, max_number: int, possible_operators: str) -> None:
        operator = choice(possible_operators)
        if operator not in '+-': raise NotImplementedError(f'Der Operator \'{operator}\' wird noch nicht unterstützt')

        if operator == '+':
            a = randint(0, min(max_number, max_result))
            b = randint(0, min(max_number, max_result) - a)
            self.string = f'{a} + {b} = '
            self.result = a + b
        elif operator == '-':
            a = randint(0, max_number)
            if a <= max_result:
                b = randint(0, a)
            else:
                b = randint(a - max_result, a)
            
            self.string = f'{a} - {b} = ' if b >= 0 else f'{a} - ({b}) = '
            self.result = a - b
        else: assert False
    
    def __str__(self) -> str: return self.string

    def __repr__(self) -> str: return self.string