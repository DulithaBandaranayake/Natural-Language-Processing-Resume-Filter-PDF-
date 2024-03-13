# Natural Language Processing Resume Filter

## Project Overview

Welcome to the Natural Language Processing (NLP) Resume Filter Python project! This project aims to streamline the job application process by leveraging NLP techniques to match resumes with job descriptions. The system provides a percentage score indicating how closely a candidate's resume aligns with a given job description.

## Features

1. **Resume Parsing**: The system extracts relevant information from resumes, including skills, experience, and education details.

2. **Job Description Analysis**: Utilizes NLP algorithms to analyze and understand the key requirements and qualifications specified in the job description.

3. **Matching Algorithm**: Employs a sophisticated matching algorithm to assess the similarity between the candidate's resume and the job description.

4. **Percentage Matching**: Generates a percentage score that represents the degree of alignment between the resume and the job description.

5. **User-Friendly Interface**: Provides an easy-to-use interface for users to input their resumes and job descriptions, view the matching score, and receive feedback.

## Getting Started

1. **Prerequisites**: Ensure that you have Python installed on your system. You can install the required libraries by running:
   
   - PDFMiner
    ```bash
    pip install pdfminer
    ```
   - scikit-learn
   
   Windows, macOS
   ```bash
   pip install -U scikit-learn
   ```
   Linux
   ```bash
   pip3 install -U scikit-learn
   ```
   Conda
   ```bash
   conda create -n sklearn-env -c conda-forge scikit-learn
   conda activate sklearn-env
   ```
   
2. **Input Resume and Job Description**: Enter the path to your resume file and the job description. The system will process the input and display the matching percentage.

3. **Interpret Results**: A higher percentage indicates a stronger match between your resume and the job description.

## Technologies Used

- Python
- Natural Language Processing (NLP) libraries (scikit-learn)
- Resume parsing libraries (pdfminer)

## Future Enhancements

1. **Customizable Weighting**: Allow users to assign different weights to specific sections (e.g., skills, experience) for a more personalized matching score.

2. **Integration with Job Platforms**: Connect the system with popular job platforms to simplify the application process.

3. **Advanced Analytics**: Provide detailed analytics on areas of strength and improvement in the resume.

4. **Machine Learning Integration**: Explore the possibility of incorporating machine learning models to enhance the matching algorithm.

## Contributors

- Dulitha Bandaranayake

## License

Feel free to contribute, modify, or distribute according to the terms outlined in the license.

Thank you for using the Natural Language Processing Resume Filter Python project! If you have any questions or feedback, please don't hesitate to reach out to me.
