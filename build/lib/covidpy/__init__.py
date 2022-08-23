"""
covidpy.

Detailed Regular Information about World\'s Covid19 Data.
"""

__version__ = "0.1.4"
__author__ = 'Nahidujjaman Hridoy'
__credits__ = 'Worldometer'

import requests
import pandas as pd
from bs4 import BeautifulSoup

### Web Scraping ###
full_page = requests.get("https://www.worldometers.info/coronavirus/")
full_page = full_page.content
soup = BeautifulSoup(full_page, "html.parser")


def WorldData():
    ### Scrapping World Data ###
    world = soup.find_all("tr", {"class": "total_row_world"})[7]
    ### All World Data ###
    world_total_cases = int(world.find_all("td")[2].text[:].replace(',', ''))
    world_new_cases = world.find_all("td")[3].text[1:].replace(',', '')
    world_total_deaths = int(world.find_all("td")[4].text[:].replace(',', ''))
    world_new_deaths = world.find_all("td")[5].text[1:].replace(',', '')
    world_total_recovered = int(world.find_all("td")[6].text[:].replace(',', ''))
    world_new_recovered = world.find_all("td")[7].text[1:].replace(',', '')
    world_total_active = world.find_all("td")[8].text[:].replace(',', '')
    world_total_serious = world.find_all("td")[9].text[:].replace(',', '')

    if world_new_cases == "":
        world_new_cases = 0
    else:
        world_new_cases = int(world.find_all("td")[3].text[1:].replace(',', ''))

    if world_new_deaths == "":
        world_new_deaths = 0
    else:
        world_new_deaths = int(world.find_all("td")[5].text[1:].replace(',', ''))

    if world_new_recovered == "":
        world_new_recovered = 0
    else:
        world_new_recovered = int(world.find_all("td")[7].text[1:].replace(',', ''))

    if world_total_active == "":
        world_total_active = 0
    else:
        world_total_active = int(world.find_all("td")[8].text[:].replace(',', ''))

    if world_total_serious == "":
        world_total_serious = 0
    else:
        world_total_serious = int(world.find_all("td")[9].text[:].replace(',', ''))

    return {
        "Total_Cases": world_total_cases,
        "New_Cases": world_new_cases,
        "Total_Deaths": world_total_deaths,
        "New_Deaths": world_new_deaths,
        "Total_Recovered": world_total_recovered,
        "New_Recovered": world_new_recovered,
        "Active_Cases": world_total_active,
        "Serious_Cases": world_total_serious,
    }


def ListCountries():
    ### Scrapping Country Data ###
    countries = soup.find_all("table", {"class": "table-hover"})[0]
    countries = (countries.find_all("tr"))
    empty_dataframe = [
        [counter, n.find(["nobr", "a", "span"]).text.upper()]
        for counter, n in enumerate(countries)
        if n.find(["nobr", "a", "span"]) is not None
    ]

    countries_scapped = pd.DataFrame(empty_dataframe)[1:]
    countries_scapped.columns = ["Country_ID", "Country_Name"]

    return countries_scapped


countries_scapped = ListCountries()


def CountryData(country=""):
    country = country.upper()
    Country_ID_Selected = int(countries_scapped[countries_scapped["Country_Name"] == country]["Country_ID"])
    countries = soup.find_all("table", {"class": "table-hover"})[0]
    countries = (countries.find_all("tr"))
    ### Country Data ###
    country_total_cases = countries[Country_ID_Selected].find_all("td")[2].text.replace("+", "").replace(",", "")
    country_new_cases = countries[Country_ID_Selected].find_all("td")[3].text.replace("+", "").replace(",", "")
    country_total_deaths = countries[Country_ID_Selected].find_all("td")[4].text.replace("+", "").replace(",", "")
    country_new_deaths = countries[Country_ID_Selected].find_all("td")[5].text.replace("+", "").replace(",", "")
    country_total_recovered = countries[Country_ID_Selected].find_all("td")[6].text.replace("+", "").replace(",", "")
    country_new_recovered = countries[Country_ID_Selected].find_all("td")[7].text.replace("+", "").replace(",", "")
    country_total_active = countries[Country_ID_Selected].find_all("td")[8].text.replace("+", "").replace(",", "")
    country_total_serious = countries[Country_ID_Selected].find_all("td")[9].text.replace("+", "").replace(",", "")
    country_total_tests = countries[Country_ID_Selected].find_all("td")[12].text.replace("+", "").replace(",", "")

    if country_total_cases == "":
        country_total_cases = 0
    else:
        country_total_cases = int(countries[Country_ID_Selected].find_all("td")[2].text.replace("+", "").replace(",", ""))

    if country_new_cases == "":
        country_new_cases = 0
    else:
        country_new_cases = int(countries[Country_ID_Selected].find_all("td")[3].text.replace("+", "").replace(",", ""))

    if country_total_deaths in [" ", ""]:
        country_total_deaths = 0
    else:
        country_total_deaths = int(
            countries[Country_ID_Selected].find_all("td")[4].text.replace("+", "").replace(",", ""))

    if country_new_deaths == "":
        country_new_deaths = 0
    else:
        country_new_deaths = int(
            countries[Country_ID_Selected].find_all("td")[5].text.replace("+", "").replace(",", ""))

    if country_total_recovered == "":
        country_total_recovered = 0
    else:
        country_total_recovered = int(
            countries[Country_ID_Selected].find_all("td")[6].text.replace("+", "").replace(",", ""))

    if country_new_recovered == "":
        country_new_recovered = 0
    else:
        country_new_recovered = int(
            countries[Country_ID_Selected].find_all("td")[7].text.replace("+", "").replace(",", ""))

    if country_total_active == "":
        country_total_active = 0
    else:
        country_total_active = int(
            countries[Country_ID_Selected].find_all("td")[8].text.replace("+", "").replace(",", ""))

    if country_total_serious == "":
        country_total_serious = 0
    else:
        country_total_serious = int(
            countries[Country_ID_Selected].find_all("td")[9].text.replace("+", "").replace(",", ""))

    if country_total_tests == "":
        country_total_tests = 0
    else:
        country_total_tests = int(
            countries[Country_ID_Selected].find_all("td")[12].text.replace("+", "").replace(",", ""))

    return {
        "Country_Name": country,
        "Total_Cases": country_total_cases,
        "New_Cases": country_new_cases,
        "Total_Deaths": country_total_deaths,
        "New_Deaths": country_new_deaths,
        "Total_Recovered": country_total_recovered,
        "New_Recovered": country_new_recovered,
        "Active_Cases": country_total_active,
        "Serious_Cases": country_total_serious,
        "Total_Tests": country_total_tests,
    }


def AllData():
    all_country_data = []
    for country in countries_scapped[7:]["Country_Name"]:
        country = country.upper()
        Country_ID_Selected = int(countries_scapped[countries_scapped["Country_Name"] == country]["Country_ID"])
        countries = soup.find_all("table", {"class": "table-hover"})[0]
        countries = (countries.find_all("tr"))
        ### Country Data ###
        country_total_cases = countries[Country_ID_Selected].find_all("td")[2].text.replace("+", "").replace(",", "")
        country_new_cases = countries[Country_ID_Selected].find_all("td")[3].text.replace("+", "").replace(",", "")
        country_total_deaths = countries[Country_ID_Selected].find_all("td")[4].text.replace("+", "").replace(",", "")
        country_new_deaths = countries[Country_ID_Selected].find_all("td")[5].text.replace("+", "").replace(",", "")
        country_total_recovered = countries[Country_ID_Selected].find_all("td")[6].text.replace("+", "").replace(",",
                                                                                                                 "")
        country_new_recovered = countries[Country_ID_Selected].find_all("td")[7].text.replace("+", "").replace(",", "")
        country_total_active = countries[Country_ID_Selected].find_all("td")[8].text.replace("+", "").replace(",", "")
        country_total_serious = countries[Country_ID_Selected].find_all("td")[9].text.replace("+", "").replace(",", "")
        country_total_tests = countries[Country_ID_Selected].find_all("td")[12].text.replace("+", "").replace(",", "")

        country_total_cases = (
            0
            if country_total_cases == ""
            else int(
                countries[Country_ID_Selected]
                .find_all("td")[2]
                .text.replace("+", "")
                .replace(",", "")
            )
        )

        country_new_cases = (
            0
            if country_new_cases == ""
            else int(
                countries[Country_ID_Selected]
                .find_all("td")[3]
                .text.replace("+", "")
                .replace(",", "")
            )
        )

        if country_total_deaths in [" ", ""]:
            country_total_deaths = 0
        else:
            country_total_deaths = int(
                countries[Country_ID_Selected].find_all("td")[4].text.replace("+", "").replace(",", ""))

        if country_new_deaths == "":
            country_new_deaths = 0
        else:
            country_new_deaths = int(
                countries[Country_ID_Selected].find_all("td")[5].text.replace("+", "").replace(",", ""))

        if country_total_recovered == "":
            country_total_recovered = 0
        else:
            country_total_recovered = int(
                countries[Country_ID_Selected].find_all("td")[6].text.replace("+", "").replace(",", ""))

        if country_new_recovered == "":
            country_new_recovered = 0
        else:
            country_new_recovered = int(
                countries[Country_ID_Selected].find_all("td")[7].text.replace("+", "").replace(",", ""))

        if country_total_active == "":
            country_total_active = 0
        else:
            country_total_active = int(
                countries[Country_ID_Selected].find_all("td")[8].text.replace("+", "").replace(",", ""))

        if country_total_serious == "":
            country_total_serious = 0
        else:
            country_total_serious = int(
                countries[Country_ID_Selected].find_all("td")[9].text.replace("+", "").replace(",", ""))

        if country_total_tests == "":
            country_total_tests = 0
        else:
            country_total_tests = int(
                countries[Country_ID_Selected].find_all("td")[12].text.replace("+", "").replace(",", ""))

        country_data = {
            "Country_Name": country,
            "Total_Cases": country_total_cases,
            "New_Cases": country_new_cases,
            "Total_Deaths": country_total_deaths,
            "New_Deaths": country_new_deaths,
            "Total_Recovered": country_total_recovered,
            "New_Recovered": country_new_recovered,
            "Active_Cases": country_total_active,
            "Serious_Cases": country_total_serious,
            "Total_Tests": country_total_tests
        }

        all_country_data.append(country_data)
    return all_country_data
