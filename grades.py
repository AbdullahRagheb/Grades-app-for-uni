import numpy as np

def manage_grades():
    # Initialize a list to store grades
    grades = []
    
    # Input grades for 10 students
    print("Please enter the midterm exam grades for 10 students (out of 30):")
    for i in range(10):
        while True:
            try:
                grade = float(input(f"Grade for student {i+1}: "))
                if 0 <= grade <= 30:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade. It must be between 0 and 30.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Convert grades list to a NumPy array for easier calculations
    grades_array = np.array(grades)
    
    # Calculating minimum and maximum grades
    min_grade = np.min(grades_array)
    max_grade = np.max(grades_array)
    
    # Calculating the range of grades
    range_of_grades = max_grade - min_grade
    
    # Calculating the average grade
    average_grade = np.mean(grades_array)
    
    # Calculating the standard deviation of grades
    std_deviation = np.std(grades_array)
    
    # Display the results
    print("\nResults:")
    print(f"Minimum Grade: {min_grade}")
    print(f"Maximum Grade: {max_grade}")
    print(f"Range of Grades: {range_of_grades}")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Standard Deviation of Grades: {std_deviation:.2f}")

# Run the program
manage_grades()
