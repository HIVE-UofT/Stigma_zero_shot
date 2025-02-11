from requests import get
import json
import time

url = 'https://www.reddit.com/r/diabetes/hot.json'
after = None
params = {}

for i in range(1, 101):
    params = {'after': after, 't': 'year', 'limit': 100}
    try:
        res = get(url, params)
        data = res.json()
    except:
        print('error occured')
        break
    
    with open(f'reddit_t2/data{i}.json', 'w') as f:
        f.write(json.dumps(res.json()))
        f.close()

    after = data['data']['after']
    time.sleep(0.5)

    
