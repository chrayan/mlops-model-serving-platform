# MLOps Model Serving Platform

Example machine learning deployment service with training pipeline and prediction API.

## Features
Model training pipeline  
Model serialization  
Inference API  
Simple model registry structure

## Tech Stack
Python  
FastAPI  
Scikit-learn  
Joblib

## Project Structure
models/train.py – model training  
serving/api.py – prediction API  
registry – model registry  
monitoring – metrics tracking

## Install

pip install -r requirements.txt

## Train Model

python models/train.py

## Run API

uvicorn serving.api:app --reload

## Endpoint

POST /predict
