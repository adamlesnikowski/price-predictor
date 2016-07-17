#This script downloads house share CSVs and geojson's into the pwd. 
#Pulls Chicago's CSVs as a default

import urllib2

input_url = raw_input("Enter your city's listings.csv.gz URL (Hit enter for default of Chicago): ")

if input_url == '':
  print('Default of http://data.insideairbnb.com/united-states/il/chicago/2015-10-03/data/listings.csv.gz used')
  input_url = 'http://data.insideairbnb.com/united-states/il/chicago/2015-10-03/data/listings.csv.gz'

#Get base url
arr = input_url.split('/')
arr.remove(arr[-1])
arr.remove(arr[-1]) #Removes last two elements
base_url = '/'.join(arr)  #Joing arr back to a url
base_url = base_url + '/' #add trailing /

#URL ends
ends = ['data/listings.csv.gz',
'data/calendar.csv.gz',
'data/reviews.csv.gz',
'visualisations/listings.csv',
'visualisations/reviews.csv',
'visualisations/neighbourhoods.csv',
'visualisations/neighbourhoods.geojson']

#Get CSVs
for end in ends:
  url = base_url + end
  print("Gettting %s..." % url)
  response = urllib2.urlopen(url)
  html = response.read()
  out_file_name = end.split('/')[1]
  with open(out_file_name, 'w+') as f:
    f.write(html)
    
print("Enjoy!")
