from django import forms
BG=(
    ('O+','O+'),
    ('O-','O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)
Disease=(
    ('Fever','Fever'),
    ('Cough','Cough'),
    ('Headache','Headache'),
    ('Diarrhea','Diarrhea'),
    ('Vomiting','Vomiting'),
    ('Sore Throat','Sore Throat'),
    ('Nausea','Nausea'),
    ('Diabetes','Diabetes'),
    ('Hypertension','Hypertension'),
    ('Heart Disease','Heart Disease'),
    ('Lung Disease','Lung Disease'),
    ('Kidney Disease','Kidney Disease'),
    ('Asthma','Asthma'),
    ('Pneumonia','Pneumonia'),
    ('Tuberculosis','Tuberculosis'),
    ('Liver Disease','Liver Disease'),
    ('Hepatitis B','Hepatitis B')    
)
gender=(
    ('Male','Male'),
    ('Female','Female'),
)
class appoinment_form(forms.Form):
    Blood_group=forms.ChoiceField(label='Blood_group',choices=BG)
    Gender=forms.ChoiceField(label='Gender',choices=gender)
    Disease=forms.ChoiceField(label='Disease',choices=Disease)