# Format Specifiers -> {value:flags} format a value based on what
#                      flags are inserted
#                      is used with f strings
# {value:.2f}
# {value:,}
# {value:010}
# {value:^}
# {value:>}
# {value:<}
# {value:+} or {value, }
# {value:=}

price1 = 1222.99
price2 = -1000.764
price3 = 9876.845

print(f"Price of price1 $ {price1: ,.2f}")
print(f"Price of price2 $ {price2: ,.2f}")
print(f"Price of price3 $ {price3: ,.2f}")
