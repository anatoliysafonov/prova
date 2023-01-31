from handlers import input_parser, BOT_COMMANDS
from handlers import suggetion
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

completer = WordCompleter(list(BOT_COMMANDS))
session = PromptSession()
while True:
    answer = session.prompt('command: ', completer = completer)
    if answer == 'close':
        break
    func, arguments = input_parser(answer)
    arguments = [arguments[i] if i < len(arguments) else None for i in range(3)]
    if not func:
        print('command not found')
        continue
    result = func(*arguments)
    if suggetion.message:
        for message in suggetion.message:
            print(message)
        suggetion.clear()
    print(result)
