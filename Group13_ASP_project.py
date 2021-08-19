import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

excel = pd.read_excel("IMVA.xls", sheet_name="IMVA")

countries = excel ['Periods'].str.split(' ', n=1, expand=True)
print(countries)
