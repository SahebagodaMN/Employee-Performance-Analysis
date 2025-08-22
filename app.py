import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import pickle
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management and flash messages
model = pickle.load(open('mlp_classifier_model.pkl', 'rb'))


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin': #changing pass & usname
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('Pmylogin.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    todict = request.form.to_dict()
    #age
    #gender
    if todict['gender'] == "Male":
        todict['gender']=1
    if todict['gender'] == 'Female':
        todict['gender']=0
    #edu_bg
    if todict['edu_bg']=='BA':
        todict['edu_bg']=0
    if todict['edu_bg']=='BCA':
        todict['edu_bg']=1
    if todict['edu_bg']=='BCOM':
        todict['edu_bg']=2
    if todict['edu_bg']=='BSC':
        todict['edu_bg']=3        
    if todict['edu_bg']=='BBA':
        todict['edu_bg']=4
    if todict['edu_bg']=='BE':
        todict['edu_bg']=5
    if todict['edu_bg']=='MBA':
        todict['edu_bg']=6
    if todict['edu_bg']=='MCA':
        todict['edu_bg']=7
    if todict['edu_bg']=='M.TECH':
        todict['edu_bg']=8
    if todict['edu_bg']=='MCOM':
        todict['edu_bg']=9
    if todict['edu_bg']=='MA':
        todict['edu_bg']=10
    #marital_stat
    if todict['marital_stat']=='Yes':
        todict['marital_stat']=1 
    if todict['marital_stat']=='No':
        todict['marital_stat']=0 
    #emp_dept
    if todict['emp_dept']=='Marketing':
        todict['emp_dept']=0    
    if todict['emp_dept']=='Finance':
        todict['emp_dept']=1 
    if todict['emp_dept']=='IT':
        todict['emp_dept']=2
    if todict['emp_dept']=='Accounting':
        todict['emp_dept']=3
    if todict['emp_dept']=='Production':
        todict['emp_dept']=4

    #Eemp_job_role
    if todict['emp_job_role']=='Software Engineer':
        todict['emp_job_role']=0
    if todict['emp_job_role']=='Network Engineer':
        todict['emp_job_role']=1
    if todict['emp_job_role']=='Cloud Engineer':
        todict['emp_job_role']=3
    if todict['emp_job_role']=='Data Adminstater':
        todict['emp_job_role']=4
    if todict['emp_job_role']=='Web Developer':
        todict['emp_job_role']=5
    if todict['emp_job_role']=='Full Stack Developer':
        todict['emp_job_role']=7
    if todict['emp_job_role']=='Backend Developer':
        todict['emp_job_role']=8
    if todict['emp_job_role']=='Fronted Developer':
        todict['emp_job_role']=9
    #BusinessTravelFrequency
    if todict['BusinessTravelFrequency']=='Non_Travel':
        todict['BusinessTravelFrequency']=0
    if todict['BusinessTravelFrequency']=='Travel_Rarely':
        todict['BusinessTravelFrequency']=1
    if todict['BusinessTravelFrequency']=='Travel_Frequently':
        todict['BusinessTravelFrequency']=2
    #DistanceFromHome
    #EmpEducationLevel
    if todict['EmpEducationLevel']=='Diploma':
        todict['EmpEducationLevel']=0
    if todict['EmpEducationLevel']=='Degree':
        todict['EmpEducationLevel']=1
    if todict['EmpEducationLevel']=='Masters':
        todict['EmpEducationLevel']=2
    if todict['EmpEducationLevel']=='PhD':
        todict['EmpEducationLevel']=3
    #EmpEnvironmentSatisfaction
    if todict['EmpEnvironmentSatisfaction']=='Low':
        todict['EmpEnvironmentSatisfaction']=0
    if todict['EmpEnvironmentSatisfaction']=='Moderate':
        todict['EmpEnvironmentSatisfaction']=1
    if todict['EmpEnvironmentSatisfaction']=='High':
        todict['EmpEnvironmentSatisfaction']=2

    #EmpHourlyRate
    #EmpJobInvolvement
    if todict['EmpJobInvolvement']=='Low':
        todict['EmpJobInvolvement']=0
    if todict['EmpJobInvolvement']=='Moderate':
        todict['EmpJobInvolvement']=1
    if todict['EmpJobInvolvement']=='High':
        todict['EmpJobInvolvement']=2
    #EmpJobLevel
    if todict['EmpJobLevel']=='Intern':
        todict['EmpJobLevel']=0
    if todict['EmpJobLevel']=='Clerk':
        todict['EmpJobLevel']=1
    if todict['EmpJobLevel']=='Associate':
        todict['EmpJobLevel']=2
    if todict['EmpJobLevel']=='Assistant Manager':
        todict['EmpJobLevel']=3
    if todict['EmpJobLevel']=='Manager':
        todict['EmpJobLevel']=4
    if todict['EmpJobLevel']=='Senior Manager':
        todict['EmpJobLevel']=5
    if todict['EmpJobLevel']=='Assistant Vice President':
        todict['EmpJobLevel']=6
    if todict['EmpJobLevel']=='Vice President':
        todict['EmpJobLevel']=7
    if todict['EmpJobLevel']=='Cheif Marketing Officer':
        todict['EmpJobLevel']=8
    if todict['EmpJobLevel']=='Cheif Executive Officer':
        todict['EmpJobLevel']=9
    #EmpJobSatisfaction
    if todict['EmpJobSatisfaction']=='Low':
        todict['EmpJobSatisfaction']=0
    if todict['EmpJobSatisfaction']=='Moderate':
        todict['EmpJobSatisfaction']=1
    if todict['EmpJobSatisfaction']=='High':
        todict['EmpJobSatisfaction']=2
    
    #NumCompaniesWorked

    #OverTime
    if todict['OverTime']=='Yes':
        todict['OverTime']=1
    if todict['OverTime']=='No':
        todict['OverTime']=0
    #EmpLastSalaryHikePercent
    #EmpRelationshipSatisfaction
    if todict['EmpRelationshipSatisfaction']=='Low':
        todict['EmpRelationshipSatisfaction']=0
    if todict['EmpRelationshipSatisfaction']=='Moderate':
        todict['EmpRelationshipSatisfaction']=1
    if todict['EmpRelationshipSatisfaction']=='High':
        todict['EmpRelationshipSatisfaction']=2
    #TotalWorkExperienceInYears
    #TrainingTimesLastYear

    #EmpWorkLifeBalance
    if todict['EmpWorkLifeBalance']=='Low':
        todict['EmpWorkLifeBalance']=0
    if todict['EmpWorkLifeBalance']=='Moderate':
        todict['EmpWorkLifeBalance']=1
    if todict['EmpWorkLifeBalance']=='High':
        todict['EmpWorkLifeBalance']=2
    #ExperienceYearsAtThisCompany
    #ExperienceYearsInCurrentRole
    #YearsWithCurrManager
    #Attrition
    if todict['Attrition']=='Yes':
        todict['Attrition']=1
    if todict['Attrition']=='No':
        todict['Attrition']=0
        

    int_features = [int(x) for x in todict.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2) #10
    #for prediction
    # output =( output / 10) * 20 #20

    return render_template('index.html', prediction_text='Performance Rating will be {}'.format(output))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
