def is_leap(year):
    leap = False
        
    # Write your logic here
    normal = year % 4
    hundred = year % 100
    quarter = year % 400

    if (hundred == 0 and quarter == 0):
        leap = True
    else:
        if (normal == 0 and hundred != 0):
            leap = True        
    return leap

year = int(input())
print(is_leap(year))