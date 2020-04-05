COLOR_SELECTOR ={"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                 "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6"}

pick_a_color = input("Enter a Color Name:")

while pick_a_color != "":
    print("The code for \"{}\" is {}".format(pick_a_color,COLOR_SELECTOR.get(pick_a_color)))
    pick_a_color = input("Enter a Color Name:")

