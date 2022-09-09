from colorama import Fore

from mathboss.settings import Settings
from mathboss.exercise import Exercise
from mathboss.score    import Score

def run_main_loop(settings: Settings) -> None:
    while True:
        game_mode = get_game_mode()

        if game_mode == 'start-game': run_game(settings)
        elif game_mode == 'show-settings': show_settings(settings)
        elif game_mode == 'set-operators': set_operators(settings)
        elif game_mode == 'set-max-result': set_max_result(settings)
        elif game_mode == 'set-max-number': set_max_number(settings)
        else: assert False, f'Game mode "{game_mode}" currently not supported'


def get_game_mode() -> str:
    while True:
        try:
            answer = input('[0]: Spiel starten\n[1]: Einstellungen zeigen\n[2]: Operatoren ändern\n[3]: Höchstes Ergebnis ändern\n' \
                + '[4]: Höchste auftretende Zahl ändern\n\nWelche Option möchtest du? ')

            if should_exit(answer): exit(0)

            answer = int(answer)
            if answer < 0 or answer > 4: raise ValueError

            if answer == 0: return 'start-game'
            if answer == 1: return 'show-settings'
            if answer == 2: return 'set-operators'
            if answer == 3: return 'set-max-result'
            if answer == 4: return 'set-max-number'

            raise ValueError

        except ValueError:
            print(Fore.YELLOW + 'Das war keine gültige Zahl von 0 bis 4' + Fore.RESET)


def should_exit(msg: str) -> bool: return msg.strip().lower() in ('beenden', 'stop')


def run_game(settings: Settings) -> None:

    score = Score()

    while True:
        exercise = Exercise(settings.max_result, settings.max_number, settings.operators)

        answer = input(exercise).lower()

        if should_exit(answer):
            print(score)
            exit(0)

        player_result = None
        
        try:
            player_result = int(answer)
        except ValueError:
            print(Fore.YELLOW + 'Das ist keine ganze Zahl' + Fore.RESET)
            continue

        if player_result == exercise.result:
            print(Fore.GREEN + 'Deine Antwort ist korrekt!' + Fore.RESET)
            score.correct += 1
        else:
            print(Fore.RED + f'Deine Antwort ist nicht korrekt. Die richtige Antwort war {exercise.result}' + Fore.RESET)
            score.incorrect += 1


def show_settings(settings: Settings) -> None:
    print(f'\n{settings}')
    input('Drücke die "Enter"-Taste, um zurückzukehren.')


def set_operators(settings: Settings) -> None:
    new_operators = input('Schreibe hier die Operatoren hin, die du verwenden möchtest: ').strip()

    if should_exit(new_operators): return

    settings.operators = new_operators
    settings.save()

    input('Drücke die "Enter"-Taste, um zurückzukehren.')


def set_max_result(settings: Settings) -> None:
    while True:
        try:
            new_max_result = input('Was soll das höchstmögliche Ergebnis sein? ')

            if should_exit(new_max_result): return

            new_max_result = int(new_max_result)
            if new_max_result < 0: raise ValueError

            settings.max_result = new_max_result
            settings.save()
            break
        except ValueError:
            print('Das war kein gültiges Ergebnis.')

    input('Drücke die "Enter"-Taste, um zurückzukehren.')


def set_max_number(settings: Settings) -> None:
    while True:
        try:
            new_max_number = input('Was soll die höchste Zahl sein, die auftreten kann? ')

            if should_exit(new_max_number): return

            new_max_number = int(new_max_number)
            if new_max_number < 0: raise ValueError

            settings.max_number = new_max_number
            settings.save()
            break
        except ValueError:
            print('Das war kein gültiges Ergebnis.')

    input('Drücke die "Enter"-Taste, um zurückzukehren.')