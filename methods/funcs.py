import methods.api as api
import pandas as pd

def get_data():
    for i in api.Encumbrances():
        pd.DataFrame.from_dict(api.Encumbrances()[i]["data"]).to_csv(f'./static/results/{i[:-9]}_data.csv', index=False)
    for i in api.Permits():
        pd.DataFrame.from_dict(api.Permits()[i]["data"]).to_csv(f'./static/results/backup/{i[:-16]}_data.csv', index=False)