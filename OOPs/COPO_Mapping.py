import pandas as pd
import matplotlib.pyplot as plt

# File Path
excel_file = 'HYE Marks.xlsx'
sheet_name = 'marks'

# Read Excel file, skipping the first 4 rows since they contain headers and other information
df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=4)

# Check the structure of the imported data (First few rows)
print("Data Preview:")
print(df.head())

# Extract test marks and other student info
# The column headers will be 'Sno', 'USN', 'Name', 'Test1', 'Test2', ..., 'Test5'
# The data starts from row 5, so we'll focus on extracting the columns accordingly.

# Extract columns and rename as required
columns = ['S.No.', 'USN', 'Name', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5']
df.columns = columns


# Perform CO-PO Mapping based on 60% rule
# Define a function to check if a test is CO-PO mapped based on the 60% scoring rule
def perform_co_po_mapping(df):
    co_po_mapping = {}
    for test in ['Test1', 'Test2', 'Test3', 'Test4', 'Test5']:
        # Calculate the passing marks (60% of maximum marks)
        passing_marks = df[test].max() * 0.60
        # Count the number of students scoring >= 60%
        students_above_60 = df[df[test] >= passing_marks].shape[0]
        # If 60% or more of students scored >= 60%, map the CO to PO
        if students_above_60 >= (0.60 * df.shape[0]):
            co_po_mapping[test] = True
            print(f"{students_above_60}")
        else:
            co_po_mapping[test] = False
    return co_po_mapping


# Perform CO-PO Mapping
co_po_mapping = perform_co_po_mapping(df)
print("\nCO-PO Mapping:")
print(co_po_mapping)


# Plot the marks distribution for each test (Test1 to Test5)
def plot_marks_distribution(df):
    plt.figure(figsize=(12, 8))

    for idx, test in enumerate(['Test1', 'Test2', 'Test3', 'Test4', 'Test5']):
        plt.subplot(2, 3, idx + 1)
        plt.hist(df[test], bins=10, range=(0, df[test].max()), edgecolor='black')
        plt.title(f'{test} Marks Distribution')
        plt.xlabel('Marks')
        plt.ylabel('No. of Students')

    plt.tight_layout()
    plt.show()


# Plot the marks distribution for all tests
plot_marks_distribution(df)