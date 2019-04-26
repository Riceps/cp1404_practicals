"""
hexadecimal colour codes in a dictionary
"""

COLOUR_TO_HEX = {"beige": "#f5f5dc", "cadetblue": "#5f9ea0", "chocolate": "#d2691e", "coral": "#ff7f50",
                 "darkolivegreen": "#556b2f", "darkorchid": "#9932cc", "firebrick": "#b22222", "goldenrod": "#daa520",
                 "gray": "#bebebe", "hotpink": "#ff69b4"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(colour, "is", COLOUR_TO_HEX[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()
