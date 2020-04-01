print("HEllo")
from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(['flu'])

# Note: make better version w/o pytrends, using requests

df = pytrends.interest_by_region(resolution='CITY')
print(df.head())