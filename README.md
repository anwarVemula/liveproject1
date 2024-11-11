
Wildfire Risk Prediction App

Project Overview

This project is a personal end-to-end machine learning application developed to predict wildfire risk levels based on environmental factors. Built with Flask, it provides an interactive interface where users can input various weather conditions and receive a risk score, showcasing the use of a Ridge Regression model in predicting wildfire tendencies.

Features

Prediction Model: Ridge Regression model for wildfire risk prediction.
Data Preprocessing: StandardScaler applied to input data for consistent predictions.
Interactive Interface: User-friendly input form to submit data and view predictions instantly.

Tech Stack

Backend: Flask
Modeling: Ridge Regression, Scikit-Learn for model persistence
Frontend: HTML templates for user input and result display

Input Variables

Temperature: Current temperature in °C
RH: Relative humidity (%)
Ws: Wind speed (km/h)
Rain: Rainfall (mm)
FFMC, DMC, ISI: Fire risk indices
Classes: Fire classification level
Region: Region code for specificity
Setup & Installation

Requirements

Python 3.x
Flask
Scikit-Learn
