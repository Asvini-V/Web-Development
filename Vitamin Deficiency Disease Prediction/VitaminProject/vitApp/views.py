from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
ListView,DetailView,
CreateView,DeleteView,
UpdateView)
from . import models
from .forms import *
from django.core.files.storage import FileSystemStorage
#from topicApp.Topicfun import Topic
#from ckdApp.funckd import ckd
#from sklearn.tree import export_graphviz #plot tree
#from sklearn.metrics import roc_curve, auc #for model evaluation
#from sklearn.metrics import classification_report #for model evaluation
##from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df2.drop('classification_yes', 1), df2['classification_yes'], test_size = .2, random_state=10)

import time
import pandas as pd
import numpy as np
#from sklearn.preprocessing import StandardScaler
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
#from sklearn.model_selection import train_test_split
#from sklearn.decomposition import PCA
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt
#import eli5 #for purmutation importance
#from eli5.sklearn import PermutationImportance
#import shap #for SHAP values
#from pdpbox import pdp, info_plots #for partial plots
np.random.seed(123) #ensure reproduc
# ... (your imports remain the same)

class dataUploadView(View):
    form_class = vitForm  # Corrected from ckdForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url = reverse_lazy('fail')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            # -------------------------------
            # Get Vitamin Deficiency Inputs
            # -------------------------------
            data_age = request.POST.get('age')
            data_bmi = request.POST.get('bmi')
            data_ac = request.POST.get('alcohol_consumption')
            data_se = request.POST.get('sun_exposure')
            data_il = request.POST.get('income_level')

            data_latitude_region = request.POST.get('latitude_region')
            data_vitamin_a_percent_rda = request.POST.get('vitamin_a_percent_rda')
            data_vitamin_c_percent_rda = request.POST.get('vitamin_c_percent_rda')
            data_vitamin_d_percent_rda = request.POST.get('vitamin_d_percent_rda')
            data_vitamin_e_percent_rda = request.POST.get('vitamin_e_percent_rda')
            data_vitamin_b12_percent_rda = request.POST.get('vitamin_b12_percent_rda')

            data_folate_percent_rda = request.POST.get('folate_percent_rda')
            data_calcium_percent_rda = request.POST.get('calcium_percent_rda')
            data_iron_percent_rda = request.POST.get('iron_percent_rda')

            data_hemoglobin_g_dl = request.POST.get('hemoglobin_g_dl')
            data_serum_vitamin_d_ng_ml = request.POST.get('serum_vitamin_d_ng_ml')
            data_serum_vitamin_b12_pg_ml = request.POST.get('serum_vitamin_b12_pg_ml')
            data_serum_folate_ng_ml = request.POST.get('serum_folate_ng_ml')

            data_symptoms_count = request.POST.get('symptoms_count')

            data_has_night_blindness = request.POST.get('has_night_blindness')
            data_has_fatigue = request.POST.get('has_fatigue')
            data_has_bleeding_gums = request.POST.get('has_bleeding_gums')
            data_has_bone_pain = request.POST.get('has_bone_pain')
            data_has_muscle_weakness = request.POST.get('has_muscle_weakness')
            data_has_numbness_tingling = request.POST.get('has_numbness_tingling')
            data_has_memory_problems = request.POST.get('has_memory_problems')
            data_has_pale_skin = request.POST.get('has_pale_skin')

            data_gender = request.POST.get('gender')
            data_smoking_status = request.POST.get('smoking_status')
            data_exercise_level = request.POST.get('exercise_level')
            data_diet_type = request.POST.get('diet_type')

            # -------------------------------
            # Raw Data Dictionary
            # -------------------------------
            raw_data = {
                'age': float(data_age),
                'bmi': float(data_bmi),
                'alcohol_consumption': int(data_ac),
                'sun_exposure': int(data_se),
                'income_level': int(data_il),

                'latitude_region': int(data_latitude_region),
                'vitamin_a_percent_rda': float(data_vitamin_a_percent_rda),
                'vitamin_c_percent_rda': float(data_vitamin_c_percent_rda),
                'vitamin_d_percent_rda': float(data_vitamin_d_percent_rda),
                'vitamin_e_percent_rda': float(data_vitamin_e_percent_rda),
                'vitamin_b12_percent_rda': float(data_vitamin_b12_percent_rda),

                'folate_percent_rda': float(data_folate_percent_rda),
                'calcium_percent_rda': float(data_calcium_percent_rda),
                'iron_percent_rda': float(data_iron_percent_rda),

                'hemoglobin_g_dl': float(data_hemoglobin_g_dl),
                'serum_vitamin_d_ng_ml': float(data_serum_vitamin_d_ng_ml),
                'serum_vitamin_b12_pg_ml': float(data_serum_vitamin_b12_pg_ml),
                'serum_folate_ng_ml': float(data_serum_folate_ng_ml),

                'symptoms_count': int(data_symptoms_count),

                'has_night_blindness': int(data_has_night_blindness),
                'has_fatigue': int(data_has_fatigue),
                'has_bleeding_gums': int(data_has_bleeding_gums),
                'has_bone_pain': int(data_has_bone_pain),
                'has_muscle_weakness': int(data_has_muscle_weakness),
                'has_numbness_tingling': int(data_has_numbness_tingling),
                'has_memory_problems': int(data_has_memory_problems),
                'has_pale_skin': int(data_has_pale_skin),

                'gender': data_gender,
                'smoking_status': data_smoking_status,
                'exercise_level': data_exercise_level,
                'diet_type': data_diet_type}

            # 2. Now input_df will work because raw_data exists
            input_df = pd.DataFrame([raw_data])

            # 3. Load your pre-processing tools (from Cell [2])
            model = pickle.load(open("Final_Model.pkl", "rb"))
            selector = pickle.load(open("F_selector.pkl", "rb"))
            scaler = pickle.load(open("scaler.pkl", "rb"))
            model_columns = pickle.load(open("columns.pkl", "rb"))

            # 4. Processing (from Cell [6] & [7])
            input_encoded = pd.get_dummies(input_df)
            input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
            input_final = scaler.transform(selector.transform(input_encoded))


            # 5. Prediction
            prediction = model.predict(input_final)[0]
            label_map = {0: "Anemia", 1: "Healthy", 2: "Night Blindness", 3: "Rickets_Osteomalacia", 4: "Scurvy"}
            out = label_map.get(prediction, "Unknown")

            # Update the context dictionary to include 'out' AND your inputs
            # This matches the "entire dictionary" approach from the lesson
            context = raw_data.copy()
            context['y_pred'] = out 

            return render(request, "succ_msg.html", context)
        else:
            # Fix: .is_valid() check ends here
            return redirect(self.failure_url)
