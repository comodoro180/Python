RANGE_INI = 0.0
RANGE_END = 1.0

score = input("Enter score: ")
try:
    score = float(score)
finally:
    print("Wrong number!")
    quit()

if RANGE_INI <= score <= RANGE_END:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Score out of range")
