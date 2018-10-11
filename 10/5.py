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

def main():
    stu1 = Students("Tim")
    stu1.addGrade(4, 3)
    stu1.addGrade(3.4, 4)
    print(stu1.get_gpa())


if __name__ == "__main__":
    main()
