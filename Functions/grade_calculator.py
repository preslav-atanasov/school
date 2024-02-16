def solve(grade_data):
    if 2.00 <= grade_data <= 2.99:
        grade = "Fail"
    elif 3.00 <= grade_data <= 3.49:
        grade = "Poor"
    elif 3.50 <= grade_data <= 4.49:
        grade = "Good"
    elif 4.50 <= grade_data <= 5.49:
        grade = "Very Good"
    elif 5.50 <= grade_data <= 6.00:
        grade = "Excellent"
    else:
        grade = "Please enter a valid grade"
    return grade


gradeFloat = float(input())


print(solve(gradeFloat))
