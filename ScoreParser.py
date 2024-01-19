import pandas as pd

def analyze_marks(marks_data):
    students = marks_data.split(" -> ")

    # Extracting marks for each student
    student_marks = [list(map(int, student.split(":")[1].split(','))) for student in students]

    # Calculate total marks for each student
    total_marks = [sum(student) for student in student_marks]

    # Find the top three scorers
    top_scorers_indices = sorted(range(len(total_marks)), key=lambda k: total_marks[k], reverse=True)[:3]
    top_scorers = [(index + 1, total_marks[index]) for index in top_scorers_indices]

    # Count the number of failed candidates
    failed_candidates = sum(any(mark < 35 for mark in student) for student in student_marks)

    # Count the number of students who scored a hundred in at least one subject
    hundred_scorers = sum(any(mark == 100 for mark in student) for student in student_marks)

    # Extract top 10 scores in Maths (assuming 4th subject is Maths)
    math_scores = [student[3] for student in student_marks]
    top_10_math_scores = sorted(math_scores, reverse=True)[:10]

    return top_scorers, failed_candidates, hundred_scorers, top_10_math_scores


def analyze_marks_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    marks_data = ' -> '.join(lines)
    return analyze_marks(marks_data)

file_path = 'marks.txt'
top_scorers, failed_candidates, hundred_scorers, top_10_math_scores = analyze_marks_from_file(file_path)

data = {
    'Top Scorers': [top_scorers],
    'Failed Candidates': [failed_candidates],
    'Hundred Scorers': [hundred_scorers],
    'Top 10 Scores in Maths': [top_10_math_scores]
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_excel_file = 'analysis_results.xlsx'
df.to_excel(output_excel_file, index=False)
print(f"Results saved to {output_excel_file}")
