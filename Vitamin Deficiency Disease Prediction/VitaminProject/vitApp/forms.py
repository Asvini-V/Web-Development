from django import forms
from .models import *

class vitForm(forms.ModelForm):
    class Meta():
        model = vitModel
        # Replace the list below with the actual column names from your vitamin dataset
        fields = ['age','bmi', 'alcohol_consumption', 'sun_exposure', 'income_level', 'latitude_region', 'vitamin_a_percent_rda',
        'vitamin_c_percent_rda', 'vitamin_d_percent_rda', 'vitamin_e_percent_rda', 'vitamin_b12_percent_rda', 'folate_percent_rda',
         'calcium_percent_rda', 'iron_percent_rda', 'hemoglobin_g_dl', 'serum_vitamin_d_ng_ml', 'serum_vitamin_b12_pg_ml',
         'serum_folate_ng_ml', 'symptoms_count', 'has_night_blindness', 'has_fatigue', 'has_bleeding_gums', 'has_bone_pain',
         'has_muscle_weakness', 'has_numbness_tingling', 'has_memory_problems', 'has_pale_skin', 'gender', 'smoking_status',
         'exercise_level', 'diet_type']
