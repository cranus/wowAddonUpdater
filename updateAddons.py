import json 
import urllib.request
import zipfile

with open('addons.json') as f:
    data = json.load(f)
    
config = data["config"]

for (i, addon) in enumerate(data["addons"]):
    print ("Download: " + addon["name"])
    file = config["tmp"] + addon["name"]+'.zip'
    urllib.request.urlretrieve(addon["url"], file)
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall(config["interface"])
    zip_ref.close()
    print ("Download: " + addon["name"] + " done")
