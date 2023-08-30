def computepay(hours, rate): 
    print("In computepay: ", hours, rate)
    hours = input("Enter hours:")
    rate = input("Enter rate: ")
    fh = float(hours)
    fr = float(rate)
    xp = fh * fr

    if fh > 40: 
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        print("Pay:", xp)


computepay(40,10)