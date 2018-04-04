import pandas as pd

def combine(cols):
	if pd.isnull(cols[1]):
		return cols[0]
	else:
		print(cols[0] + cols[1])
		return cols[0] + cols[1]

df = pd.read_csv("us_cities_states_counties.csv", skiprows = 1, names = ['City|State short|State full|County|City alias',''])

df['City|State short|State full|County|City alias'] = df[['City|State short|State full|County|City alias','']].apply(combine, axis = 1)
del df['']

df.to_csv("us_cities_states_counties.csv", index= False)