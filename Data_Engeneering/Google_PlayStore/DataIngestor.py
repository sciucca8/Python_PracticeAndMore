import pandas as pd
import numpy as np

class DataIngestor:
    def __init__(self, csv):
        self.csv = csv
    
    def extract_(self):
        df = pd.read_csv(self.csv)
        return df