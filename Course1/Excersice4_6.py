INCREMENT = 1.5
TOP_HRS = 40.0


# Compute the gross pay
def computepay(h: float,
               r: float) -> float:
    gross_pay = 0.0

    if h > TOP_HRS:
        bonus = (h - TOP_HRS) * (r * INCREMENT)
        gross_pay = bonus + (TOP_HRS * r)
    elif hrs > 0.0:
        gross_pay = h * r

    return gross_pay


hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)
