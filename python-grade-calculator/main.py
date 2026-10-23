
def calculate_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    elif average >= 33:
        return "D"
    return "F"


def main():
    print("=== Student Grade Calculator ===")

    name = input("Student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    subjects = ["Python", "SQL", "Computer Science"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject} marks (0-100): "))

                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100.")
                    continue

                marks.append(mark)
                break

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("\n=== Result ===")
    print("Student:", name)
    print(f"Total: {total:g}/{len(subjects) * 100}")
    print(f"Average: {average:.2f}%")
    print("Grade:", grade)


if __name__ == "__main__":
    main()
