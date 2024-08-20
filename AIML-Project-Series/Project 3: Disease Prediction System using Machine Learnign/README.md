# Disease Prediction System using Machine Learning

This project focuses on developing a **Disease Prediction System** that predicts heart disease using machine learning techniques. The system utilizes patient data to train various machine learning models, ultimately identifying the most accurate and reliable model for heart disease prediction.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Key Results](#key-results)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [License](#license)

## Overview

The goal of this project is to create a machine learning model that can accurately predict the likelihood of heart disease based on various patient attributes. The project involves data preprocessing, model training, evaluation, and hyperparameter tuning to identify the best-performing model.

## Dataset

The dataset used in this project contains patient data with the following features:
- **Age**
- **Sex**
- **Chest Pain Type (cp)**
- **Resting Blood Pressure (trestbps)**
- **Cholesterol (chol)**
- **Fasting Blood Sugar (fbs)**
- **Resting ECG (restecg)**
- **Maximum Heart Rate Achieved (thalach)**
- **Exercise Induced Angina (exang)**
- **ST Depression Induced by Exercise (oldpeak)**
- **Slope of the Peak Exercise ST Segment (slope)**
- **Number of Major Vessels (ca)**
- **Thalassemia (thal)**
- **Target (Heart Disease: 1 = Yes, 0 = No)**

## Methodology

1. **Data Collection and Preprocessing:** The dataset is cleaned and prepared for model training by handling missing values and normalizing the data where necessary.
2. **Model Selection:** Various machine learning models including Logistic Regression, Support Vector Machine (SVM), Decision Tree, and Random Forest were trained on the data.
3. **Model Evaluation:** Models were evaluated using accuracy scores on both training and testing datasets.
4. **Hyperparameter Tuning:** Grid Search was used to fine-tune the models, optimizing their performance.
5. **Cross-Validation:** Cross-validation was performed to ensure the models' generalizability and robustness.

## Model Training and Evaluation

The following models were trained and evaluated:
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree**
- **Random Forest**

After hyperparameter tuning, the **Random Forest** model was found to be the most accurate and reliable for predicting heart disease, achieving the highest accuracy on the test data.

## Key Results

- **Random Forest Accuracy on Test Data:** 81.97%
- **SVM Accuracy on Test Data:** 80.33%
- **Decision Tree Accuracy on Test Data:** 73.77%

The Random Forest model was chosen as the final model for the disease prediction system due to its superior performance.

