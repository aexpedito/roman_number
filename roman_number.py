import sys
import re

numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

acceptable = set('IVXLCDM')

def acceptable_chars(string):
    validation = set(string)
    if validation.issubset(acceptable):
        return True
    else:
        return False
def validate_char_count(string):
    result = re.findall("([I]{4,}|[V]{4,}|[X]{4,}|[L]{4,}|[C]{4,}|[D]{4,}|[M]{4,})", string)
    if len(result) != 0:
        return True
    return False

def roman_to_int(roman):
    #verifica se o numero contem apenas os caracteres romanos
    if not acceptable_chars(roman):
        print(f"{roman}: Invalid Roman Number")
        return -1

    if validate_char_count(roman):
        print(f"{roman}: Invalid Roman Number")
        return -1

    #tranforma string para array
    array_chars = []
    for char in roman:
        array_chars.append(char)

    #computa o total
    total = 0
    for i in range(0, len(array_chars)-1):
        if numbers[array_chars[i+1]] <= numbers[array_chars[i]]:
            total += numbers[array_chars[i]]
        else:
            total -= numbers[array_chars[i]]

    #soma o ultimo caracter
    total += numbers[array_chars[-1]]

    return total


if __name__ == "__main__":
    roman = sys.argv[1]
    print(f"{roman} = {roman_to_int(roman)}")
