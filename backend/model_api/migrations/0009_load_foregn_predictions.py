# Generated by Django 3.0.4 on 2020-06-11 18:42

from django.db import migrations
from typing import List
import urllib.request
import urllib.error
import io
import csv
import datetime
import _thread

# Static model predictions from other universities/research labs.
class StaticForeignModel:
    def __init__(self, 
                 us_death_prediction_url: str,
                 name: str,
                 description: str = ""):
        self.us_death_prediction_url = us_death_prediction_url
        self.name = name
        self.description = description

STATIC_FOREIGN_MODELS = [
    StaticForeignModel(
        us_death_prediction_url="https://raw.githubusercontent.com/reichlab/covid19-forecast-hub/master/data-processed/CU-select/2020-06-11-CU-select.csv",
        name="Columbia University - Select (US state level only)",
        description="This metapopulation county-level SEIR model makes projections of future COVID-19 deaths. \
        The predictions are provided by the Shaman Lab at Columbia University. \
        More info on https://github.com/shaman-lab/COVID-19Projection."
    ), 

    StaticForeignModel(
        us_death_prediction_url="https://raw.githubusercontent.com/reichlab/covid19-forecast-hub/master/data-processed/UCLA-SuEIR/2020-06-07-UCLA-SuEIR.csv",
        name="UCLA - SuEIR (US state level only)",
        description="The SuEIR model is a variant of the SEIR model considering both untested and unreported cases. \
        The model takes reopening into consideration and assumes that the contact rate will increase after the reopen.\
        The predictions are provided by the UCLA Statistical Machine Learning Lab. \
        More info on https://github.com/reichlab/covid19-forecast-hub/tree/master/data-processed/UCLA-SuEIR."
    ),

    StaticForeignModel(
        us_death_prediction_url="https://raw.githubusercontent.com/reichlab/covid19-forecast-hub/master/data-processed/MIT_CovidAnalytics-DELPHI/2020-06-08-MIT_CovidAnalytics-DELPHI.csv",
        name="MIT - DELPHI (US state level only)",
        description="This model makes predictions for future cases based on a heavily modified SEIR model taking \
        into account underdetection and government intervention. The predictions are provided by the COVIDAnalytics Research Team at MIT. \
        More info on https://github.com/COVIDAnalytics/DELPHI."
    ), 

    StaticForeignModel(
        us_death_prediction_url="https://raw.githubusercontent.com/reichlab/covid19-forecast-hub/master/data-processed/JHU_IDD-CovidSP/2020-06-07-JHU_IDD-CovidSP.csv",
        name="JHU - IDD (US state level only)",
        description="County-level metapopulation model with commuting and stochastic SEIR disease dynamics. \
        The predictions are provided by the Johns Hopkins ID Dynamics COVID-19 Working Group. \
        More info on https://github.com/HopkinsIDD/COVIDScenarioPipeline."
    )
]

def load_csv(apps, url):
    """
    Reads the given csv url and returns a list of Covid19PredictionDataPoint
    objects. Only the date, area, and val fields on the objects are set. Note
    that the objects have not been saved into the database yet.
    :param apps: Django apps object.
    :param path: Path to CSV with prediction data.
    :return: List of Covid19PredictionDataPoint objects (NOT SAVED YET).
    """
    Area = apps.get_model('model_api', 'Area')
    Covid19PredictionDataPoint = apps.get_model(
        'model_api', 'Covid19PredictionDataPoint')

    try:
        f = io.StringIO(urllib.request.urlopen(url).read().decode('utf-8')) 
    except urllib.error.HTTPError as httpe:
        print("A HttpError is found when loading data from" + url)
        return []
    except urllib.error.URLError as urle:
        print("A URLError is found when loading data from" + url)
        return []
    

class Migration(migrations.Migration):

    dependencies = [
        ('model_api', '0008_load_predictions'),
    ]

    operations = [
    ]
