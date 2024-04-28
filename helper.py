import numpy as np 
import pandas as pd

import pandas as pd

def fetch_medal_tally(years, country, df):
    medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','Sport','Event','Medal'])
    flag = 0
    if years == "--Select--" and country == "--Select--":
        temp_df = medal_df
    elif years == "--Select--" and country != "--Select--":
        flag =1 
        temp_df = medal_df[medal_df['region'] == country]
    elif years != "--Select--" and country == "--Select--":
        temp_df = medal_df[medal_df['Year'] == int(years)]
    elif years != "--Select--" and country != "--Select--":
        temp_df = medal_df[(medal_df['Year'] == int(years)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x




def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total'] =medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']
    return medal_tally

def Country_year_list(df):
    years=df['Year'].unique().tolist()  
    years.sort()
    years.insert(0,'--Select--')

    country  = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'--Select--')

    return years,country





def participating_nations_over_time(df):
    nation_over_time = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index()
    nation_over_time.columns = ['Edition', 'No of countries']
    nation_over_time = nation_over_time.sort_values('Edition')
    return nation_over_time

def Events_all_over_time(df):
    event_over_time = df.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index()
    event_over_time.columns = ['Edition', 'No of Events']
    event_over_time = event_over_time.sort_values('Edition')
    return event_over_time
def athletes_all_over_time(df):
    athlete_over_time = df.drop_duplicates(['Year','Name'])['Year'].value_counts().reset_index()
    athlete_over_time.columns = ['Edition', 'No of Athletes']
    athlete_over_time = athlete_over_time.sort_values('Edition')
    return athlete_over_time



def most_successful(df, sport):
    temp_df = df.dropna(subset=["Medal"])
    if sport != "--Select--":
        temp_df = temp_df[temp_df['Sport'] == sport]
            
    # Calculate the counts of 'Name' occurrences and reset the index
    name_counts = temp_df['Name'].value_counts().reset_index()
    name_counts.columns = ['Name', 'Medals']  # Rename columns for clarity
    
    # Merge with the original DataFrame 'df' based on the 'Name' column
    merged_df = pd.merge(name_counts.head(15), df, on='Name', how='left')[['Name', 'Medals', 'Sport', 'region']]
    
    # Drop duplicates based on the 'Name' column
    x = merged_df.drop_duplicates('Name')
    return x     


def yearwise_Medal_Tally(df,country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team','NOC','Games','Year','Sport','Event','Medal'],inplace = True)       
    new_df=temp_df[temp_df['region'] == country]
    final_df =new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df

def Country_event_heatmap(df,country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team','NOC','Games','Year','Sport','Event','Medal'],inplace = True) 


    new_df=temp_df[temp_df['region'] == country]
    pt=new_df.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0).annot=True
    return pt



    

            
    
