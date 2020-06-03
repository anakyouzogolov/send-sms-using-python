# importing twilio 
from twilio.rest import Client 

# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

client = Client(account_sid, auth_token) 


# create a message 
message = "hello your welcome in twilio"
message = client.messages.create( 
							from_='+yyyyyyyyyyyy', 
							body =message, 
							to ='+xxxxxxxxxxxxx'
						) 

print(message.body) 


