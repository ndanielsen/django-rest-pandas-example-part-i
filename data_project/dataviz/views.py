import os

from django.shortcuts import render
from django.conf import settings

from rest_pandas import PandasSimpleView
import pandas as pd

class SimpleDataView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        data_file = os.path.join(str(settings.BASE_DIR), 'dataviz', 'data', 'dd7c7a92659b4f4a8971e9addacbf2db_51.csv')
        df = pd.read_csv(data_file)
        df['COUNT'] = 1
        df_wards = df.groupby(['WARD']).COUNT.sum().reset_index()
        df_wards['WARD'] = 'Ward' + ' ' + df_wards.WARD.apply(str)
        return df_wards
