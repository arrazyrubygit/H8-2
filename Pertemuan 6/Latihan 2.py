import numpy as np
import pandas as pd

revenue = pd.Series([5555,7000,1980])

city_revenue = pd.Series([5000,6000,7000], index=["Jakarta","Bandung","Surabaya"])

city_employee = pd.Series({"Jakarta":10,"Bandung":5,"Surabaya":15})

city_data = pd.DataFrame({"revenue":city_revenue,"Employee":city_employee})
print(city_data)