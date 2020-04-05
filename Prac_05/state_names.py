"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
NAME_OF_STATES = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory",
                  "WA" : "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
                  "TAS": "Tasmania"}
print(NAME_OF_STATES)

states = input("Enter short state: ").upper()
while states != "":
    if states in NAME_OF_STATES:
        print(states, "is", NAME_OF_STATES[states])
    else:
        print("Invalid short state")
    states = input("Enter short state: ")