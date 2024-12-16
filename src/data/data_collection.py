import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import yaml
#test_size = yaml.safe_load(open("params.yaml"))["data_collection"]["test_size"]

def load_params(filepath: str) -> float:
    try:
        with open(filepath,'r') as file:
            params = yaml.safe_load(file)
        return params["data_collection"]["test_size"]
    except Exception as e:
        raise Exception(f"Error loading parameter from {filepath}:{e}")

#data = pd.read_csv(r'C:\Users\u350272\Desktop\projectdata\e2eflowdata\water_potability.csv')
def load_data(filepath:str) ->pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error Loading data from {filepath}:{e}")

#train_data, test_data=train_test_split(data, test_size=0.2, random_state=42)
def split_data(data: pd.DataFrame, test_size:float) -> tuple[pd.DataFrame,pd.DataFrame]:
    try:
        return train_test_split(data, test_size=test_size, random_state=42)
    except ValueError as e:
        raise Exception(f"Error splitting data:{e}")
    


def save_data(df: pd.DataFrame, filepath:str) -> None:
    try:
        df.to_csv(filepath,index=False)
    except Exception as e:
        raise Exception(f"Error saving data to {filepath}:{e} ")

#data_path = os.path.join("data", "raw")
def main():
    try:
        data_filepath = r'C:\Users\u350272\Desktop\projectdata\e2eflowdata\water_potability.csv'
        params_filepath = r'params.yaml'
        raw_data_path = os.path.join("data", "raw")

        data = load_data(data_filepath)
        test_size = load_params(params_filepath)

        train_data, test_data = split_data(data, test_size)
        os.makedirs(raw_data_path)

        save_data(train_data,os.path.join(raw_data_path,"train_data.csv"))
        save_data(test_data,os.path.join(raw_data_path,"test_data.csv"))
    except Exception as e:
        raise Exception(f"An error occurred:{e}")

if __name__=="__main__":
    main()