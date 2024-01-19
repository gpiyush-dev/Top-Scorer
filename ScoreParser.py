import pandas as pd

def analyze_marks(marks_data):
    students = marks_data.split(" -> ")

    # Extracting marks for each student
    student_data = [student.split(":") for student in students]
    student_ids = [int(student[0]) for student in student_data]
    student_marks = [list(map(int, student[1].split(','))) for student in student_data]

    # Calculate total marks for each student
    total_marks = [sum(student) for student in student_marks]

    # Find the top three scorers
    top_scorers_indices = sorted(range(len(total_marks)), key=lambda k: total_marks[k], reverse=True)[:3]
    top_scorers = [(student_ids[index], total_marks[index]) for index in top_scorers_indices]

    # Count the number of failed candidates
    failed_candidates = sum(any(mark < 35 for mark in student) for student in student_marks)

    # Count the number of students who scored a hundred in at least one subject
    hundred_scorers = sum(any(mark == 100 for mark in student) for student in student_marks)

    # Extract top 10 scores in Maths (assuming 4th subject is Maths)
    math_scores = [(student_ids[index], student[3]) for index, student in enumerate(student_marks)]
    top_10_math_scores = sorted(math_scores, key=lambda x: x[1], reverse=True)[:10]
    top_10_math_scorer_ids = [student[0] for student in top_10_math_scores]

    # Extracting IDs and scores of top 3 scorers
    top_3_scorers_with_scores = [(student_ids[index], total_marks[index]) for index in top_scorers_indices]

    return top_3_scorers_with_scores, failed_candidates, hundred_scorers, top_10_math_scorer_ids


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
