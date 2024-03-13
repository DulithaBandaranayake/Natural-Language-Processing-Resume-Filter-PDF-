from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Insert Resume Path
resume_path = 'Web-Developer-resume.pdf'

#Insert Job Description
file = open('jobdescription.txt', 'r')
job_description = file.read()
file.close()

pdf_resume = extract_text(resume_path)

content = [job_description,pdf_resume]

#Calculate Comparison Percentage
resume = CountVectorizer()
matrix = resume.fit_transform(content)

similarity_matrix = cosine_similarity(matrix)

print(str(similarity_matrix[1][0]*100)) #Output Look Like - 30.021547
