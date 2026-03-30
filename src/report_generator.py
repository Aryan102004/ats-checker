from fpdf import FPDF


def generate_pdf(score, matched_skills, missing_skills):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="ATS Resume Report", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"ATS Match Score: {score}%", ln=True)

    pdf.ln(5)

    pdf.cell(200, 10, txt="Matched Skills:", ln=True)
    pdf.multi_cell(0, 10, ", ".join(matched_skills) if matched_skills else "None")

    pdf.ln(5)

    pdf.cell(200, 10, txt="Missing Skills:", ln=True)
    pdf.multi_cell(0, 10, ", ".join(missing_skills) if missing_skills else "None")

    pdf.ln(5)

    pdf.cell(200, 10, txt="Suggestions:", ln=True)
    if missing_skills:
        pdf.multi_cell(
            0,
            10,
            "Add these missing skills naturally in your resume: "
            + ", ".join(missing_skills[:5])
        )
    else:
        pdf.multi_cell(0, 10, "Your resume matches the job description well!")

    file_path = "ATS_Report.pdf"
    pdf.output(file_path)

    return file_path
