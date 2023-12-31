import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Helper_Functions:
    def __init__(self):
        self.diseases = True
        self.drugs = True
        self.supplements = True
        self.symptoms = True

        self.mayo = True
        self.webmd = True

        self.number = 5

        self.df = pd.read_csv("full_data.csv")
    
    def customize_refresh(self):
        self.df = pd.read_csv("full_data.csv")
    
    def customize_disease(self, state):
        self.diseases = state
        if state == False:
            self.df = self.df[self.df['type'] != 'disease']
        
    def customize_drugs(self, state):
        self.drugs = state
        if state == False:
            self.df = self.df[self.df['type'] != 'drug']

    def customize_supplements(self, state):
        self.supplements = state 
        if state == False:
            self.df = self.df[self.df['type'] != 'supplement']

    def customize_symptoms(self, state):
        self.symptoms = state
        if state == False:
            self.df = self.df[self.df['type'] != 'symptom']

    def customize_mayo(self, state):
        self.mayo = state
        if state == False:
            self.df = self.df[self.df['website'] != 'Mayo Clinic']
        
    def customize_webmd(self, state):
        self.webmd = state
        if state == False:
            self.df = self.df[self.df['website'] != 'Webmd']

    def customize_number(self, number):
        self.number = number

    def cosine_similarity_check(self, text):
        try:
            if text == "":
                text = 'Abdominal aortic aneurysm'
            vectorizer = CountVectorizer()

            text_vector = vectorizer.fit_transform([text])
            column_vector = vectorizer.transform(self.df['name'])

            cosine_sim = cosine_similarity(text_vector, column_vector)
            self.df['Cosine Similarity'] = cosine_sim[0]

            dataframe_sorted = self.df.sort_values(by='Cosine Similarity', ascending=False)

            if len(dataframe_sorted) < self.number:
                return (True, dataframe_sorted)
            else:
                return (True, dataframe_sorted[:self.number])
        except:
            return (False, None)



