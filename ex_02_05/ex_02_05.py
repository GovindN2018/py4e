#temp_deg_cel = float(input('Enter temperature in deg. Celsius: '))
try:
    temp_deg_cel = float(input('Enter temperature in deg. Celsius: '))
    temp_deg_fahr = (temp_deg_cel * (9.0/5.0)) + 32.0
    print('Temperature in deg. Fahrenheit:', temp_deg_fahr)
except:
    print('Please enter a number')