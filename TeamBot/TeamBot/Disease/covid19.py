from django import forms

class CovidDiseaseForm(forms.Form):
    test_date = forms.DateField(label='Test Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    cough = forms.BooleanField(label='Do you have a cough?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fever = forms.BooleanField(label='Do you have a fever?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    sore_throat = forms.BooleanField(label='Do you have a sore throat?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    shortness_of_breath = forms.BooleanField(label='Do you have shortness of breath?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    head_ache = forms.BooleanField(label='Do you have a headache?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    corona_result = forms.TypedChoiceField(label='Corona Test Result', choices=[('Positive', 'Positive'), ('Negative', 'Negative')], widget=forms.Select(attrs={'class': 'form-control'}))
    age_60_and_above = forms.TypedChoiceField(label='Age 60 or Above', choices=[('Yes', 'Yes'), ('No', 'No')], widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.TypedChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    test_indication = forms.TypedChoiceField(label='Test Indication', choices=[('Abroad', 'Abroad'), ('Contact with confirmed', 'Contact with confirmed'), ('Other', 'Other')], widget=forms.Select(attrs={'class': 'form-control'}))
