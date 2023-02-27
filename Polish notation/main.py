
def parse_string(string:str):
    operation = string.lstrip()[0]
    args= string[1:].split()
    return operation, args

def get_numeric(args:list[str]) -> list[float]:
    return [float(i) for i in args]

def multi(args:list):
    result = 1
    for i in args:
        result = result * i
    return result

def add(args:list[str]) ->int:
    return sum(args)

def minus(args:list[str]) ->int:
    result, *other = args
    for i in other:
        result = result-i
    return result

def div(args:list[str]) ->float:
    result, *other = args
    for i in other:
        result = result/i
    return result

OPERATIONS = {
    '+':add,
    '*':multi,
    '-':minus,
    '/':div,
}

def parse(string:str)->str:
    start = end = -1
    if string.isnumeric():
        return string
    for index, char in enumerate(string):
        if char =='(':
            start = index
        if char == ')' and start!=-1:
            end = index
            func, arguments = parse_string(string[start+1:end])
            res = str(OPERATIONS.get(func)(get_numeric(arguments)))
            return  (parse(string[:start] + res + string[end +1:])).strip()

    return string


string = '(+(*5 20) 4)'
print(round(float(parse(string)),5))