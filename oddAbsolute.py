def calculateAbsolute():
    # This first line is provided for you
    try:
        in_num  = int(input("Enter a number: "))
    except:
        print('Please enter a numeric value:')  
    num_value = abs(in_num)
    if num_value > 21:
        result = (num_value - 21) * 2
    else:
        result = 21 - num_value
    return abs(result)    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
difference = calculateAbsolute()
print ('Result:', difference)