"""
Toy implementation of LZW compression.
"""

def init_symbols():
    """
    Create table of ASCII codes.
    """
    symbols = []
    for i in range(256):
        symbols.append(chr(i))
    
    return symbols

def encode(text):
    """
    Initialise symbols
    Check to see if the current characters are in the table.
    If they are, record the code, otherwise add it to the table
    """

    symbols = init_symbols()

    result = []
    p = text[0]
    for c in text[1:]:
        if p + c in symbols:
            p = p + c
        else:
            result.append(symbols.index(p) + 1)
            symbols.append(p + c)
            p = c

    result.append(symbols.index(p) + 1)
    return result


def decode(codes):
    """
    Use inference of the first few characters to rebuild the symbols
    table.
    """

    symbols = init_symbols()

    result = ""

    p = symbols[codes[0] -1]
    result += p

    for code in codes[1:]:
        if code - 1 <= len(symbols):
            entry = symbols[code - 1]
        elif code - 1 > len(symbols):
            entry = p + p[0]
        else:
            raise ValueError("Invalid LZW code")
        result += entry
        symbols.append(p + entry[0])
        p = entry
    
    return result


def write_file(data):

    with open("encoded", "w") as f:
        for c in data:
            f.write(chr(c))


def read_file():
    codes = []
    with open("encoded", "r") as f:
        data = f.read()
    
    for d in data:
        codes.append(ord(d))

    print(codes)

    return decode(codes)

with open("orig.txt") as f:
    text = f.read()

result = encode(text)
print(f"Encoded = {len(result)} as opposed to {len(text)}")

dec = decode(result)
