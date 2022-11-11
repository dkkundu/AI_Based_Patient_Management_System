from django import forms

sex_chose = [
    (0, "Male"),
    (1, "Female")
]
chest_pain_type_chose = [
    (0, "Normal"),
    (1, "Simple Pain"),
    (2, "One time Pain"),
    (3, "Multiple Time Pain"),
]
resting_electrocardiographic_results_chose = [
    (0, "Normal"),
    (1, "Stage 1"),
    (2, "Stage 2"),
]
thal_chose = [
    (0, "Normal"),
    (1, "Fixed Defect"),
    (2, "Reversable defect"),
    (3, "Full defect"),
]


class HeartDiseasePredictionForm(forms.Form):

    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=sex_chose)
    chest_pain_type = forms.ChoiceField(
        choices=chest_pain_type_chose,
        label="Chest Pain Type"
    )

    resting_blood_pressure = forms.IntegerField(
        label="Resting Blood Pressure"
    )
    serum_cholestoral = forms.IntegerField(
        help_text="Serum Cholestoral in MG/DL",
        label="Serum Cholestoral"

    )
    fasting_blood_sugar = forms.IntegerField(
        help_text="Fasting Blood Sugar(More than 120 MG/DL)",
        label="Fasting Blood Sugar"

    )
    resting_electrocardiographic_results = forms.ChoiceField(
        choices=resting_electrocardiographic_results_chose,
        label="Resting Electrocardiographic Results (ECO)"

    )
    maximum_heart_rate_achieved = forms.IntegerField(
        label="Maximum Heart Rate Achieved"
    )
    exercise_induced_angina = forms.IntegerField(
        label="Exercise Induced Angina"
    )
    oldpeak = forms.IntegerField(
        help_text="ST depression induced by exercise relative to rest",
        label="Oldpeak"

    )
    slope = forms.IntegerField(
        label="The slope of the peak exercise ST segment"
    )
    ca = forms.IntegerField(
        label="Number of major vessels (0-3) colored by flourosopy"
    )
    thal = forms.ChoiceField(
        choices=thal_chose
    )
