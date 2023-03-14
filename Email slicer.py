#email slicer

email = input("Enter your email address : ")

#code to validate email 
#check whether dot and @ present or not
if('.' not in email and '@' not in email):
	print("Email must contain @ and .")
#if yes then check for valid email
else:							
	atposition = email.index('@')
	dotposition = email.index('.')
	if(atposition<1):
		print("Enter valid input ")
	elif(dotposition<atposition):
		print("enter valid email!")
	else:
		afterat = atposition +1
		username = email[0:atposition]
		domainName = email[afterat:]
		print("The username is : ",username)
		print("The domain name is : ",domainName)