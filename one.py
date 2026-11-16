COLUMNS = ("Roll No", "Name", "Course", "Marks")

records = []


def find_record(roll):
    """Return the record with the given roll number, or None."""
    for rec in records:
        if rec["roll"] == roll:
            return rec
    return None


def read_roll(text):
    """Convert text to an int roll number; return None if invalid."""
    try:
        return int(text)
    except ValueError:
        return None


def read_marks(text):
    """Convert text to int marks; return None if not a number."""
    try:
        return int(text)
    except ValueError:
        return None


def add_record(roll, name, course, marks):
    roll = read_roll(roll)
    if roll is None:
        print("Invalid roll number.")
        return
    if find_record(roll) is not None:
        print(f"Roll number {roll} already exists.")
        return
    marks = read_marks(marks)
    if marks is None or not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return
    records.append({"roll": roll, "name": name, "course": course, "marks": marks})
    print(f"Record added: {roll} | {name} | {course} | {marks}")


def view_records():
    if not records:
        print("No records found.")
        return
    line = "-" * 46
    print(line)
    print(f"{COLUMNS[0]:<10}{COLUMNS[1]:<16}{COLUMNS[2]:<12}{COLUMNS[3]:<6}")
    print(line)
    for rec in records:
        print(f"{rec['roll']:<10}{rec['name']:<16}{rec['course']:<12}{rec['marks']:<6}")
    print(line)


def search_record(roll):
    roll = read_roll(roll)
    rec = find_record(roll) if roll is not None else None
    if rec is None:
        print(f"Roll number {roll} not found.")
        return
    print(f"{rec['roll']} | {rec['name']} | {rec['course']} | {rec['marks']}")


def update_record(roll, marks):
    roll = read_roll(roll)
    rec = find_record(roll) if roll is not None else None
    if rec is None:
        print(f"Roll number {roll} not found.")
        return
    marks = read_marks(marks)
    if marks is None or not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return
    rec["marks"] = marks
    print(f"Marks updated: {marks}")


def delete_record(roll):
    roll = read_roll(roll)
    rec = find_record(roll) if roll is not None else None
    if rec is None:
        print(f"Roll number {roll} not found.")
        return
    records.remove(rec)
    print(f"Record deleted: {roll}")


def main():
    while True:
        print("\n1. Add  2. View  3. Search  4. Update marks  5. Delete  6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            data = [x.strip() for x in input("Enter roll, name, course, marks: ").split(",")]
            if len(data) != 4:
                print("Enter exactly 4 values: roll, name, course, marks.")
            else:
                add_record(*data)
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record(input("Enter roll number: ").strip())
        elif choice == "4":
            roll = input("Enter roll number: ").strip()
            marks = input("Enter new marks: ").strip()
            update_record(roll, marks)
        elif choice == "5":
            delete_record(input("Enter roll number: ").strip())
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Enter 1-6.")


if __name__ == "__main__":
    main()