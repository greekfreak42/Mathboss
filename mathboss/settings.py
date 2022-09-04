import json

class Settings:
    filename = 'settigns.json'

    def __init__(self) -> None:

        with open(Settings.filename, 'r') as settings_file: settings = json.load(settings_file)

        self.operators = settings['operators']
        self.max_result = settings['max-result']


    def save(self) -> None:
        with open(Settings.filename, 'w') as settings_file: json.dump({'operators' : self.operators, 'max-result' : self.max_result}, settings_file)