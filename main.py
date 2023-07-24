d = int(input("Введите день рождения: "))
m = int(input("Введите месяц рождения: "))
y = int(input("Введите год рождения: "))


def ageCalculator(y, m, d):
    import datetime

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    return age


print('Возраст:', ageCalculator(y, m, d))
