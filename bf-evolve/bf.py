# A modified version of the brainfuck interpreter found at https://github.com/pocmo/Python-Brainfuck

from settings import *


def evaluate(code):
    code = cleanup(list(code))
    bracemap = buildbracemap(code)
    result = ''
    command_count = 0

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < len(ALPHABET)-1 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else len(ALPHABET)-1

        if command == "[" and cells[cellptr] == 0:
            codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0:
            codeptr = bracemap[codeptr]
        if command == ".":
            result += to_char(cells[cellptr])
        if command == ",":
            # Read the last written character or 0
            cells[cellptr] = ALPHABET.index(result[-1]) if result else 0

        codeptr += 1

        command_count += 1
        if command_count > 2000:
            break

    return result


def to_char(num):
    return ALPHABET[num % len(ALPHABET)]


def cleanup(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[":
            temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


