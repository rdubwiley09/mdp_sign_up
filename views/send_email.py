from views.email_password import pwd, api_key
import requests

def sendEmail(email, name, subj, text, anonymous):
	import smtplib, string

	if anonymous:
		toaddrs  = [email]
	else:
		toaddrs = [email,'wileyrya@gmail.com']

	msg  = "Hello %s," %(name)
	msg = msg + "\r\n" + text

	requests.post(
		"https://api.mailgun.net/v3/reformmidems.com/messages",
		auth=("api", api_key),
		data = {
			"from": "Ryan Wiley <mailgun@reformmidems.com>",
			"to": toaddrs,
			"subject": subj,
			"text": msg
		}
	)

def successMessage(firstName, lastName, expirationDate):
	success_message = """
	We found a record of your membership!

	Name: %s %s

	Your membership will expire on: %s

	Thanks,

	Ryan Wiley (creator of the app)

	""" %(firstName, lastName, expirationDate)

	return success_message


message = """
This email is to inform you that we recieved your application to the Michigan Democratic Party.

We shall convert your application to paper form and drop it off in the next few weeks.

Thank you so much for using the app. We shall update you with membership updates.

Thanks,

Ryan Wiley (creator of the app)

"""

fail_message = """
This email is to inform you that we could not find you in our records.

Please sign up here: http://www.reformmidems.com/

Thanks,

Ryan Wiley (creator of the app)

"""

not_dropped_off = """
While we do have a record of you filling out your form, we have yet to drop off your application.

It usually takes a few weeks for forms to be dropped off.

If you have any questions please email Ryan at: wileyryra@gmail.com

Thanks,

Ryan Wiley (creator of the app)
"""
