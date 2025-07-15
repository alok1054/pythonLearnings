# Sample CO to PO mapping (example, can be extended)
co_po_mapping = {
    'CO1': ['PO1', 'PO2'],
    'CO2': ['PO2', 'PO3'],
    'CO3': ['PO1', 'PO3'],
    'CO4': ['PO4'],
}

# Maximum marks for each CO
max_marks = {
    'CO1': 100,
    'CO2': 50,
    'CO3': 75,
    'CO4': 100,
}

# Marks obtained by students for each CO
student_marks = {
    'CO1': [65, 70, 40, 80, 60, 55],
    'CO2': [45, 48, 40, 20, 10],
    'CO3': [70, 65, 60, 50, 40, 35, 30],
    'CO4': [90, 92, 95, 88, 75, 60, 55],
}

def co_achieved(marks_list, max_mark):
    threshold_score = 0.6 * max_mark
    students_above_threshold = [m for m in marks_list if m >= threshold_score]
    percentage = (len(students_above_threshold) / len(marks_list)) * 100
    return percentage >= 60

# Compute CO-PO mapping based on achievement
achieved_cos = []
final_mapping = {}

for co, marks in student_marks.items():
    if co_achieved(marks, max_marks[co]):
        achieved_cos.append(co)
        final_mapping[co] = co_po_mapping.get(co, [])

# Display results
print("Achieved Course Outcomes (COs):")
for co in achieved_cos:
    print(f"{co}")

print("\nMapped Program Outcomes (POs):")
for co, pos in final_mapping.items():
    print(f"{co} maps to {', '.join(pos)}")