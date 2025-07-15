import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file (update file name and sheet name as needed)
df = pd.read_excel("C:\\Users\\Admin\\Desktop\\AP\\Alok_Civil_BMSCE\\OOPs\\student_marks.xlsx", sheet_name='Marks')

# Define max marks for each CO
max_marks = {
    'CO1': 100,
    'CO2': 50,
    'CO3': 75,
    'CO4': 100,
}

# Define CO to PO mapping
co_po_mapping = {
    'CO1': ['PO1', 'PO2'],
    'CO2': ['PO2', 'PO3'],
    'CO3': ['PO1', 'PO3'],
    'CO4': ['PO4'],
}

# Function to check if 60% students scored >= 60% marks
def co_achieved(marks_list, max_mark):
    threshold_score = 0.6 * max_mark
    students_above_threshold = [m for m in marks_list if m >= threshold_score]
    percentage = (len(students_above_threshold) / len(marks_list)) * 100
    return percentage >= 60

# Analyze each CO
achieved_cos = []
final_mapping = {}
co_status = {}

for co in max_marks.keys():
    marks = df[co].tolist()
    if co_achieved(marks, max_marks[co]):
        achieved_cos.append(co)
        final_mapping[co] = co_po_mapping.get(co, [])
        co_status[co] = "Achieved"
    else:
        co_status[co] = "Not Achieved"

# Print Achieved COs and Mapping
print("Achieved COs and their PO Mapping:")
for co in achieved_cos:
    print(f"{co} -> {', '.join(final_mapping[co])}")

# Plotting: Number of Students vs % Marks for a CO
def plot_marks_distribution(co_name):
    marks = df[co_name].tolist()
    max_mark = max_marks[co_name]
    percentages = [(m / max_mark) * 100 for m in marks]

    plt.figure(figsize=(8, 5))
    plt.hist(percentages, bins=10, color='skyblue', edgecolor='black')
    plt.axvline(60, color='red', linestyle='--', label='60% Threshold')
    plt.title(f'Marks Distribution for {co_name}')
    plt.xlabel('Marks Percentage')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example: Plot for CO1
plot_marks_distribution('CO1')