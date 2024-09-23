

def drop_decimal_but_first(num):
    # Convert number to string and split it by the decimal point
    num_str = str(num)
    
    if '.' in num_str:
        # Split into integer and decimal parts
        integer_part, decimal_part = num_str.split('.')
        # Keep only the first digit of the decimal part
        decimal_part = decimal_part[0]
        # Combine the integer part with the first decimal digit
        result = f"{integer_part}.{decimal_part}"
    else:
        # If there's no decimal point, return the number as is
        result = num_str
    
    return float(result)