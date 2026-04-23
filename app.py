import pandas as pd
import plotly.express as px
import streamlit as st

# Reading the data
car_data = pd.read_csv('vehicles.csv')

# Application header
st.header('Car Sales Dashboard')

# Introduction text
st.write("""
### Welcome to the Car Sales Data Explorer
This interactive dashboard allows you to explore a dataset of car sales advertisements. 
You can visualize the relationship between vehicle mileage and pricing through different chart types.
Use the buttons below to generate visualizations and discover insights about the car market.
""")

# Button to create histogram
hist_button = st.button('Create histogram')

if hist_button:
    st.write('**Histogram: Distribution of Vehicle Mileage**')
    st.write('This chart shows how vehicle mileage (odometer readings) is distributed across all cars in the dataset.')
    
    fig = px.histogram(car_data, 
                      x="odometer",
                      title="Distribution of Vehicle Mileage",
                      labels={
                          "odometer": "Mileage (miles)",
                          "count": "Number of Vehicles"
                      })
    
    # Customize the chart appearance
    fig.update_layout(
        xaxis_title="Mileage (miles)",
        yaxis_title="Number of Vehicles",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Button to create scatter plot
scatter_button = st.button('Create scatter plot')

if scatter_button:
    st.write('**Scatter Plot: Mileage vs Price Relationship**')
    st.write('This chart explores the relationship between vehicle mileage and price. Generally, you might expect to see lower prices for higher mileage vehicles.')
    
    fig = px.scatter(car_data, 
                    x="odometer", 
                    y="price",
                    title="Vehicle Price vs Mileage",
                    labels={
                        "odometer": "Mileage (miles)",
                        "price": "Price (USD)"
                    })
    
    # Customize the chart appearance
    fig.update_layout(
        xaxis_title="Mileage (miles)",
        yaxis_title="Price (USD)"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.write("---")
st.write("*Data source: Car sales advertisements dataset*")