"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
from .views import (
    train_heart_disease_model, prediction_heart_disease,
    train_pneumonia_disease_model
)
# CORE IMPORTS
app_name = 'ai'

urlpatterns = [
    # index url ---------------------------------------------------------------
    path(
        'train-heart-disease-model/', train_heart_disease_model,
        name='train-heart-disease'
    ),
    path(
        'prediction-heart-disease/', prediction_heart_disease,
        name='prediction_heart_disease'
    ),
    path(
        'train-pneumonia-disease/', train_pneumonia_disease_model,
        name='train_pneumonia_disease'
    ),


]
