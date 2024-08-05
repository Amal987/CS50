def deep(val):
    if val == '42':
        return "Yes"
    elif val == "Forty Two":
        return "Yes"
    elif val == "forty-two":
        return "Yes"
    else:
        return "No"
    
input = input()
print(deep(input))