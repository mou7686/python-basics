def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)

    return the_mean

student_grades = {"marry":9.1,"sim":8.8,"jhon":7.5}
monday_temperatures = [8.8,9.1,9.9]
print(mean(student_grades))    