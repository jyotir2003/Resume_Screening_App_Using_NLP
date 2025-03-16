# 📄 Resume Screening App Using NLP

<!-- Link to video file in Google Drive -->
[![Watch the video](images/video_thumbnail.png)](https://drive.google.com/file/d/13T4YeodVxZqgFAWjpAyij6uB0Y5UnYd6/view?usp=drive_link)

In the digital age, the recruitment process has undergone a significant transformation, thanks to advancements in machine learning and artificial intelligence. One such revolutionary application is in resume screening, where machine learning algorithms are utilized to automate and enhance the candidate selection process. In this project, we explore an end-to-end solution leveraging machine learning techniques to categorize resumes, provide job recommendations, and extract vital information seamlessly.

## The Challenge 🎯

Traditional resume screening processes are often time-consuming and prone to human bias. Sorting through numerous resumes to identify suitable candidates for a job opening can be overwhelming for recruiters. Moreover, manually extracting relevant information from resumes, such as skills, education, and contact details, adds another layer of complexity to the process.

## Our Solution 🚀

Our project offers a comprehensive solution to streamline the resume screening process using machine learning. By harnessing the power of natural language processing (NLP) techniques and classification algorithms, we automate the categorization of resumes based on predefined criteria. Additionally, our system provides personalized job recommendations to match candidates with suitable job openings, optimizing the recruitment process.

## 🔍 Overview
This application leverages Natural Language Processing (NLP) and Machine Learning techniques to automate resume screening processes. The system categorizes resumes, recommends suitable job positions, and extracts key information like contact details, skills, and education - all in a user-friendly web interface.

## 🛠️ Tech Stack

### 🔙 Backend
- **Python** 🐍: Primary programming language
- **Flask** 🌶️: Web framework for serving the application
- **PyPDF2** 📑: Library for extracting text from PDF documents
- **Regular Expressions (re)** 🔎: For pattern matching and information extraction
- **Pickle** 🥒: For serializing and deserializing ML models

### 🧠 Machine Learning
- **Scikit-learn** 🤖: For ML models (Random Forest Classifiers used for categorization and job recommendation)
- **TF-IDF Vectorization** 📊: Converting resume text to numerical features for ML processing

### 🖥️ Frontend
- **HTML/CSS** 🎨: Basic frontend interface using Flask's template rendering
- **Bootstrap** 🅱️ (implied): For responsive design and UI components

## ✨ Features

### 1️⃣ Resume Text Extraction
- Supports PDF and TXT file formats 📝
- Extracts complete text content from uploaded resumes

### 2️⃣ Resume Categorization
- Classifies resumes into predefined categories based on content analysis 🏷️
- Uses Random Forest classifier with TF-IDF vectorization

### 3️⃣ Job Recommendation
- Suggests suitable job positions based on resume content 💼
- Also utilizes Random Forest classifier with TF-IDF features

### 4️⃣ Information Extraction
- **Contact Information** 📱: Phone numbers and email addresses
- **Skills Detection** 🔧: Identifies technical and soft skills from a comprehensive predefined list
- **Education Details** 🎓: Extracts academic background from a wide range of disciplines
- **Name Extraction** 👤: Attempts to identify the candidate's name

### 5️⃣ Clean Web Interface
- Simple upload interface 📤
- Displays results in a user-friendly format 📊

## 📂 Project Structure

```
Resume_Screening_App_Using_NLP/
├── app.py                   # Main Flask application file
├── models/                  # Directory containing trained ML models
│   ├── rf_classifier_categorization.pkl
│   ├── tfidf_vectorizer_categorization.pkl
│   ├── rf_classifier_job_recommendation.pkl
│   └── tfidf_vectorizer_job_recommendation.pkl
├── templates/               # HTML templates
│   └── resume.html
├── README.md                # Project documentation
└── clean_resume_data.csv    # Training data (optional)
```

## 🚀 Setup and Installation

### 📋 Prerequisites
- Python 3.6+ 🐍
- pip (Python package installer) 📦

### 📥 Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/jyotir2003/Resume_Screening_App_Using_NLP.git
cd Resume_Screening_App_Using_NLP
```

2. Install required packages:
```bash
pip install flask PyPDF2 scikit-learn pandas numpy
```

3. Run the application:
```bash
python app.py
```

4. Access the application in your browser:
```
http://127.0.0.1:5000/
```

## 🖱️ Usage

1. Navigate to the web interface 🌐
2. Upload a resume in PDF or TXT format 📄
3. Click submit to process the resume ✅
4. View the results:
   - Predicted category 🏷️
   - Recommended job position 💼
   - Extracted contact information 📞
   - Identified skills 💡
   - Education details 🎓

## 🤖 Machine Learning Models

The application uses two primary ML models:

1. **Resume Categorization Model** 📊:
   - Random Forest classifier 🌲
   - Trained on labeled resume data 📝
   - Categorizes resumes into industry-specific groups 🏢

2. **Job Recommendation Model** 💼:
   - Random Forest classifier 🌲
   - Recommends specific job positions based on resume content 📄

Both models use TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction from resume text.

## 🧹 Data Preprocessing

Before processing through ML models, the application performs several text cleaning operations:
- Removing URLs 🔗
- Eliminating special characters #️⃣
- Cleaning social media handles @️
- Standardizing white spaces ⬜

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 🙌

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details. ⚖️

## 🙏 Acknowledgments

- Thanks to all contributors who have helped with the development of this application 👏
- Special thanks to the open source community for providing the libraries and tools used in this project 🌟
