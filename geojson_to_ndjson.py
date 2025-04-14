import geojson
import json

# Load your GeoJSON file
with open('crime_output_lsoa.geojson', 'r') as f:
    data = json.load(f)

# Write to NDJSON file (one feature per line)
with open('crime_output_lsoa.ndjson', 'w') as outfile:
    for feature in data.get('features',[]):
        json.dump(feature, outfile)
        outfile.write('\n')