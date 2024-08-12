import requests

def info(card):
    while True:
        response = requests.get('https://bins.antipublic.cc/bins/' + card[:6])
        
        if 'not found' in response.text:
            return ("------", "------", "------", "------", "------", "------")
        elif 'Cloudflare' in response.text:
        	break
        elif response.status_code == 200:
            break

    if response.status_code == 200:
        data = ['brand', 'type', 'level', 'bank', 'country_name', 'country_flag']
        result = []
        
        for field in data:
            try:
                result.append(response.json()[field])
            except:
                result.append("------")  
    
        return tuple(result)
    else:
    	return ("------", "------", "------", "------", "------", "------")