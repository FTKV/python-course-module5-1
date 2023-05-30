text = "Hello+World"

print(text.translate({ord("+"): " ", ord("W"): "+", ord("l"): "-"}))

print(text.replace("World", "Hello"))