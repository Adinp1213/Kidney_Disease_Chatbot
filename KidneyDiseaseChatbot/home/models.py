from django.db import models

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)

class AdminDetails(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

class FeedBackDetails(models.Model):
    userid = models.CharField(max_length=122)
    feedback = models.CharField(max_length= 300)
    response = models.CharField(max_length = 300,null=True)

class PreviousDetection(models.Model):
    user_id = models.CharField(max_length=122)
    datetime = models.DateTimeField(auto_now_add=True)
    detection_result = models.CharField(max_length=122)
    input_file = models.FileField(upload_to='media/', default=None)

class ProfileDetails(models.Model):
    user_id = models.CharField(max_length=122)
    # Demographic Information
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True)
    # Lifestyle and Activity
    activity_level = models.CharField(max_length=50, blank=True)
    exercise_frequency = models.CharField(max_length=50, blank=True)
    # Dietary Habits
    vegetarian = models.CharField(max_length=50, blank=True,null=True)
    allergies = models.TextField(blank=True)
    # Medical History
    medical_conditions = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    # Biometric Data
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    # Health Metrics
    blood_pressure = models.CharField(max_length=20, blank=True)
    cholesterol_level = models.CharField(max_length=20, blank=True)
    # Sleep Patterns
    sleep_duration = models.FloatField(blank=True, null=True)
    sleep_quality = models.CharField(max_length=50, blank=True)
    # Smoking and Alcohol Consumption
    smoking_status = models.CharField(max_length=50, blank=True)
    alcohol_consumption = models.CharField(max_length=50, blank=True)
    # Psychosocial Factors
    stress_level = models.CharField(max_length=50, blank=True)
    mental_health_status = models.CharField(max_length=50, blank=True)
    # Health Goals
    health_goals = models.TextField(blank=True)