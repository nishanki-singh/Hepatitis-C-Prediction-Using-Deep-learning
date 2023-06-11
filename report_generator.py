from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph

def generate_patient_report():
    # Prompt the user to input patient information
    patient_info = {}
    print("Enter Patient Information:")
    patient_info["Name"] = input("Name: ")
    patient_info["Age"] = input("Age: ")
    patient_info["Gender"] = input("Gender: ")

    # Prompt the user to input laboratory results
    lab_results = {}
    print("\nEnter Laboratory Results:")
    lab_results["ALB (Albumin)"] = float(input("ALB (Albumin) (g/dL): "))
    lab_results["AST (Aspartate Aminotransferase)"] = float(input("AST (Aspartate Aminotransferase) (U/L): "))
    lab_results["BIL (Bilirubin)"] = float(input("BIL (Bilirubin) (mg/dL): "))
    lab_results["CHE (Cholinesterase)"] = float(input("CHE (Cholinesterase) (U/L): "))
    lab_results["CHOL (Cholesterol)"] = float(input("CHOL (Cholesterol) (mg/dL): "))
    lab_results["GGT (Gamma-Glutamyl Transferase)"] = float(input("GGT (Gamma-Glutamyl Transferase) (U/L): "))

    # Create a new PDF file
    c = canvas.Canvas("patient_report.pdf", pagesize=letter)

    # Set the font size and position for writing text
    c.setFont("Helvetica", 12)
    x = 50
    y = 700

    # Write the patient information to the PDF
    c.drawString(x, y, "Patient Report for Hepatitis C")
    y -= 20
    for key, value in patient_info.items():
        c.drawString(x, y, "- {}: {}".format(key, value))
        y -= 20

    # Write the laboratory results to the PDF
    c.drawString(x, y, "\nLaboratory Results:")
    y -= 20
    for key, value in lab_results.items():
        c.drawString(x, y, "- {}: {}".format(key, value))
        y -= 20

    # Perform analysis and write interpretation for each parameter
    c.drawString(x, y, "\nAnalysis:")
    y -= 20
    for key, value in lab_results.items():
        c.drawString(x, y, key)
        y -= 20

        normal_range = ""
        interpretation = ""

        if key == "ALB (Albumin)":
            normal_range = "3.5 - 5.5 g/dL"
            if 3.5 <= value <= 5.5:
                interpretation = "The patient's albumin levels are within the normal range, indicating normal liver function."
            else:
                interpretation = "The patient's albumin levels are outside the normal range."

        elif key == "AST (Aspartate Aminotransferase)":
            normal_range = "10 - 40 U/L"
            if 10 <= value <= 40:
                interpretation = "The patient's AST levels are within the normal range, suggesting normal liver function."
            else:
                interpretation = "The patient's AST levels are outside the normal range."

        elif key == "BIL (Bilirubin)":
            normal_range = "0.2 - 1.2 mg/dL"
            if 0.2 <= value <= 1.2:
                interpretation = "The patient's bilirubin levels are within the normal range, indicating normal liver function."
            else:
                interpretation = "The patient's bilirubin levels are outside the normal range."

        elif key == "CHE (Cholinesterase)":
            normal_range = "2500 - 12500 U/L"
            if 2500 <= value <= 12500:
                interpretation = "The patient's cholinesterase levels are within the normal range, indicating normal liver function."
            else:
                interpretation = "The patient's cholinesterase levels are outside the normal range."

        elif key == "CHOL (Cholesterol)":
            normal_range = "<200 mg/dL"
            if value < 200:
                interpretation = "The patient's cholesterol levels are within the normal range."
            else:
                interpretation = "The patient's cholesterol levels are outside the normal range."

        elif key == "GGT (Gamma-Glutamyl Transferase)":
            normal_range = "9 - 48 U/L (males), 9 - 36 U/L (females)"
            if patient_info["Gender"].lower() == "male":
                if 9 <= value <= 48:
                    interpretation = "The patient's GGT levels are within the normal range, indicating normal liver function."
                else:
                    interpretation = "The patient's GGT levels are outside the normal range."
            elif patient_info["Gender"].lower() == "female":
                if 9 <= value <= 36:
                    interpretation = "The patient's GGT levels are within the normal range, indicating normal liver function."
                else:
                    interpretation = "The patient's GGT levels are outside the normal range."

        # Write the parameter's normal range, result, and interpretation to the PDF
        c.drawString(x + inch, y, "- Normal Range: {}".format(normal_range))
        y -= 20
        c.drawString(x + inch, y, "- Result: {}".format(value))
        y -= 20
        c.drawString(x + inch, y, "- Interpretation: {}".format(interpretation))
        y -= 20

    # Save and close the PDF
    c.save()

    print("Patient report generated and saved to patient_report.pdf")

# Generate patient report based on user input
if __name__ == '__main__':
    generate_patient_report()
