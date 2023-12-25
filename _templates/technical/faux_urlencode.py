import sys

def faux_urlencode(string):
    result = []
    for char in string.lower():
        if char.isalnum():
            result.append(char)
        elif char != ' ':
            result.append(format(ord(char), '02X'))
    return ''.join(result)

input_string = sys.stdin.read().strip()
print(faux_urlencode(input_string))
