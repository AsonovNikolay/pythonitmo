import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    step = 0
    main = []
    ciphertext = ""
    position = 0
    for x in plaintext:
        main.append(x)
    mainlistup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mainlistdown = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(len(main)):
        if main[x] in mainlistup:
            position = mainlistup.index(main[x])
            if position + shift > 25:
                position = position + shift - 26
            else:
                position += shift
            main[x] = mainlistup[position]
        elif main[x] in mainlistdown:
            position = mainlistdown.index(main[x])
            if position + shift > 25:
                position = position + shift - 26
            else:
                position += shift
            main[x] = mainlistdown[position]
        ciphertext += main[x]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    step = 0
    main = []
    plaintext = ""
    position = 0
    for x in ciphertext:
        main.append(x)
    mainlistup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mainlistdown = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(len(main)):
        if main[x] in mainlistup:
            position = mainlistup.index(main[x])
            if position - shift < 0:
                position = position - shift + 26
            else:
                position -= shift
            main[x] = mainlistup[position]
        elif main[x] in mainlistdown:
            position = mainlistdown.index(main[x])
            if position - shift < 0:
                position = position - shift + 26
            else:
                position -= shift
            main[x] = mainlistdown[position]
        plaintext += main[x]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
