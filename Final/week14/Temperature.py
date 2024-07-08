"""Week14"""

def c_temp(celcius, want):
    """Celcius"""
    if want == "F":
        return celcius * (9/5) + 32
    elif want == "K":
        return celcius + 273.15
    elif want == "R":
        return (celcius+ 273.15) * (9/5)
