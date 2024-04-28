import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt


df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")

df= preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
"Select an option",
("Medal tally","Overall Analysis","Country_wise Analysis","Athlete wise Analysis"))


if user_menu =='Medal tally':
    st.sidebar.header("Medal tally")
    years,country = helper.Country_year_list(df)

    selected_year=st.sidebar.selectbox("Select Year", years)
    selected_country=st.sidebar.selectbox("Select country",country)

    medal_tally = helper.fetch_medal_tally(selected_year,selected_country,df)
    if selected_year == "--Select--" and selected_year == "--Select--":
        st.title("Overall Tally")

    if selected_year != "--Select--" and selected_year == "--Select--":
        st.title("Medal Tally in " + str(selected_year)+"  Olampics")

    if selected_year == "--Select--" and selected_year != "--Select--":
        st.title(selected_country+"  Overall performance")
    if selected_year != "--Select--" and selected_year != "--Select--":
        st.title(selected_country+"  performance in " + str(selected_year) +"  Olampics")
    st.table(medal_tally)


if user_menu =='Overall Analysis':
    editions=df['Year'].unique().shape[0]- 1
    cities=df['City'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    athelets=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3= st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col1:
        st.header("Hosts")
        st.title(cities)
    with col1:
        st.header("Sports")
        st.title(sports)        
    

    col1,col2,col3= st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col1:
        st.header("Nations")
        st.title(nations)
    with col1:
        st.header("Athletes")
        st.title(athelets) 
    

    nation_over_time = helper.participating_nations_over_time(df)
    fig = px.line(nation_over_time, x="Edition", y="No of countries", title='Participating Nation Over Time')
    st.plotly_chart(fig)
    
    event_over_time = helper.Events_all_over_time(df,)
    fig1 = px.line(event_over_time, x="Edition", y="No of Events", title='Events Over The Time')
    st.plotly_chart(fig1)
    
    athlete_over_time = helper.athletes_all_over_time(df,)
    fig2 = px.line(athlete_over_time, x="Edition", y="No of Athletes", title='Athletes Over The Time')
    st.plotly_chart(fig2)
  

    st.title("No. of Events over time(Every sports)")
    fig, ax = plt.subplots(figsize=(10, 10))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(
    x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
    annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"--Select--")
    
    Selected_sport = st.selectbox('Select a Sport',sport_list)
    x=helper.most_successful(df,'Selected_sport')
    st.table(x)


if user_menu =='Country_wise Analysis':
    st.sidebar.title("Country_wise Analysis")
    country_list =df['region'].dropna().unique().tolist()
    country_list.sort()
    

    selected_country=st.sidebar.selectbox("Select a Country", country_list)

    country_df=helper.yearwise_Medal_Tally(df,selected_country)
    
    fig8 = px.line(country_df, x="Year", y="Medal", title='Country wise Medal Tally per Year')
    st.title(selected_country  +"Medal Taly over The Years")
    st.plotly_chart(fig8)

