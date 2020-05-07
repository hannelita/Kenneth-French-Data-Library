import urllib.request
import csv
import zipfile

import os
from os import listdir
from os.path import isfile, join

import pandas as pd

#Auxiliar function to remove comments from CSV files

def add_comments_into_file(file, lines, bound):
    with open('FILE_COMMENTS.md', "a+") as readme:
      readme.write('Comments from file ' + file + ':\n')
      readme.writelines(lines[0:bound])
      readme.write('\n')

# Download data
default_path_for_data = 'archive/us-research-returns/'

print("Downloading raw files...")

fama_french_3_factors_source = 'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip'
fama_french_3_factors_archive = 'fama_french_3_factors.zip'
urllib.request.urlretrieve(fama_french_3_factors_source, default_path_for_data + fama_french_3_factors_archive)


fama_french_3_factors_weekly_source = 'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_weekly_CSV.zip'
fama_french_3_factors_weekly_archive = 'fama_french_3_factors_weekly.zip'
urllib.request.urlretrieve(fama_french_3_factors_weekly_source, default_path_for_data + fama_french_3_factors_weekly_archive)


fama_french_3_factors_daily_source = 'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip'
fama_french_3_factors_daily_archive = 'fama_french_3_factors_daily.zip'
urllib.request.urlretrieve(fama_french_3_factors_daily_source, default_path_for_data + fama_french_3_factors_daily_archive)


fama_french_5_factors_weekly_source = 'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip'
fama_french_5_factors_weekly_archive = 'fama_french_5_factors_weekly.zip'
urllib.request.urlretrieve(fama_french_5_factors_weekly_source, default_path_for_data + fama_french_5_factors_weekly_archive)


fama_french_5_factors_daily_source = 'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_daily_CSV.zip'
fama_french_5_factors_daily_archive = 'fama_french_5_factors_daily.zip'
urllib.request.urlretrieve(fama_french_5_factors_daily_source, default_path_for_data + fama_french_5_factors_daily_archive)


# Extract
print("Raw Zip files now being extracted: ")

zipfiles = [f for f in listdir(default_path_for_data) if isfile(join(default_path_for_data, f))]
print(zipfiles)

default_extracted_data_path = 'data/us-research-returns/'

for f in zipfiles:
  with zipfile.ZipFile((default_path_for_data + f), 'r') as extractor:
    extractor.extractall(default_extracted_data_path)

print("Files extracted to CSV: ")

csvfiles = [f for f in listdir(default_extracted_data_path) if isfile(join(default_extracted_data_path, f))]
print(csvfiles)

for bad_csv_file in csvfiles:
  os.rename((default_extracted_data_path + bad_csv_file), (default_extracted_data_path + bad_csv_file.lower()))

print("Renaming CSV files: ")
csvfiles = [f for f in listdir(default_extracted_data_path) if isfile(join(default_extracted_data_path, f))]
print(csvfiles)




# Individual treatement of files
# research_data_5_factors_2x3.csv; splits into two csv files
with open((default_extracted_data_path + 'f-f_research_data_5_factors_2x3.csv'), "r") as file:
  lines = file.readlines()
  add_comments_into_file('f-f_research_data_5_factors_2x3.csv', lines, 2)
with open((default_extracted_data_path + 'research_data_5_factors_2x3.csv'), "w+") as file:
  file.writelines(lines[3:685])
with open((default_extracted_data_path + 'research_data_5_factors_2x3_annual.csv'), "w+") as file:
  file.writelines(lines[687:])
  with open('FILE_COMMENTS.md', "a+") as readme:
    readme.write(lines[686])
    readme.write('\n\n\n')

os.remove((default_extracted_data_path + 'f-f_research_data_5_factors_2x3.csv'))

df = pd.read_csv((default_extracted_data_path + 'research_data_5_factors_2x3.csv'))
print(df.info())

df = pd.read_csv((default_extracted_data_path + 'research_data_5_factors_2x3_annual.csv'))
print(df.info())


#f-f_research_data_5_factors_2x3_daily.csv
with open((default_extracted_data_path + 'f-f_research_data_5_factors_2x3_daily.csv'), "r") as file:
  lines = file.readlines()
  add_comments_into_file('f-f_research_data_5_factors_2x3_daily.csv', lines, 2)
with open((default_extracted_data_path + 'research_data_5_factors_2x3_daily.csv'), "w+") as file:
  file.writelines(lines[3:])

os.remove((default_extracted_data_path + 'f-f_research_data_5_factors_2x3_daily.csv'))

df = pd.read_csv((default_extracted_data_path + 'research_data_5_factors_2x3_daily.csv'))
print(df.info())


# f-f_research_data_factors.csv
with open((default_extracted_data_path + 'f-f_research_data_factors.csv'), "r") as file:
  lines = file.readlines()
  add_comments_into_file('f-f_research_data_factors.csv', lines, 2)
with open((default_extracted_data_path + 'research_data_factors.csv'), "w+") as file:
  file.writelines(lines[3:1128])

with open((default_extracted_data_path + 'research_data_factors_annual.csv'), "w+") as file:
  file.writelines(lines[1131:1225])
  with open('FILE_COMMENTS.md', "a+") as readme:
    readme.write(lines[1130] + '\n')
    readme.write(lines[1226])
    readme.write('\n\n\n')

os.remove((default_extracted_data_path + 'f-f_research_data_factors.csv'))

df = pd.read_csv((default_extracted_data_path + 'research_data_factors.csv'))
print(df.info())
df = pd.read_csv((default_extracted_data_path + 'research_data_factors_annual.csv'))
print(df.info())

# f-f_research_data_factors_daily.csv
with open((default_extracted_data_path + 'f-f_research_data_factors_daily.csv'), "r") as file:
  lines = file.readlines()
  add_comments_into_file('f-f_research_data_factors_daily.csv', lines, 2)
with open((default_extracted_data_path + 'research_data_factors_daily.csv'), "w+") as file:
  file.writelines(lines[4:24710])

os.remove((default_extracted_data_path + 'f-f_research_data_factors_daily.csv'))

df = pd.read_csv((default_extracted_data_path + 'research_data_factors_daily.csv'))
print(df.info())

# f-f_research_data_factors_weekly.csv
with open((default_extracted_data_path + 'f-f_research_data_factors_weekly.csv'), "r") as file:
  lines = file.readlines()
  add_comments_into_file('f-f_research_data_factors_weekly.csv', lines, 2)
with open((default_extracted_data_path + 'research_data_factors_weekly.csv'), "w+") as file:
  file.writelines(lines[4:4896])

os.remove((default_extracted_data_path + 'f-f_research_data_factors_weekly.csv'))

df = pd.read_csv((default_extracted_data_path + 'research_data_factors_weekly.csv'))
print(df.info())


