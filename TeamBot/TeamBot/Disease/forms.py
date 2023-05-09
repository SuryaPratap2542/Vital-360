from  django import forms


class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}))
    sex = forms.TypedChoiceField(label='Sex', choices=[(1, 'Male'), (0, 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    cp = forms.TypedChoiceField(label='Chest Pain Type', choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anginal Pain'), (4, 'Asymptomatic')], coerce=int, widget=forms.Select(attrs={'class': 'form-control'}))
    trestbps = forms.IntegerField(label='Resting Blood Pressure', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Resting Blood Pressure'}))
    chol = forms.IntegerField(label='Serum Cholesterol', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serum Cholesterol'}))
    fbs = forms.TypedChoiceField(label='Fasting Blood Sugar', choices=[(1, 'Greater Than 120mg/dl'), (0, 'Less Than or Equal to 120mg/dl')], widget=forms.Select(attrs={'class': 'form-control'}))
    restecg = forms.TypedChoiceField(label='Resting Electrocardiography Results', choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Left Ventricular Hypertrophy')], coerce=int, widget=forms.Select(attrs={'class': 'form-control'}))
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Maximum Heart Rate Achieved'}))
    exang = forms.TypedChoiceField(label='Exercise Induced Angina', choices=[(1, 'Yes'), (0, 'No')], widget=forms.Select(attrs={'class': 'form-control'}))
    oldpeak = forms.FloatField(label='ST Depression Induced by Exercise', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter ST Depression Induced by Exercise'}))
    slope = forms.TypedChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(1, 'Up Sloping'), (2, 'Flat'), (3, 'Down Sloping')], coerce=int, widget=forms.Select(attrs={'class': 'form-control'}))
    ca = forms.TypedChoiceField(label='Number of Major Vessels Colored by Fluoroscopy', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], coerce=int, widget=forms.Select(attrs={'class': 'form-control'}))
    thal = forms.TypedChoiceField(label='Thal', choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')], coerce=int, widget=forms.Select(attrs={'class': 'form-control'}))

#Diabetese


