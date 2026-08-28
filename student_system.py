# Student Grading and Management System
# Created by Aman for University Portfolio

def calculate_grade(marks):
    if marks >= 90: return 'A+'
    elif marks >= 80: return 'A'
    elif marks >= 70: return 'B'
    elif marks >= 60: return 'C'
    else: return 'Pass/Fail'

def main():
    print("=== Student Performance Management System ===")
    student_name = input("Enter student name: ")
    
    try:
        maths = float(input("Enter Mathematics marks (out of 100): "))
        science = float(input("Enter Science marks (out of 100): "))
        computer = float(input("Enter Computer Science marks (out of 100): "))
        
        total = maths + science + computer
        percentage = (total / 300) * 100
        final_grade = calculate_grade(percentage)
        
        print("\n--- Performance Report ---")
        print(f"Student Name: {student_name}")
        print(f"Total Marks: {total}/300")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Final Academic Grade: {final_grade}")
        print("--------------------------")
        
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
