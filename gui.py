import tkinter as tk
from keras.models import load_model
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from report_generator import generate_patient_report

scaler = StandardScaler()
data = pd.read_csv('HepatitisCdata.csv')
X_t = data[['ALB', 'AST', 'BIL', 'CHE', 'CHOL', 'GGT']]

def reset_inputs():
    # Clear all input fields
    for entry in entry_list:
        entry.delete(0, tk.END)

def submit_inputs():
    # Get the values from the input fields
    values = [entry.get() for entry in entry_list]
    # Perform the desired action with the values (e.g., call your machine learning model)
    print("Submitted values:", values)
    input_list = np.array([values[i] for i in [2, 5, 6, 7, 8, 10]]).reshape(1, -1)
    X = scaler.fit_transform(X_t)
    arr = scaler.transform(input_list)
    model = load_model('mlp_model.h5')
    out = np.argmax(model.predict(arr))
    if out == 0:
        print("Chances are that Hepatitis-C is not present")
    elif out == 1:
        print("Chances of Stage 1 Hepatitis C (Hepatitis)")
    elif out == 2:
        print("Chances of Stage 2 Hepatitis C (Fibrosis)")
    else:
        print("Chances of Stage 3 Hepatitis C (Cirrhosis)")


def generate_report():
    print("Enter the necessary details accordingly")
    generate_patient_report()
    print("Report generated")

    # Start the UI
    #window.mainloop()

# Create the main window
window = tk.Tk()
window.title("DeepHepa-C")

# Create the box with 12 inputs
entry_list = []

label = tk.Label(window, text="Enter Age: ")
label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter your Gender: ")
label.grid(row=1, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=1, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Albumin Blood Test (ALB) value: ")
label.grid(row=2, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=2, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Alkaline Phosphatase (ALP) value: ")
label.grid(row=3, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=3, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Alkaline Phosphatase (ALP) value: ")
label.grid(row=3, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=3, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Alanine Transaminase (ALT) value: ")
label.grid(row=4, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=4, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Aspartate Transaminase (AST) value: ")
label.grid(row=5, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=5, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Bilirubin (BIL) value: ")
label.grid(row=6, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=6, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Acetylcholinesterase (CHE) value: ")
label.grid(row=7, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=7, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Cholesterol (CHOL) value: ")
label.grid(row=8, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=8, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Creatinine (CREA) value: ")
label.grid(row=9, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=9, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Gamma-Glutamyl Transferase (GGT) value: ")
label.grid(row=10, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=10, column=1, padx=5, pady=5)
entry_list.append(entry)

label = tk.Label(window, text="Enter Proteins (PROT) value: ")
label.grid(row=11, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=11, column=1, padx=5, pady=5)
entry_list.append(entry)

# Create the buttons
reset_button = tk.Button(window, text="Reset", command=reset_inputs)
reset_button.grid(row=12, column=0, padx=5, pady=10)

submit_button = tk.Button(window, text="Submit", command=submit_inputs)
submit_button.grid(row=12, column=1, padx=5, pady=10)

report_button = tk.Button(window, text="Generate Report", command=generate_report)
report_button.grid(row=12, column=2, padx=5, pady=10)
#report_button.pack()

# Start the UI
window.mainloop()
