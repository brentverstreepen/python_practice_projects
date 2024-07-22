import pandas as pd
import numpy as np

# Data scraped from TV using tvdatafeed
data = pd.read_csv("msft.csv")
data["datetime"] = pd.to_datetime(data["datetime"])
data.set_index("datetime", inplace=True)
print(data)