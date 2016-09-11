def answer(x, y, z):
    # This method takes three integers as arguments and returns possible date configurations assuming
    # 1. All three integers are between 1 and 99
    # 2. If there are multiple possible dates or no date is possible, return "Ambiguous"
    # 3. There are no leap years (calendar is consistent every year)
    
    # Perform basic checks
    month=-1
    if x==y and x==z:
        month=x
    if (x<13 and y<13) or (z<13 and y<13) or (x<13 and z<13):
        if month==-1: return "Ambiguous"
    if month>12: return "Ambiguous"
    
    # Set month
    if x<13: month = x
    if y<13: month = y
    if z<13: month = z
    if not month: return "Ambiguous"
    a = [x,y,z]
    if month in a:
        a.remove(month)
    
    # Declare # of days/month
    NumDays=[31,28,31,30,31,30,31,31,30,31,30,31]

    # Set year
    year = -1
    if x>NumDays[month-1]: year = x
    if y>NumDays[month-1]: year = y
    if z>NumDays[month-1]: year = z
    if a[0]==a[1]: year=a[0]
    if year == -1: return "Ambiguous"
    if year in a:
        a.remove(year)
    
    # Set day
    day = a[0]
    if day>NumDays[month-1]: return "Ambiguous"
    
    # Fix # of digits, set to 2 for each
    if len(str(month))==1:
        month = "0" + str(month)
    if len(str(day))==1:
        day = "0" + str(day)
    if len(str(year))==1:
        year = "0" + str(year)
        
    return str(month) + "/" + str(day) + "/" + str(year)