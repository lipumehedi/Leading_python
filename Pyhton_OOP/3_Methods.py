class Employee:
    def __init__(self, name, hours_worked_list):
        self.name = name
        self.hours_worked = hours_worked_list
        
    def get_total_hours(self):
        total = sum(self.hours_worked)
        print(f"{self.name} worked a total of {total} hours.")


emp1 = Employee("Rika", [8, 7, 9, 8, 6])
emp2 = Employee("Ayase", [7, 8, 8, 9, 8])
emp3 = Employee("Tanaka", [9, 6, 8, 7, 9])
emp4 = Employee("Sato", [9, 9, 6, 8, 7])


emp1.get_total_hours()
emp2.get_total_hours()
emp3.get_total_hours()
emp4.get_total_hours()