from colorama import Fore

from mathboss.settings import Settings
from mathboss.exercise import Exercise

def show_main_menu(settings: Settings) -> None:
    game_mode = get_game_mode()

    if game_mode == 'start-game': start_game(settings)
    elif game_mode == 'show-settings':
        show_settings(settings)
        show_main_menu(settings)
    elif game_mode == 'set-operators':
        set_operators(settings)
        show_main_menu(settings)
    elif game_mode == 'set-max-result':
        set_max_result(settings)
        show_main_menu(settings)
    else: assert False, f'Game mode "{game_mode}" currently not supported'

def get_game_mode() -> str:
    while True:
        try:
            answer = input('[0]: Spiel starten\n[1]: Einstellungen zeigen\n[2]: Operatoren ändern\n[3]: Höchstes Ergebnis ändern\nWelche Option möchtest du? ')

            if answer in ('beenden', 'stop'): exit(0)

            answer = int(answer)
            if answer < 0 or answer > 3: raise ValueError

            if answer == 0: return 'start-game'
            if answer == 1: return 'show-settings'
            if answer == 2: return 'set-operators'
            if answer == 3: return 'set-max-result'

            raise ValueError

        except ValueError:
            print(Fore.YELLOW + 'Das war keine gültige Zahl von 0 bis 3' + Fore.RESET)


def start_game(settings: Settings) -> None:
    while True:
        exercise = Exercise(settings.max_result, settings.operators)

        answer = input(str(exercise)).lower()

        if answer in ('beenden', 'stop'): break

        player_result = None
        
        try:
            player_result = int(answer)
        except ValueError:
            print(Fore.YELLOW + 'Das ist keine ganze Zahl' + Fore.RESET)
            continue

        if player_result == exercise.result:
            print(Fore.GREEN + 'Deine Antwort ist korrekt!' + Fore.RESET)
        else:
            print(Fore.RED + f'Deine Antwort ist nicht korrekt. Die richtige Antwort war {exercise.result}' + Fore.RESET)


def show_settings(settings: Settings) -> None:
    print(f'Operatoren:\t\t{settings.operators}\nHöchstes Ergebnis:\t{settings.max_result}', end='\n\n')

    input('Drücke die "Enter"-Taste, um zurückzukehren.')


def set_operators(settings: Settings) -> None:
    settings.operators = input('Schreibe hier die Operatoren hin, die du verwenden möchtest: ').strip()
    settings.save()

    input('Drücke die "Enter"-Taste, um zurückzukehren.')


def set_max_result(settings: Settings) -> None:
    while True:
        try:
            new_max_result = int(input('Was soll das höchstmögliche Ergebnis sein? '))
            if new_max_result < 0: raise ValueError
            settings.max_result = new_max_result
            settings.save()
            break
        except ValueError:
            print('Das war kein gültiges Ergebnis.')

    input('Drücke die "Enter"-Taste, um zurückzukehren.')