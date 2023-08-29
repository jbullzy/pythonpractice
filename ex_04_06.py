def computepay(hours, rate): 
    print("In computepay: ", hours, rate)
    hours = input("Enter hours:")
    rate = input("Enter rate: ")
    fh = float(hours)
    fr = float(rate)

    if fh > 40: 
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
    else:
        xp = fh * fr
    print("Pay:",xp)

computepay(fh, fr)