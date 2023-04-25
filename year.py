class IsLeapYear:
    def __init__(self, year):
        self.year = year

    def check(self):
        if self.year % 4 == 0:
            return True
        elif self.year % 100 == 0 and self.year % 400 != 0:
            return False
        else:
            return False

year = 2021
print(year, " is a leap year." if IsLeapYear(year).check() else " is not a leap year")



