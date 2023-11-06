#!python3

# Formatted output to right/left justify string output
# This table was drawn using unicode symbols found at https://www.unicode.org/charts/PDF/U2500.pdf
outString = "word"

#These two equivalent ways to left justify in a space of 10 chracters
print(f"┌──────────┬────────────┐")
print(f"│L Justify │ {outString.ljust(10)} │")
print(f"│L-Justify │ {outString:<10} │")
print(f"│──────────┼────────────┤")
#These two equivalent ways to right justify in a space of 10 characters
print(f"│R Justify │ {outString.rjust(10)} │")
print(f"│R-Justify │ {outString:>10} │")