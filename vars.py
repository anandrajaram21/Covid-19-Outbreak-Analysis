# Imports
import pandas as pd

# Data from the John Hopkins University Dataset on GitHub
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series

# Defining the variables required
filenames = ['time_series_covid19_confirmed_global.csv',
             'time_series_covid19_deaths_global.csv',
             'time_series_covid19_recovered_global.csv']

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

# Making the main dataframes required for the analysis
confirmed_global = pd.read_csv(url + filenames[0])
deaths_global = pd.read_csv(url + filenames[1])
recovered_global = pd.read_csv(url + filenames[2])
country_cases = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')


# Simple Data Cleaning - Removing and renaming the Columns

# Removing the Province/State column, as it is pretty much not of any use
confirmed_global.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
deaths_global.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
recovered_global.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
country_cases.drop(
    columns=["People_Tested", "People_Hospitalized"], inplace=True)

# Renaming the columns for easier access
confirmed_global.rename(columns={"Country/Region": "country"}, inplace=True)
deaths_global.rename(columns={"Country/Region": "country"}, inplace=True)
recovered_global.rename(columns={"Country/Region": "country"}, inplace=True)

country_cases.rename(columns={
    "Country_Region": "country",
    "Last_Update": "last",
    "Confirmed": "confirmed",
    "Deaths": "deaths",
    "Recovered": "recovered",
    "Active": "active",
    "Mortality_Rate": "mortality"
}, inplace=True)

# Removing some duplicate values from the table
confirmed_global = confirmed_global.groupby(['country'], as_index=False).sum()
deaths_global = deaths_global.groupby(['country'], as_index=False).sum()
recovered_global = recovered_global.groupby(['country'], as_index=False).sum()

country_cases_sorted = country_cases.sort_values("confirmed", ascending=False)
country_cases_sorted.index = [x for x in range(len(country_cases_sorted))]
