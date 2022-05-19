name1 = "Tom"
height1 = 1.68
weight1 = 60

name2 = "Ванесса"
height2 = 1.84
weight2 = 83

name3 = "Жаклин"
height3 = 1.78
weight3 = 89


def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("ИНдеск массы тела: " + str(bmi))
    if bmi < 25:
        return name + " не имеет лишный вес"
    else:
        return name + " имеет лишный вес"

bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)

print(bmi1)
print(bmi2)
print(bmi3)
