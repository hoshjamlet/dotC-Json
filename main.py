import json


#filename = 'N104XA Single Sim Installed Product details.json'
filename = 'testjson.json'
with open(filename, 'r') as data_file:
    json_data = data_file.read()    
data = json.loads(json_data)


def find_product_items(data, level=0, results=None):
    if results is None:
        results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'productItem':
                for item in value: 
                    #print(item['businessId'])
                    results.append((item['businessId'], level, 'BusinessId'))
                    results.append((item['name'], level, 'Name'))
            find_product_items(value, level + 1, results)
    elif isinstance(data, list):
        for item in data:
            find_product_items(item, level, results)
    return results

def main():
    product_items = find_product_items(data)
    for x in product_items:
        spaces = x[1]
        print('   '*spaces,x[2],':', x[0])



main()