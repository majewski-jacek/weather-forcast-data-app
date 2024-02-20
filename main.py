import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days =st.slider("Forecast Days", min_value=1, max_value=5,
                help="Select the number of forcasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky data and dates
        filtered_data = get_data(place, days)
        dates = [dict["dt_txt"] for dict in filtered_data]

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]-273.15 for dict in filtered_data]            
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, 
                            labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_contitions = [dict["weather"][0]["main"] for dict in filtered_data]
            imaages_paths = [images[condition] for condition in sky_contitions]
            st.image(imaages_paths, caption=dates, width=115)
    except KeyError:
        st.info("The place doesn't exist")
