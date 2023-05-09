from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from Disease.forms import  HeartDiseaseForm
# Create your views here.
#pdf
from django.http import FileResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import render_to_string


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from django.shortcuts import render
from .forms import HeartDiseaseForm

from Disease.cancer import CancerDiseaseForm
from Disease.covid19 import CovidDiseaseForm
from Disease.liver import LiverDiseaseForm


# from Disease.diabeteseform import DiabetesForm




# @login_required(login_url='login')
@login_required(login_url='login')
def Home(request):
    return render (request,'home.html')


def SignupPage(request):
    
    if request.method=='POST':
        
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        user_exist=User.objects.filter(username = uname).exists()
        email_check=User.objects.filter(email=email).exists()
   
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        
        elif user_exist==True:
            messages.error(request, "This username is already taken")
            return redirect('/')
        
        elif email_check==True:
            messages.error(request, "This email is already taken")
            return redirect('/')
        
        
        
        else:
            my_user=User.objects.create_user(username = uname,email=email,password=pass1)
        
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')
        
        
        

def LoginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

#pdf start
def download_pdfd(request):
    # Render the HTML template with the context data
    html_content = render_to_string('result.html', {})

    # Create a file-like buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)

    # If there was an error, return an error response
    if pisa_status.err:
        return HttpResponse('Error generating PDF: %s' % pisa_status.err)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='result.pdf')
def download_pdfh(request):
    # Render the HTML template with the context data
    html_content = render_to_string('heartsolution.html', {})

    # Create a file-like buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)

    # If there was an error, return an error response
    if pisa_status.err:
        return HttpResponse('Error generating PDF: %s' % pisa_status.err)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='heartsolution.pdf')
def download_pdfc(request):
    # Render the HTML template with the context data
    html_content = render_to_string('csolution.html', {})

    # Create a file-like buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)

    # If there was an error, return an error response
    if pisa_status.err:
        return HttpResponse('Error generating PDF: %s' % pisa_status.err)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='csolution.pdf')
def download_pdfco(request):
    # Render the HTML template with the context data
    html_content = render_to_string('covidsolution.html', {})

    # Create a file-like buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)

    # If there was an error, return an error response
    if pisa_status.err:
        return HttpResponse('Error generating PDF: %s' % pisa_status.err)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='covidsolution.pdf')
#PDF end

# Diabetes Start
def diabaties(request):
    return render(request, 'diabaties.html')
def result(request):
    data = pd.read_csv("static/diabetes.csv")
    X= data.drop("Outcome",axis=1) 
    Y= data["Outcome"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1= ""
    value=0
    if pred==[1]:
        value=1
        result1="Oops! You have DIABETES 😔."
    else:
        value=0
        result1="Great! You DON'T have daibetes 😁."
    if value==1:
        return render(request, "result.html", {"result2": result1})
    else:
        return render(request,"congratulations.html",{"result2": result1})


#Diabetse End Here


#Heart start Here
def heart(request):
    df = pd.read_csv('static/heart.csv')
    # Replace the rest of the old code with the new code

    # Check for missing values
    df = df.fillna(df.median())

    # Drop duplicates
    df = df.drop_duplicates()

    # Normalize the data
    scaler = StandardScaler()
    df[df.columns[:-1]] = scaler.fit_transform(df[df.columns[:-1]])

    # Split into X and y
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    value = ''
    if request.method == 'POST':

        # Get user data from form
        user_data = np.array([
            float(request.POST[field])
            for field in ('age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                          'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal')
        ]).reshape(1, 13)

        # Scale user data
        user_data = scaler.transform(user_data)

        # Make predictions
        predictions = model.predict(user_data)
        # temp=int(predictions[0])
        # if temp == 1:
        #     # Redirect to the solution page if predicted to have heart disease
        #     return redirect('solution')
        # elif temp == 0:
        #     # Redirect to the congratulations page if predicted to not have heart disease
        #     return redirect('congratulations')
        result1= ""
        val=1
        if int(predictions[0])==0:
            val=1
            result1="Oops! You have Heart Decease 😔."
        elif int(predictions[0])==1:
            val=0
            result1="Great! You DON'T have Heart Decease 😁."
        if val==1:
            return render(request, "heartsolution.html", {"result2": result1})
        else:
            return render(request,"congratulations.html",{"result2": result1})
        
    return render(request,
                  'heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': HeartDiseaseForm(),
                  })
def solution(request):
    return render(request, 'heartsolution.html')

def congratulations(request):
    return render(request, 'congratulations.html')

# Heart End Here

#Cancer start here

def cancer(request):
   
    df = pd.read_csv('static/cancer.csv')
   
    features = df.drop(['id','diagnosis'], axis = 1)
    labels = df['diagnosis']
    X=features
    Y=labels

    print(X)
    print(Y) 
 
    value = ''
 
    if request.method == 'POST':
 
        id = float(request.POST['id'])
        diagnosis = float(request.POST['diagnosis'])
        radius_mean = float(request.POST['radius_mean'])
        texture_mean = float(request.POST['texture_mean'])
        perimeter_mean= float(request.POST['perimeter_mean'])
        area_mean= float(request.POST['area_mean'])
        smoothness_mean = float(request.POST['smoothness_mean'])
        concavity_mean= float(request.POST['concavity_mean'])
        concave_points_mean= float(request.POST['concave_points_mean'])
        symmetry_mean= float(request.POST['symmetry_mean'])
        fractal_dimension_mean= float(request.POST['fractal_dimension_mean'])
        radius_se= float(request.POST['radius_se'])
        texture_se = float(request.POST['texture_se'])
        perimeter_se=float(request.POST['perimeter_se'])
        area_se=float(request.POST['area_se'])
        smoothness_se=float(request.POST['smoothness_se'])
        compactness_se=float(request.POST['compactness_se'])
        concavity_se=float(request.POST['concavity_se'])
        concave_points_se=float(request.POST['concave_points_se'])
        symmetry_se=float(request.POST['symmetry_se'])
        fractal_dimension_se=float(request.POST['fractal_dimension_se'])
        radius_worst=float(request.POST['radius_worst'])
        texture_worst=float(request.POST['texture_worst'])
        perimeter_worst=float(request.POST['perimeter_worst'])
        area_worst=float(request.POST['area_worst'])
        smoothness_worst=float(request.POST['smoothness_worst'])
        compactness_worst=float(request.POST['compactness_worst'])
        concavity_worst=float(request.POST['concavity_worst'])
        concave_points_worst=float(request.POST['concave_points_worst'])
        symmetry_worst=float(request.POST['symmetry_worst'])
        fractal_dimension_worst=float(request.POST['fractal_dimension_worst'])

 
        # user_data = np.array(
        #     (id,diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,
        #      perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst
        #      ,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst)
        # ).reshape(1, 31)

        user_data = np.array(
            (radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,
            perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst
            ,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst, 0)
        ).reshape(1, 30)

        print(user_data)

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)
        # print(int(float(predictions[0])))
        # if int(float(predictions[0])) == 1:
        #     # Redirect to the solution page if predicted to have heart disease
        #     return redirect('cansolution')
        # elif int(float(predictions[0])) == 0:
        #     # Redirect to the congratulations page if predicted to not have heart disease
        #     return redirect('cancongratulations')
        result1= ""
        val=1
        if int(float(predictions[0]))==1:
            val=1
            result1="Oops! You have Cancer 😔."
        elif int(float(predictions[0]))==0:
            val=0
            result1="Great! You DON'T have Cancer 😁."
        if val==1:
            return render(request, "csolution.html", {"result2": result1})
        else:
            return render(request,"congratulations.html",{"result2": result1})
    

    return render(request,
                  'cancer.html',
                  {
                      'context': value,
                      'title': 'Cancer Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': CancerDiseaseForm(),
                  })
# def cansolution(request):
#     return render(request, 'csolution.html')

# def cancongratulations(request):
#     return render(request, 'congratulations.html')

#Cancer end here

#Covid19 Start Here
def covid19(request):
    return render(request,'covidsolution.html')
def covid1(request):
    df = pd.read_csv('static/covid19.csv')

    # Convert non-numeric columns to numeric data types
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col], errors='coerce')
      
    # Get X and Y values in a dataframe
    df_clean = df.dropna()

# Get X and Y values in a dataframe
    X = df_clean.drop('corona_result', axis=1)
    Y = df_clean['corona_result']
    print(X)
    print(Y)

    value = ''

    if request.method == 'POST':
        # Get form data
        cough = True if request.POST.get('cough') == 'True' else False
        fever = True if request.POST.get('fever') == 'True' else False
        sore_throat = True if request.POST.get('sore_throat') == 'True' else False
        shortness_of_breath = True if request.POST.get('shortness_of_breath') == 'True' else False
        head_ache = True if request.POST.get('head_ache') == 'True' else False
        corona_result = request.POST['corona_result']
        age_60_and_above = True if request.POST.get('age_60_and_above') == 'True' else False
        gender = request.POST['gender']
        test_indication = request.POST['test_indication']

        # Create a numpy array with the form data
        user_data = np.array((cough, fever, sore_throat, shortness_of_breath, head_ache, corona_result,
                              age_60_and_above, gender, test_indication)).reshape(1, 9)

        print(user_data)

        # Create and fit the random forest classifier
        rf = RandomForestClassifier(n_estimators=16, criterion='entropy', max_depth=9)
        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)

        # Make a prediction using the user's data
        predictions = rf.predict(user_data)
        result1= ""
        val=1
        if int(float(predictions[0]))==0:
            val=1
            result1="Oops! You have Heart Decease 😔."
        elif int(float(predictions[0]))==1:
            val=0
            result1="Great! You DON'T have Heart Decease 😁."
        if val==1:
            return render(request, "covidsolution.html", {"result2": result1})
        else:
            return render(request,"congratulations.html",{"result2": result1})

    return render(request,
                  'covid19.html',
                  {
                      'context': value,
                      'title': 'COVID-19 Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': CovidDiseaseForm(),
                  })

#Covid19 End Here

#Leve start here
def liver(request):
   
    df = pd.read_csv('static/liver.csv')
    # print(df.head())
    # print(df.shape)
    # print(df.info())
    # print(df.describe())
    # print(df.isnull().sum())
    # print(df['target'].value_counts())

    #how to get X and Y values in a dataframe
    X = df.drop('Result', axis=1)
    #df.drop how it works?
    # df.drop is a function that we use to drop a column or row
    # in this case, we want to drop the column that we want to predict
    # so we use df.drop('target', axis=1)
    #drop('target') means that we want to drop the column named 'target'
    #axis=1 means that we want to drop a column
    #axis=0 means that we want to drop a row
    #so df.drop('target', axis=1) means that we want to drop a column named 'target'

    Y = df['Result']
    #X = df.drop('target', axis=1)
    
    #df.drop how it works?
    # df.drop is a function that we use to drop a column or row
    # in this case, we want to drop the column that we want to predict
    # so we use df.drop('target', axis=1)
    #drop('target') means that we want to drop the column named 'target'
    #axis=1 means that we want to drop a column
    #axis=0 means that we want to drop a row
    #so df.drop('target', axis=1) means that we want to drop a column named 'target'

    #Y = df['target']
    #what is target and axis=1 means?
    # target is the column that we want to drop
    # axis=1 means that we want to drop a column    
    # drowp the column that we want to predict



    # data = df.values
    # X = data[:, :-1]
    # Y = data[:, -1:]


    #eassy way to get X and Y
    # X = df.drop('target', axis=1)
  

    # Y = df['target']


# what is X and Y?
# X is the data that we will use to predict Y
# Y is the data that we want to predict
# in this case, we want to predict if a person has heart disease or not
# so we will use the data in X to predict if a person has heart disease or not
# and the data in Y is the result of the prediction

    print(X)
    print(Y) 
 
    value = ''
 
    if request.method == 'POST':
        Age=float(request.POST['Age'])
        Gender=float(request.POST['Gender'])
        Total_Bilirubin=float(request.POST['Total_Bilirubin'])
        Direct_Bilirubin=float(request.POST['Direct_Bilirubin'])
        Alkphos_Alkaline_Phosphotase=float(request.POST['Alkphos_Alkaline_Phosphotase'])
        Alamine_Aminotransferase=float(request.POST['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase=float(request.POST['Aspartate_Aminotransferase'])
        Total_Protiens=float(request.POST['Total_Protiens'])
        Albumin=float(request.POST['Albumin'])
        Ratio_Albumin_Globulin=float(request.POST['Ratio_Albumin_Globulin'])
        Result=float(request.POST['Result'])
        
 
        # user_data = np.array(
        #     (id,diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,
        #      perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst
        #      ,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst)
        # ).reshape(1, 31)

        user_data = np.array(
        (Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkphos_Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
         Total_Protiens,Albumin,Ratio_Albumin_Globulin)
).reshape(1,10 )

        print(user_data)
 
        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )
       
        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)
        temp=0
        result1=""
        if int(predictions[0])== 1:
            temp=1
            result1="Oops! You have Lever Problem 😔."
        elif int(predictions[0]) == 0:
            temp=0
            result1="Great! You DON'T have Any Lever Decease 😁."
        if temp==1:
            return render(request, "lsolution.html", {"result2": result1})
        else:
            return render(request,"congratulations.html",{"result2": result1})



    return render(request,
                  'liver.html',
                  {
                      'context': value,
                      'title': 'liver Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': LiverDiseaseForm(),
                  })
#Leve end here
