import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataIngestor import DataIngestor
from DataPreprocessor import DataPreprocessor

ingest = DataIngestor("googleplaystore.csv").extract_()

preprocess = DataPreprocessor(ingest)
df = preprocess.cleaning()

print(df.info())
print(preprocess.df_origin.info())