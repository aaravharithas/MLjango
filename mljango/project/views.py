from django.shortcuts import render
from django.http import HttpResponseRedirect
from projectCard.models import Project
from django.contrib import messages
from joblib import load
from django.conf import settings
import os



# Machine Learning Project Fuction Template

'''

def ProjctName_ProjectCode(request):
    project_code = 'ML001'
    project_template = 'project_detail.html' # project_template is html form page
    project = Project.objects.get(pk=project_code) # projectCard_pk value for title and discription
    
    savedModel_name = 'iris_model.joblib' # savedModel name 
    model = load('./savedModels/'+ savedModel_name) 

    # handle code form here
    if request.method == 'POST':     # input field variable name   
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        values = [[sepal_length, sepal_width, petal_length, petal_width]]
        y_pred = model.predict(values)[0] # prediction value
        
        # for giving the classification label for result from prediction
        if y_pred == 0: 
            result = "Setosa"
        elif y_pred == 1:
            result = "Versicolor"
        else:
            result = "Virginica"
        # handle code area end
        
        messages.success(request,f'your result is: {result}')
        messages.success(request,f'for values : {values[0]} respectively.')
        for i in range(len(labels)):
            messages.success(request,f'pridiction probabilty {round(model.predict_proba(values)[0,i]*100,2)}% for {labels[i]}.')
        # message.success provides the value to html template only once. Removed after reload.
        return HttpResponseRedirect(project_code)
    return render(request, project_template, context = {'project' : project}) 
    
    '''


# Create your views here.


# iris flower classification
def iris_ML001(request):
    project_code = 'ML001'
    project_template = 'iris_ML001.html' # project_template is html form page
    project = Project.objects.get(pk=project_code) # projectCard_pk value for title and discription

    savedModel_name = 'iris_model.joblib' # savedModel name
    # model = load('./savedModels/'+ savedModel_name)
    model = load(os.path.join(settings.FILES_DIR, savedModel_name))
    if request.method == 'POST':     # input field variable name   
        
        input_label = ['sepal_length','sepal_width','petal_length','petal_width']
        input_list = []
        for label in input_label:
            input_list.append(request.POST[label])
        values = [input_list]

        y_pred = model.predict(values)[0]
        labels = ['Setosa', 'Versicolor', 'Virginica']
        result = labels[y_pred]

        messages.success(request,f'your result is: {result}.')
        messages.success(request,f'for values : {values[0]} respectively.')
        for i in range(len(labels)):
            messages.success(request,f'pridiction probabilty {round(model.predict_proba(values)[0,i]*100,2)}% for {labels[i]}.')
        # message.success provides the value to html template only once. Removed after reload.
        return HttpResponseRedirect(project_code)
        # return render(request,'project_detail.html',context) it re-submits the form upon reload. So, avoid it.
    return render(request, project_template, context = {'project':project,'title':savedModel_name.split('.')[0]})

# emotion analysis

def emotion_ML002(request):
    # model based fuction
    def preprocess_text(text):
    # Lowercase the text
        text = text.lower()
        # Remove non-alphanumeric characters
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        return text
     # Import necessary libraries
    import pandas as pd

    project_code = 'ML002'
    project_template = 'emotion_ML002.html' # project_template is html form page
    project = Project.objects.get(pk=project_code) # projectCard_pk value for title and discription
    # vectorizer = load('./savedModels/emotion_vectorizer.joblib')
    vectorizer = load(os.path.join(settings.FILES_DIR, 'emotion_vectorizer.joblib'))
    savedModel_name = 'emotion_analysis.joblib' # savedModel name 
    # model = load('./savedModels/'+ savedModel_name)
    model = load(os.path.join(settings.FILES_DIR, savedModel_name)) 

    # handle code form here
    if request.method == 'POST':     # input field variable name   
        emotion_text = request.POST['emotion_text']
        value = preprocess_text(emotion_text)
        value = vectorizer.transform([value])
        y_pred = model.predict(pd.Series([value])[0])[0] # prediction value
        labels = ['Sad','Happy','Love','Anger','Fear','Surprised']
        # for giving the classification label for result from prediction
        # handle code area end
        result = labels[y_pred]
        messages.success(request,f'your result is: {result}')
        messages.success(request,f'for text : {emotion_text}')
        for i in range(len(labels)):
            messages.success(request,f'pridiction probabilty {round(model.predict_proba(pd.Series([value])[0])[0,i]*100,2)}% for {labels[i]}.')
        # message.success provides the value to html template only once. Removed after reload.
        return HttpResponseRedirect(project_code)
    return render(request, project_template, context = {'project' : project}) 



def cardio_ML003(request):
    project_code = 'ML003'
    project_template = 'cardio_ML003.html' # project_template is html form page
    project = Project.objects.get(pk=project_code) # projectCard_pk value for title and discription
    
    savedModel_name = 'cardio_predict.joblib' # savedModel name 
    # model = load('./savedModels/'+ savedModel_name) 
    model = load(os.path.join(settings.FILES_DIR, savedModel_name))

    # handle code form here
    if request.method == 'POST':     # input field variable name   
        input_label = ['age', 'gender', 'height', 'weight', 'systole_hi', 'diastole_lo',
       'cholesterol', 'gluc', 'smoke', 'alco', 'active']
        input_list = []
        for label in input_label:
            input_list.append(request.POST[label])
        values = [input_list]
        y_pred = model.predict(values)[0] # prediction value
        # handle code area end
        labels = ['Chance of not having Cardiovascular Disease','Chance of Cardiovascular Disease']

        # messages.success(request,f'Your values : {values[0]} respectively.')
        for i in range(len(labels)):
            messages.success(request,f'{labels[i]}: {round(model.predict_proba(values)[0,i]*100,2)}%')
        # message.success provides the value to html template only once. Removed after reload.
        return HttpResponseRedirect(project_code)
    return render(request, project_template, context = {'project' : project}) 
