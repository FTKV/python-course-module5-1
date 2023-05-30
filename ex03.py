lorem = "Ljrhwp hhwejlw riljw oi qjrjlkqw e?"

print(lorem.upper())

print(lorem)

lorem_up = lorem.upper()

lorem = lorem.upper()

find_l_first = lorem.find("h".upper())

find_l_last = lorem.rfind("h".upper())

print(lorem[find_l_first:find_l_last + 1])

# if find_l >= 0:
#     print(f"""FInd in position {find_l}""")
# else:
#     print("Not find")