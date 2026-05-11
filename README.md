# Vitamin Deficiency Prediction Web Application

This project is a Machine Learning based web application developed using Django.  
The application predicts vitamin deficiency diseases based on patient health, nutritional, and lifestyle data.

## Project Overview

The system takes user input such as:
- Age
- Gender
- BMI
- Nutritional intake
- Serum vitamin levels
- Lifestyle habits
- Symptoms

and predicts the possible vitamin deficiency condition using a trained Machine Learning model.

## Technologies Used

- Python
- Django
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- HTML
- Bootstrap

## Features

- User-friendly web interface
- Patient data input form
- Machine Learning prediction system
- Result display page
- Local server deployment using Django

## Machine Learning Workflow

1. Data preprocessing
2. Feature selection
3. Model training
4. Model serialization using Pickle
5. Integration with Django web application
6. Prediction through local server

## Project Structure

```bash
VitaminProject/
│
├── vitApp/
├── templates/
├── static/
├── model.pkl
├── manage.py
└── requirements.txt

How to Run the Project
Clone Repository
git clone <repository-link>
Install Dependencies
pip install -r requirements.txt
Run Server
python manage.py runserver
Open Browser
http://127.0.0.1:8000/
Learning Outcome

Through this project, I learned:

Machine Learning model deployment
Django web framework basics
URL routing
Template rendering
Integrating ML models with web applications
Running applications on a local server
