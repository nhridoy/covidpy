# covidpy
## _Detailed Regular Information about World's Covid19 Data_

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI download total](https://img.shields.io/pypi/dt/ansicolortags.svg)](https://pypi.org/project/covidpy/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/covidpy/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/hridoyboss12/Covidpy)


## Features

- Get Worlds Covid19 Status
- Get All Country's Covid19 Status
- Get Individual Countriy's Covid19 Status

## Requirements
```
python >= 3.6
```
## Installation

Install the dependencies and devDependencies and start the server.

```
pip install covidpy
```

## Dependencies
```
pandas
requests
beautifulsoup4
```


## Functions

Instructions on how to use them in your own application are linked below.

| Functions | Work |
| ------ | ------ |
| WorldData() | Get Worldwide Data |
| ListCountries() | Get Total Country List |
| CountryData(country) | Get Individual Country's Data |
| AllData() | Get All Country's Data |

## Usage
### Get Worldwide Data
```
from covidpy import WorldData

world = WorldData()
print(world)
```

Result:

```
{
    'Total_Cases': 161080616, 
    'New_Cases': 3853,
    'Total_Deaths': 3345018,
    'New_Deaths': 274,
    'Total_Recovered': 139849282,
    'New_Recovered': 2483,
    'Active_Cases': 17886316,
    'Serious_Cases': 105218
}
```

### Get Country List
```
from covidpy import ListCountries

countries = ListCountries()
print(countries)
```

Result:

```
     Country_ID      Country_Name
1             1     NORTH AMERICA
2             2              ASIA
3             3     SOUTH AMERICA
4             4            EUROPE
5             5            AFRICA
..          ...               ...
225         226  MARSHALL ISLANDS
226         227             SAMOA
227         228      SAINT HELENA
228         229        MICRONESIA
229         230             CHINA
```


### Get All Countries Data
```
from covidpy import AllData

all_data = AllData()
print(all_data)
```

Result:

```
[
    {
        'Country_Name': 'USA', 
        'Total_Cases': 33586136, 
        'New_Cases': 0, 
        'Total_Deaths': 597785, 
        'New_Deaths': 0, 
        'Total_Recovered': 26620229, 
        'New_Recovered': 0, 
        'Active_Cases': 6368122, 
        'Serious_Cases': 8707, 
        'Total_Tests': 461476543
    },
    {
        'Country_Name': 'INDIA', 
        'Total_Cases': 23702832, 
        'New_Cases': 0, 
        'Total_Deaths': 258351, 
        'New_Deaths': 0, 
        'Total_Recovered': 19728436, 
        'New_Recovered': 0, 
        'Active_Cases': 3716045, 
        'Serious_Cases': 8944, 
        'Total_Tests': 307583991
    },
    ...
]
```

### Get Individual Country Data
```
from covidpy import CountryData

country = CountryData("Bangladesh")
print(country)
```

Result:

```
{
    'Country_Name': 'BANGLADESH', 
    'Total_Cases': 777397, 
    'New_Cases': 0, 
    'Total_Deaths': 12045, 
    'New_Deaths': 0, 
    'Total_Recovered': 718249, 
    'New_Recovered': 0, 
    'Active_Cases': 47103, 
    'Serious_Cases': 1120, 
    'Total_Tests': 5677222
}
```

## License

MIT



