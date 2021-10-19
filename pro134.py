#importing libraries
import pandas as pd
from pandas.core.frame import DataFrame

#Loading file as df 
df = pd.read_csv("star_with_gravity.csv")
#removing unwanted columns

df['Distance']=df['Distance'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float') 

distance = [] 

for x in df.Distance:
  if float(x) <= 100:
    distance.append(True)
  else:
    distance.append(False)

is_distance = pd.Series(distance)

star_distance = df[is_distance]
star_distance.reset_index(inplace=True, drop=True)
print(star_distance.head())

gravity = []
for data in star_distance.Gravity:
  if data<=350 and data>=150 :
    gravity.append(True)
  else:
    gravity.append(False)

is_gravity = pd.Series(gravity)
filtered_stars = star_distance[gravity]
print(filtered_stars.head())

filtered_stars.to_csv("filtered_stars.csv")
