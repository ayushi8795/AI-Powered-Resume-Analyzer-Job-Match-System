import spacy 
nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = ['Python', 'Django', 'REST', 'SQL', 'Machine Learning', 'AI', 'NLP', 'Java', 'C++', 'AWS']
EDUCATION_KEYWORDS = ['Bachelor', 'Master', 'B.Tech', 'M.Tech', 'PhD', 'University', 'College',"MS", "MSc", "BSc", "Bachelors", "Masters"]
EXPERIENCE_KEYWORDS = ['experience', 'worked at', 'internship', 'developed', 'managed', 'led']

def parse_resume(text):
    doc = nlp(text)
    skills = [word for word in SKILL_KEYWORDS if word.lower() in text.lower()]
    education = [sent.text for sent in doc.sents if any(edu in sent.text for edu in EDUCATION_KEYWORDS)]
    experience = [sent.text for sent in doc.sents if any(exp in sent.text.lower() for exp in EXPERIENCE_KEYWORDS)]
    return {
        'skills': ','.join(skills),
        'education':'|'.join(education),
        'experience': '|'.join(experience)
    }