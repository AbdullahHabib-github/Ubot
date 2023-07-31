import json
import os

def remove_common_sentence(jsonl_file, common_sentence):
    output_lines = []

    with open(jsonl_file, 'r') as file:
        for line in file:
            data = json.loads(line.strip())
            if "page_content" in data:
                text = data["page_content"]
                updated_text = text.replace(common_sentence, ".").strip()
                data["page_content"] = updated_text
            output_lines.append(json.dumps(data))

    # Writing back to the same file or a new one
    output_file = f"{os.path.splitext(jsonl_file)[0]}.jsonl"
    with open(output_file, 'w') as file:
        file.write("\n".join(output_lines))


def truncate_at_end (jsonl_file, pattern):
    output_lines = []

    with open(jsonl_file, 'r') as file:
        for line in file:
            data = json.loads(line.strip())
            if "page_content" in data:
                text = data["page_content"]
                index = text.find(pattern)
                if index != -1:  # Pattern found in the line
                     data["page_content"] = text[:index-18]+"."  # Truncate the line up to the pattern
            output_lines.append(json.dumps(data))



       # Writing back to the same file or a new one
    output_file = f"{os.path.splitext(jsonl_file)[0]}.jsonl"
    with open(output_file, 'w') as file:
        file.write("\n".join(output_lines))


if __name__ == "__main__":
    jsonl_file_path = "/content/data.jsonl"
    common_sentence_to_remove = "- Ghulam Ishaq Khan Institute of Engineering Sciences and Technology - GIKI                         Scholarships Undergraduate Scholarships Graduate Scholarship Subscribe to Admission Alerts  Alumni QEC & Accreditation ORIC Careers SOPREST Tenders & Notices Contact Us Newsletters Newsletter | Fall 2022 SDGIKI | Newsletter Newsletter | Spring 2022 Newsletter | Fall 2021  Annual Report Annual Report 2022 Annual Report 2021  IT Department IT Helpdesk IT Department   HOME VISION & MISSION ABOUT GIK Overview Board of Governors Chancellor’s Message President’s Message Rector’s Message  ACADEMICS Information Overview Academic Policy Academic Calendar Library Student Affairs Office of Admission & Examination Quality Enhancement Cell ORIC  Faculties Electrical Engineering Computer Sciences and Engineering Engineering Sciences Mechanical Engineering Material Science & Chemical Engineering Department of Civil Engineering School of Management Sciences   Apply for UG Admissions ADMISSIONS Undergraduate Admissions Apply for Undergraduate Admissions 2023 Undergraduate Scholarships Graduate Admissions Graduate Scholarship  ADMINISTRATION CAMPUS LIFEScholarships Undergraduate Scholarships Graduate Scholarship Subscribe to Admission Alerts  Alumni QEC & Accreditation ORIC Careers SOPREST Tenders & Notices Contact Us Newsletters Newsletter | Fall 2022 SDGIKI | Newsletter Newsletter | Spring 2022 Newsletter | Fall 2021  Annual Report Annual Report 2022 Annual Report 2021  IT Department IT Helpdesk IT Department HOME VISION & MISSION ABOUT GIK Overview Board of Governors Chancellor’s Message President’s Message Rector’s Message  ACADEMICS Information Overview Academic Policy Academic Calendar Library Student Affairs Office of Admission & Examination Quality Enhancement Cell ORIC  Faculties Electrical Engineering Computer Sciences and Engineering Engineering Sciences Mechanical Engineering Material Science & Chemical Engineering Department of Civil Engineering School of Management Sciences  Apply for UG Admissions ADMISSIONS Undergraduate Admissions Apply for Undergraduate Admissions 2023 Undergraduate Scholarships Graduate Admissions Graduate Scholarship  ADMINISTRATION CAMPUS LIFE  HOME VISION & MISSION ABOUT GIK Overview Board of Governors Chancellor’s Message President’s Message Rector’s Message  ACADEMICS Information Overview Academic Policy Academic Calendar Library Student Affairs Office of Admission & Examination Quality Enhancement Cell ORIC  Faculties Electrical Engineering Computer Sciences and Engineering Engineering Sciences Mechanical Engineering Material Science & Chemical Engineering Department of Civil Engineering School of Management Sciences   Apply for UG Admissions ADMISSIONS Undergraduate Admissions Apply for Undergraduate Admissions 2023 Undergraduate Scholarships Graduate Admissions Graduate Scholarship  ADMINISTRATION CAMPUS LIFE"
    remove_common_sentence(jsonl_file_path, common_sentence_to_remove)

    common_sentence_to_remove ="PrevAdmissions 2023Register for GIKI Open Day FAQs \u2013 Frequently Asked Questions Apply for Undergraduate Admissions 2023 UG Prospectus 2022 How To Apply Eligibility and Assessment Criteria Fees and Expenses Aid & Scholarships Undergraduate Admission Test Syllabus Transfer from other Universities How to pay the Application Processing Fee?StudentsStudent Handbook Academic Calendar Academic Policy Order A  Transcript Internships Industrial Open HouseQuick LinksApply for Undergraduate Admissions 2023 Undergraduate Admissions Graduate Admissions The Catalyst GIK Incubator Convocation Alumni Reunion Student Clearance Transport GIKIAccreditation\u00a0 \u00a0   Topi 23460, Khyber Pakhtunkhwa, Pakistan. T: (0938) 281026 FAX: (098) 281032\u00a0 Copyright All Rights Reserved 2023, GIK Institute of Engineering Sciences and Technology     WhatsApp us"
    truncate_at_end(jsonl_file_path, " 2023Register for GIKI Open Day FAQs \u2013 Frequently Asked Questions Apply")
