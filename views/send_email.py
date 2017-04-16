from views.email_password import pwd, api_key
import requests

def sendEmail(email, name, text):
	import smtplib, string

	fromaddr = 'ReformMiDems@gmail.com'
	toaddrs  = [email, 'wileyrya@gmail.com']
	subj = "Thank you for signing up!"

	msg  = "Hello %s," %(name)
	msg = msg + "\r\n" + text

	requests.post(
		"https://api.mailgun.net/v3/reformmidems.com/messages",
		auth=("api", api_key),
		data = {
			"from": "no-reply <mailgun@reformmidems.com>",
			"to": toaddrs,
			"subject": subj,
			"text": msg
		}
	)

message = """
This email is to inform you that we recieved your application to the Michigan Democratic Party.

We shall convert your application to paper form and drop it off in the next few weeks.

Thank you so much for using the app. We shall update you with membership updates.

Thanks,

Ryan Wiley (creator of the app)

"""
