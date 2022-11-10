import urllib.request
import json

# this module needs to be installed separately
# in PyCharm you can install the package if its not found!

import var_dump as vd

# get internet data
url = 'https://kimiquotes.herokuapp.com/quote'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# tarvittava data on nyt data-muuttujassa!
data = json.loads(raw_data)
vd.var_dump(data)

