def nan_expand(times):
    nan = "NaN"
    if times == 0:
        return ""
    else:
        result = f"{times * 'Not a '}{nan}"

    return result

nan_expand(3)