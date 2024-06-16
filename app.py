from flask import Flask, request, render_template
from PyPDF2 import PdfReader
import re
import pickle

app = Flask(__name__)
# Load models===========================================================================================================
rf_classifier_categorization = pickle.load(open('models/rf_classifier.pkl', 'rb'))
tfidf_vectorizer_categorization = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
rf_classifier_job_recommendation = pickle.load(open('models/rf_classifier_job_recommendation.pkl', 'rb'))
tfidf_vectorizer_job_recommendation = pickle.load(open('models/tfidf_vectorizer_job_recommendation.pkl', 'rb'))

# routes===============================================

@app.route('/')
def resume():
    # Provide a simple UI to upload a resume
    return render_template("resume.html")

@app.route('/pred', methods=['POST'])
def pred():
    # Process the PDF or TXT file and make prediction
    if 'resume' in request.files:
        file = request.files['resume']
        filename = file.filename
        if filename.endswith('.pdf'):
            text = pdf_to_text(file)
        elif filename.endswith('.txt'):
            text = file.read().decode('utf-8')
        else:
            return render_template('resume.html', message="Invalid file format. Please upload a PDF or TXT file.")

        predicted_category = predict_category(text)
        recommended_job = job_recommendation(text)
        phone = extract_contact_number_from_resume(text)
        email = extract_email_from_resume(text)

        extracted_skills = extract_skills_from_resume(text)
        extracted_education = extract_education_from_resume(text)
        name = extract_name_from_resume(text)

        return render_template('resume.html', predicted_category=predicted_category,recommended_job=recommended_job,
                               phone=phone,name=name,email=email,extracted_skills=extracted_skills,extracted_education=extracted_education)
    else:
        return render_template("resume.html", message="No resume file uploaded.")

if __name__ == '__main__':
    app.run(debug=True)