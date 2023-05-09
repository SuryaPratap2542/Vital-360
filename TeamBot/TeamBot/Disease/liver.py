from django import forms
from django.db import models

class LiverDiseaseForm(forms.Form):
    Age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age of the patient'}))
    Gender = forms.TypedChoiceField(label='Gender', choices=[(1, 'M'), (0, 'F')], coerce=int, widget=forms.Select(attrs={'class': 'form-control' ,'placeholder':'Gender of the patient'}))
    Total_Bilirubin = forms.IntegerField(label='Total_Bilirubin', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the total Bilirubin'}))
    Direct_Bilirubin = forms.IntegerField(label='Direct_Bilirubin', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Direct Bilirubin'}))
    Alkphos_Alkaline_Phosphotase = forms.IntegerField(label='Alkphos_Alkaline_Phosphotase', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Alkphos Alkaline Phosphotase '}))
    Alamine_Aminotransferase = forms.TypedChoiceField(label='Alamine_Aminotransferase', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Sgpt_Alamine_Aminotransferase'}))
    Aspartate_Aminotransferase = forms.TypedChoiceField(label='Aspartate_Aminotransferase', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Aspartate_Aminotransferase'}))
    Total_Protiens = forms.IntegerField(label='Total_Protiens', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the total protiens'}))
    Albumin= forms.IntegerField(label='Albumin', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the ALB_Albumin '}))
    Ratio_Albumin_Globulin= forms.IntegerField(label='A/G_Ratio_Albumin', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the A/G Ratio Albumin  and Globulin'}))
   
    Result= forms.IntegerField(label='Result', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Result '}))
  

    
