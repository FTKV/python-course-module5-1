def custom_split(text: str, split_symbol: str="") -> list:
    result = []
    temp_str = ""
    for i in text:
        if i == split_symbol:
            result.append(temp_str)
            temp_str = ""
            continue
        temp_str += i

    return result

lorem = "Ljrhwp hhwejlw  riljw oi qjrjlkqw e?"


print(custom_split(lorem, " "))