def dec2base(base, decimal):
    binaries = []
    while decimal > 0:
        rest = decimal % base
        binaries.append(rest)
        decimal = decimal / base
    s = ''
    for addr_part in reversed(binaries):
        s += str(addr_part)
    while len(s) < 8:
        s = '0' + s
    return s
