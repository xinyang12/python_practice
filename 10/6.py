class Students:
    def __init__(self, name):
        self.name = name
        self.hours = 0.0
        self.qpoints = 0.0

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_qpoints(self):
        return self.qpoints

    def get_gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints += gradePoint
        self.hours += credits

    def addLetterGrade(self, gradePoint, credits):
        if gradePoint == 'A':
            self.qpoints += 4
        elif gradePoint == 'B':
            self.qpoints += 3
        elif gradePoint == 'C':
            self.qpoints += 2
        else:
            self.qpoints += 1

        self.hours += credits

def main():
    stu1 = Students("Tim")
    stu1.addGrade(4, 3)
    stu1.addGrade(3.4, 4)
    stu1.addLetterGrade('A', 3)
    stu1.addLetterGrade('B', 4)
    print(stu1.get_gpa())


if __name__ == "__main__":
    main()
