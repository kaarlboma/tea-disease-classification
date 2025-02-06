# Tea Leaf Disease Classifier

A machine learning web application that classifies diseases in tea leaf images

## Demo

🌿 [Try it yourself!](https://tea-leaf-disease-classifier.streamlit.app)

## Overview

This project uses machine learning to identify diseases in tea leaves from uploaded images. The model was trained on 850+ labeled images using XGBoost and achieves 80% average accuracy through 5-fold cross validation.

## Features

- Upload and classify tea leaf images
- Get instant disease classification results
- Simple, easy-to-use web interface

## Tech Stack

- **ML Model**: XGBoost
- **Image Processing**: PIL
- **Backend**: FastAPI 
- **Frontend**: Streamlit
- **Deployment**: Docker, AWS ECS

## Getting Started

```bash
# Clone the repository
git clone https://github.com/kaarlboma/tea-disease-classification.git

# Navigate to project directory
cd tea-disease-classification

# Build and run with Streamlit
cd tea-disease-classification/streamlit
streamlit run main.py
```
Visit http://localhost:8501 in your browser.

Visit `http://localhost:8501` in your browser.
