def iban_formatter(iban):
    iban_list = []
    iterations = 0
    for char in iban:
        iterations += 1
        if iterations == 5 and char != " ":
            iban_list.append(" ")
            iterations = 1
        elif iterations == 5 and char == " ":
            iterations = 0
        iban_list.append(char)
    return "".join(iban_list)


iban_formatter("BG80BNBG96611020345678")
