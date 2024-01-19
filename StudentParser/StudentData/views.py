import pandas as pd
from django.shortcuts import render

# Create your views here.
def display_student_statistics(request):
    # Change 'path/to/your/excel/file.xlsx' to the actual path of your Excel file
    excel_file_path = 'C:\\Users\\Piyush\\analysis_results.xlsx'

    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    # Extract values from the Excel file
    top_scorers = df.at[0, 'Top Scorers']
    failed_candidates = df.at[0, 'Failed Candidates']
    hundred_scorers = df.at[0, 'Hundred Scorers']
    top_10_math_scorers = df.at[0, 'Top 10 Scores in Maths']

    return render(request, 'display_student_statistics.html', {
        'top_scorers': top_scorers,
        'failed_candidates': failed_candidates,
        'hundred_scorers': hundred_scorers,
        'top_10_math_scorers': top_10_math_scorers,
    })
