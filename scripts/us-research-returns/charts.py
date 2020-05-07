import pandas as pd

import matplotlib.pyplot as plt

default_extracted_data_path = 'data/us-research-returns/'
df = pd.read_csv((default_extracted_data_path +
                  'research_data_5_factors_2x3_annual.csv'))
ax = plt.gca()
df.plot(kind='line', x=0, y=5, ax=ax)
plt.xlabel('Year')
plt.ylabel('CMA')
plt.show()
