__author__ = 'josh'
'''
This is my solution to the assignment found at
http://moodle.svcs.cs.pdx.edu/mod/assign/view.php?id=443
'''

#Converts user input to Kelvin to make life easier. I call this in the main function.
def convert_toK(temp, scale_indicator):
    if scale_indicator == "F":
        return (temp - 32) * 5 / 9 + 273.15
    elif scale_indicator == "C":
        return temp + 273.15
    elif scale_indicator == "R":
        return temp * 5 / 9
    elif scale_indicator == "K":
        return temp
    else: return "Error: invalid scale indicator."

#Gathers user input and does actual conversion.
def temp_converter():

    user_temp = raw_input("Please enter a temperature in F, C, K, or R (e.g. 86F)")
    scale_indicator = user_temp[-1]
    temp = int(user_temp[:-1])
    target_scale = raw_input("Please enter the scale to which you'd like to convert (F, C, K, or R)")

    x = convert_toK(temp, scale_indicator)
    if target_scale == "K":
        endvalue = x
    elif target_scale == "C":
        endvalue = x - 273.15
    elif target_scale == "F":
        endvalue = (x - 273.15) * 9 / 5 + 32
    elif target_scale == "R":
        endvalue = x * 9 / 5
    else:
        endvalue = "I can't do that."

    print("the temp is" + endvalue)

temp_converter()

