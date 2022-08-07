import json
import urllib.request
from num2words import num2words

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    source = json.dumps(output, indent=4, sort_keys=True)

    for i in output['bpi']:
        result = int(float(output['bpi'][i]['rate'].replace(",", "")))
        full = (((num2words(result)).replace("-", " ")).replace(",", "")).upper()
        print(result)
        print(full)

except Exception as e:
    print(str(e))
