import json

class Settings:
    filename = 'settigns.json'

    def __init__(self) -> None:

        with open(Settings.filename, 'r') as settings_file: settings = json.load(settings_file)

        self.operators = settings['operators']
        self.max_result = settings['max-result']
        self.max_number = settings['max-occuring-number']


    def save(self) -> None:
        with open(Settings.filename, 'w') as settings_file:
            json.dump({'operators' : self.operators, 'max-result' : self.max_result, 'max-occuring-number' : self.max_number}, settings_file)
    

    def __repr__(self) -> str:
        return f'Operatoren:\t\t\t{self.operators}\nHöchstes Ergebnis:\t\t{self.max_result}\nHöchste auftretende Zahl:\t{self.max_number}\n'
        