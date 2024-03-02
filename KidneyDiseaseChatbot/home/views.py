from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404 
from home.models import UserDetails,AdminDetails,FeedBackDetails,PreviousDetection,ProfileDetails
from django.contrib import messages
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from home import gui
from joblib import load
import numpy as np
from datetime import datetime
from django.core.files.base import ContentFile
import os
from dateutil import parser as date_parser
# Load the saved model
loaded_rf = load('home/random_forest_model.joblib')
# Create your views here.

flag = False
current_question_index = 0
answers = []

def index(request):
    global flag, current_question_index,answers
    flag = False
    current_question_index = 0
    answers=[]
    return render(request,'index2.html')

def login(request):
    return render(request,'login.html')

def create(request):
    return render(request,'createaccount.html')

def logout(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(username = username)
        except UserDetails.DoesNotExist:
            user = None
        
        if user is not None:
            if(user.password == password):
                messages.success(request, 'You have successfully logged in.')
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                
                return redirect("/")
            # Passwords match, redirect to home
            else:
                messages.error(request, 'Wrong password')
                return redirect("/login")

        else:
            messages.error(request, 'Account not found')
            return redirect("/login")

    return render(request, 'logout.html')

def failed(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        confirmPassword = request.POST.get('confirmPassword')

        if UserDetails.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect("/create") 
        
        if password!=confirmPassword:
            messages.error(request, 'Passwords does not match')
            return redirect("/create") 
        
        else:
            user = UserDetails(username = username, password = password,email =email,phone=phone)
            user.save()
            profile_details = ProfileDetails(user_id = user.id)
            profile_details.save()
            messages.success(request, 'Account created successfully!')
            return redirect("/") 
        
    return render(request, 'failed.html')

def logout_2(request):
    request.session.clear()
    return redirect('/')

def login_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = AdminDetails.objects.get(username = username)
        except AdminDetails.DoesNotExist:
            user = None
        
        if user is not None:
            if(user.password == password):
                messages.success(request, 'You have successfully logged in.')
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                
                return redirect("/admin_home")
            # Passwords match, redirect to home
            else:
                messages.error(request, 'Wrong password')
                return redirect("/login_admin")

        else:
            messages.error(request, 'Account not found')
            return redirect("/login_admin")

    return render(request, 'login_admin.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def view_users(request):
    users = UserDetails.objects.all() 
    return render(request, 'view_users.html', {'users': users})

def view_feedbacks(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        response = request.POST.get('response_text')

        feedback = FeedBackDetails.objects.get(id=feedback_id)
        feedback.response = response
        feedback.save()

    feedbacks = FeedBackDetails.objects.all() 
    return render(request, 'view_feedbacks.html', {'feedbacks': feedbacks})

def give_feedback(request):
    if request.method == "POST":
        user_id = request.session.get('user_id', None)
        feedback_text = request.POST.get('feedback', None)
        feedback = FeedBackDetails.objects.create(userid=user_id, feedback=feedback_text, response=None)
        messages.success(request, 'Feedback submitted!')
        return redirect('give_feedback')  # Redirect to the feedback page to show the updated list
    
    user_id = request.session.get('user_id', None)  # Get user ID from session
    if user_id:
        user_feedback = FeedBackDetails.objects.filter(userid=user_id)  # Get feedbacks for the user ID
        return render(request, 'give_feedback.html', {'user_feedback': user_feedback})
    else:
        return redirect('/login')   

def previous_detection(request):
    user_id = request.session.get('user_id', None)  # Get user ID from session
    if user_id:
        data = PreviousDetection.objects.filter(user_id=user_id) 
        return render(request,'previous_detection.html',{'data': data})
    else:
        return redirect('/login')
    
def profile_management(request):
    user_id = request.session.get('user_id', None)  # Get user ID from session
    if user_id:
        profile_details = ProfileDetails.objects.get(user_id=user_id) 
        print(profile_details.age)
        return render(request,'profile_management.html', {'profile': profile_details})
    else:
        return redirect('/login')
    
def edit_profile(request):
    user_id = request.session.get('user_id', None)
    profile_details = ProfileDetails.objects.get(user_id=user_id)  

    if request.method == "POST":
        profile_details.age = request.POST.get('age', None)
        profile_details.gender = request.POST.get('gender', None)
        profile_details.activity_level = request.POST.get('activity_level', None)
        profile_details.exercise_frequency = request.POST.get('exercise_frequency', None)
        profile_details.vegetarian = request.POST.get('vegetarian', None)
        profile_details.allergies = request.POST.get('allergies', None)
        profile_details.medical_conditions = request.POST.get('medical_conditions', None)
        profile_details.medications = request.POST.get('medications', None)
        profile_details.height = request.POST.get('height', None) or None  # Convert empty string to None
        profile_details.weight = request.POST.get('weight', None) or None
        profile_details.blood_pressure = request.POST.get('blood_pressure', None)
        profile_details.cholesterol_level = request.POST.get('cholesterol_level', None)
        profile_details.sleep_duration = request.POST.get('sleep_duration', None) or None
        profile_details.sleep_quality = request.POST.get('sleep_quality', None)
        profile_details.smoking_status = request.POST.get('smoking_status', None)
        profile_details.alcohol_consumption = request.POST.get('alcohol_consumption', None)
        profile_details.stress_level = request.POST.get('stress_level', None)
        profile_details.mental_health_status = request.POST.get('mental_health_status', None)
        profile_details.health_goals = request.POST.get('health_goals', None)
        profile_details.save()
        return redirect('/profile_management')

    return render(request,'edit_profile.html',{'profile_details': profile_details})

def demo(request):
    return render(request,'demo.html')

def chatbot(request):
    global flag, current_question_index,answers
    questions = [
        'What is your Age?',
        'What is your Blood Pressure?', 
        'What is your Specific Gravity?',
        'What is your albumin?',
        'What is your sugar level?',
        'RBCs Count? 0 if normal, 1 if abnormal',
        'Pus cell? 0 if normal, 1 if abnormal',
        'Pus cell-clumps? 0 if present, 1 if not present',
        'Bacteria? 0 if present, 1 if not present',
        'Blood Glucose random level?',
        'Blood Urea level?',
        'serum creatinine level?',
        'Sodium level?',
        'Potassium level?',
        'Haemoglobin level ?',
        'Packed cell volume?',
        'WBC cell count ?',
        'RBC count?',
        'Do you have Hypertension? 1 if yes, 0 if no',
        'Do you have diabetes mellitus? 1 if yes, 0 if no',
        'Do you have coronary artery disease? 1 if yes, 0 if no',
        'How is your appetite? 1 if good, 0 if poor ',
        'Do you have peda edema? 1 if yes, 0 if no',
        'Are you have anemic? 1 if yes, 0 if no',
    ]

    if request.method == 'POST':

        user_id = request.session.get('user_id', None)

        if user_id == None:
            return JsonResponse({'response': 'Login First if you want to use chatbot'})
        
        user_message = request.POST.get('message', '')
        print(user_message)

        if "start" in user_message.lower() and "ckd" in user_message.lower() and flag:
            current_question_index = 0
            answers = []
            bot_response = "Detection started. Please answer the following questions: (Press Ok to start detection) (Answer in numbers only)"

        elif flag:
            if current_question_index < len(questions):
                answers.append(user_message)
                
                if current_question_index < len(questions):
                    bot_response = questions[current_question_index]
                    
                else:
                    flag = False
                    bot_response = "All questions have been asked. Thank you!"
                current_question_index += 1
            else:
                answers.append(user_message)
                current_question_index = 0
                flag = False
                final_pred, answers_float = getprediction(answers)
                question_answer_str = "\n".join([f"Question {i}: {question}\nAnswer {i}: {answer}" for i, (question, answer) in enumerate(zip(questions, answers_float))])
                file_contents = ContentFile(question_answer_str)
                file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_questions_answers.txt"
                file_path = os.path.join('media/', file_name)
                with open(file_path, 'w') as f:
                    f.write(file_contents.read())
                previous_detection = PreviousDetection(user_id = user_id ,datetime=datetime.now(), detection_result=final_pred,input_file=file_name)
                previous_detection.save()
                
                answers = []
                if final_pred == "Not CKD":
                    bot_response = "All questions have been answered. No need to worry you dont have any chronic kidney disease"
                else:
                    bot_response = "All questions have been answered. You seem to be at a risk of chronic kidney Disease. Consult a doctor for more information about your condition"

        elif "start" in user_message.lower() and "ckd" in user_message.lower():
            flag = True
            current_question_index = 0
            answers = []
            bot_response = "Detection started. Please answer the following questions: (Press Ok to start detection) (Answer in numbers only)"
        else:
            bot_response = gui.get_response(user_message)  

        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def getprediction(answers):
    answers = answers[1:]
    default_answers = [41.0, 70.0 ,1.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 125.0, 38.0, 0.6, 140.0, 5.0, 16.8, 41, 6300, 5.9, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]

    # Replace missing values with default values
    answers_float = [float(answer) if answer else default_answers[i] for i, answer in enumerate(answers)]

    answers_2d = np.array(answers_float).reshape(1, -1)
    print(answers_float)
    prediction = loaded_rf.predict(answers_2d)
    if prediction[0] == 0.0: 
        final_pred = "Not CKD" 
    else: 
        final_pred = "CKD"
    print(final_pred)
    return final_pred, answers_float
    
# def ckd_detection(request):
#     user_id = request.session.get('user_id', None)  # Get user ID from session
#     if user_id:
#         return render(request,'ckd_detection.html')
#     else:
#         return redirect('/login')