phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    val = value[1:]
    print("00{}".format(val))