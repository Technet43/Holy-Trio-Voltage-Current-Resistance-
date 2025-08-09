print("Hello , this is a tool which you can find voltage , current and resistance with the data you give")
value = int(input("İf you want to find the voltage press -> '1' \n"
              "İf you want to find the current press -> '2' \n"
              "İf you want to find the voltage press -> '3' \n"))
if value == 1:
    #data = input("You are finding the voltage . Please enter your Current and Resistance: (please separate with a space) ")
    #current , resistance = data.split(); # split function splits the value . but after you enter current you shouldnt immediatly press enter

    print("You are finding the Voltage . Please enter your Current and Resistance: ")
    current = float(input("Current: " ))
    print(f"Current {current} A")
    resistance = float(input("Resistance: "))
    print(f"Resistance {resistance} Ohm")
    voltage = current * resistance
    print(f"Great, according to the Current {current} Amper and Resistance {resistance} Ohm the Voltage is = {voltage} Volt")

elif value == 2:
    print("You are finding the Current . Please enter your Voltage and Resistance: ")
    voltage = float(input("Voltage: "))
    print(f"Voltage {voltage} V")
    resistance = float(input("Resistance: "))
    print(f"Resistance {resistance} Ohm")
    current = voltage / resistance
    print(f"Great, according to the Voltage {voltage} Volt and Resistance {resistance} Ohm the Current is = {current} Amper")

elif value == 3:
    print("You are finding the Resistance . Please enter your Voltage and Current: ")
    voltage = float(input("Voltage: "))
    print(f"Voltage {voltage} V")
    current = float(input("Current: "))
    print(f"Current {current} A")
    resistance = voltage / current
    print(f"Great, according to the Voltage {voltage} Volt and Current {current} Amper the Resistance is = {resistance} Ohm")
