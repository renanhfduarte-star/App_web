# Car Sales Dashboard

A web application built with Streamlit for exploring car sales advertisement data through interactive visualizations.

## 🚀 Live Demo

**[View Live Application](https://app-web-4oqf.onrender.com/)**

## 📋 Project Description

This project is part of the TripleTen Data Analysis Bootcamp (Sprint 5). The goal is to create an interactive web dashboard that allows users to explore a dataset of car sales advertisements through different types of visualizations.

The application provides:
- **Histogram visualization**: Shows the distribution of vehicle mileage
- **Scatter plot visualization**: Explores the relationship between mileage and price
- **Interactive buttons**: Users can generate charts on demand

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly Express** - Interactive data visualization
- **Render** - Cloud deployment platform

## 📁 Project Structure

```
├── README.md
├── app.py                 # Main Streamlit application
├── vehicles.csv           # Car sales dataset
├── requirements.txt       # Python dependencies
├── notebooks/
│   └── EDA.ipynb         # Exploratory Data Analysis
└── .streamlit/
    └── config.toml       # Streamlit configuration for deployment

🚀 How to Run Locally

Clone the repository

bash
git clone https://github.com/renanhfduarte-star/App_web.git
cd App_web

Create a virtual environment

conda create -n vehicles_env python=3.9
conda activate vehicles_env

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

Open your browser and go to http://localhost:8501

📊 Dataset

The dataset contains information about car sales advertisements including:
- Vehicle mileage (odometer readings)
- Pricing information
- Various vehicle characteristics

Source: Car sales advertisements dataset

🌐 Deployment
This application is deployed on Render and is accessible via the live demo link above.

👨‍💻 Author
Renan Duarte
- GitHub: @renanhfduarte-star
- LinkedIn: renanduarteferreira

📝 License
This project is part of the TripleTen Data Analysis Bootcamp curriculum.
```