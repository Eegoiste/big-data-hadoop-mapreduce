import pandas as pd

# preprocesing Reviews.csv file to do job
df = pd.read_csv('Reviews.csv')
print(df.info())

df.to_csv('prep_reviews.tsv', sep='\t', header=False, index=False)