__author__ = 'josh'
'''
This is my solution to the assignment found at
http://moodle.svcs.cs.pdx.edu/mod/assign/view.php?id=443
'''
def convert_toK(temp, scale_indicator):
    temp = int(temp)
    if scale_indicator == "F":
        return (temp - 32) * 5 / 9 + 273.15
    elif scale_indicator == "C":
        return temp + 273.15
    elif scale_indicator == "R":
        return temp * 5 / 9
    else: return "Error; incorrect scale indicator"

def temp_converter():

    user_temp = raw_input("Please enter a temperature in F, C, K, or R (e.g. 86F)")
    scale_indicator = user_temp[-1]
    temp = user_temp[:-1]
    convert_to = raw_input("Please enter the scale to which you'd like to convert (F, C, K, or R)")

    if convert_to == "K":
        endvalue = convert_toK(temp, scale_indicator)
        print endvalue
    else: return False

temp_converter()

