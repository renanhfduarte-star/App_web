# Car Sales Dashboard

This repository contains a web application built with Streamlit for exploring car sales advertisement data through interactive visualizations.

## Project Overview

This project was developed as part of a Data Analytics Bootcamp curriculum. The primary goal is to create an interactive web dashboard that allows users to explore a dataset of car sales advertisements. By providing on-demand visualizations, the application facilitates the analysis of vehicle mileage distribution and its correlation with pricing.

*Dashboard Link:* [View Live Application on Render](#) *(https://app-web-4oqf.onrender.com/)*

## Tools & Technologies

*   **Python 3.x:** Core programming language.
*   **Streamlit:** Web application framework for UI creation and interactivity.
*   **Pandas:** Data manipulation, cleaning, and analysis.
*   **Plotly Express:** Interactive data visualization.
*   **Render:** Cloud deployment platform.

## Key Features

| Feature Category | Description |
| :--- | :--- |
| **Distribution Analysis** | Interactive histogram visualization that displays the distribution of vehicle mileage (odometer readings) across the entire dataset. |
| **Pricing Relationship** | Dynamic scatter plot visualization designed to explore and identify correlations between vehicle mileage and listing price. |
| **User Interactivity** | Clean UI with interactive buttons that allow users to generate, toggle, and manipulate charts on demand without reloading the page. |

## Repository Structure

```text
├── README.md
├── app.py                 # Main Streamlit application
├── vehicles.csv           # Car sales dataset
├── requirements.txt       # Python dependencies
├── notebooks/
│   └── EDA.ipynb          # Exploratory Data Analysis
└── .streamlit/
    └── config.toml        # Streamlit configuration for deployment