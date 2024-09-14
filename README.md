Olympics Data Analysis Web Application
Overview
This project is a Streamlit web application designed to analyze historical Olympic Games data from Athens 1896 to Rio 2016. The dataset includes details about athletes, events, and medals, offering insights into how the Olympic Games have evolved over time. The web app is interactive and allows users to explore different aspects of the data, including medal tallies, country-wise performances, and athlete achievements.

Features
Medal Tally: View the medal tally for specific years and countries.
Overall Analysis: Examine key statistics such as the number of editions, participating nations, athletes, events, and more.
Country-wise Analysis: Explore how specific countries have performed in terms of medals over the years.
Athlete-wise Analysis: View the top-performing athletes by sport and medals won.
Technologies Used
Frontend: Streamlit for the user interface.
Backend: Python, Pandas for data processing.
Data Visualization: Seaborn and Plotly for generating insightful visualizations.
Deployment: The application is deployed on Heroku for easy access.
Dataset
The dataset used in this project is historical data on the Olympic Games, scraped from Sports Reference in May 2018. It includes 271,116 rows and 15 columns with details about athletes, their performance, and events they participated in. The columns are:

ID: Unique number for each athlete
Name: Athlete's name
Sex: M or F
Age: Integer
Height: In centimeters
Weight: In kilograms
Team: Team name
NOC: National Olympic Committee 3-letter code
Games: Year and season
Year: Integer
Season: Summer or Winter
City: Host city
Sport: Sport
Event: Event
Medal: Gold, Silver, Bronze, or NA
Installation
To run the project locally, follow these steps:

Prerequisites
Python 3.x
Streamlit
Pandas
Plotly
Seaborn
Matplotlib
Steps
Clone the repository:

Copy code
streamlit run app.py
Access the app: Open the local Streamlit link provided in the terminal after running the above command.

Project Structure
plaintext
├── app.py                     # Main Streamlit app
├── helper.py                  # Helper functions for data processing and visualization
├── preprocessor.py            # Data cleaning and preprocessing
├── athlete_events.csv          # Dataset with Olympic athlete data
├── noc_regions.csv             # National Olympic Committee regions
└── README.md                  # This file


Acknowledgements
Data scraped from Sports Reference.
Thanks to the Olympic history enthusiasts and 'statistorians' for their incredible research.
License
This project is licensed under the MIT License.

