# Cleaner, but a list expression would be nicer.
def gradingStudents(grades):
    rounded = []

    for i in grades:
        r = i%5

        if r > 2 and i > 37:
            rounded.append(i-r+5)
        else:
            rounded.append(i)

    return rounded
