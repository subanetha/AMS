class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, student_name):
        self.students[student_id] = {"name": student_name, "attendance": {}}

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            self.students[student_id]["attendance"][date] = "Present"

    def view_attendance(self, student_id):
        if student_id in self.students:
            print(f"Attendance for {self.students[student_id]['name']}:")
            for date, status in self.students[student_id]["attendance"].items():
                print(f"{date}: {status}")
        else:
            print("Student not found.")

    def run(self):
        while True:
            print("Attendance Monitoring System")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Attendance")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                self.add_student(student_id, student_name)
            elif choice == "2":
                student_id = input("Enter student ID: ")
                date = input("Enter date (YYYY-MM-DD): ")
                self.mark_attendance(student_id, date)
            elif choice == "3":
                student_id = input("Enter student ID: ")
                self.view_attendance(student_id)
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    system = AttendanceSystem()
    system.run()