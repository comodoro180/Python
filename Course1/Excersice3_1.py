INCREMENT = 1.5
TOP_HRS = 40.0

gross_pay = 0.0
bonus = 0.0

hrs = input("Enter hours:")
hrs = float(hrs)
rate = input("Rate:")
rate = float(rate)

if hrs > TOP_HRS:
    bonus = (hrs - TOP_HRS) * (rate * INCREMENT)
    gross_pay = bonus + (TOP_HRS * rate)
elif hrs > 0.0:
    gross_pay = hrs * rate

print(gross_pay)


