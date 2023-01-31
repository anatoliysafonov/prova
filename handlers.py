class Suggetion:
    def __init__(self):
        self.message = []

    def clear(self):
        self.message.clear()


class Command:
    suggetion = True

    def __init__(self):
        self.suggetion = True

    def __call__(self, *args):
        self.precommand()
        result = self.command(*args)
        self.postcommand()
        return result

    def precommand(self):
        pass

    def command(self, *args):
        pass

    def postcommand(self):
        pass


class Add(Command):
    """To use ADD command use format: add name [phone] [birthday]"""
    def command(self, *args):
        name, phone, birthday = args
        if not name:
            return self.__doc__
        if Command.suggetion and self.suggetion:
            if not phone:
                suggetion.message.append('Tip: To add phone number use: add [name] [phone] ')
                self.suggetion = False
            if not birthday:
                suggetion.message.append('Tip: To set birthday use: set birthday [name] [date]')
                self.suggetion = False
        return 'THIS IS A ADD COMMAND WIH {} ARGUMENTS'.format(args)


class Sub(Command):
    """To use DEL function use a format: del [name] [phone]"""
    
    
    def command(self, *args):
        if Command.suggetion and self.suggetion:
            suggetion.message.append('TIP: del [name] -> to delete entire contact')
            suggetion.message.append('TIP: del [name] [phone] -> to delete phone\'s number from contact')
            self.suggetion = False
        name, phone, *_ =  args
        if not name:
            return self.__doc__
        return 'THIS IS A DEL COMMAND WIH {} ARGUMENTS'.format(args)


suggetion = Suggetion()


def set_tips(*args):
    """To set enable/disable tips use: set tips [on]/[off]"""
    is_enable, *_ = args
    if not is_enable or (is_enable != 'off' and is_enable != 'on'):
        return set_tips.__doc__
    Command.suggetion = is_enable
    return 'TIPS is {}'.format(is_enable)


BOT_COMMANDS = {
    'add': Add(),
    'del': Sub(),
    'set_tips': set_tips,
}


def input_parser(string: str) -> tuple:
    string = string.split()
    func, *arguments = string
    func = BOT_COMMANDS.get(func)
    return func, arguments







