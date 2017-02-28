from views.email_password import pwd

def sendEmail(email, name, text):
	import smtplib, string

	fromaddr = 'ReformMiDems@gmail.com'
	toaddrs  = email
	subj = "Thank you for signing up!"

	msg  = "Hello %s," %(name)
	msg = msg + "\r\n" + text

	body = str.join("\r\n", (
		"From: %s" % fromaddr,
		"To: %s" % toaddrs,
		"Subject: %s" % subj,
		msg,
	       ))


	# Gmail Login

	username = 'reformmidems@gmail.com'
	password = pwd

	# Sending the mail

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, [toaddrs], body)
	server.quit()

message = """
This email is to inform you that we recieved your application to the Michigan Democratic Party.

We shall convert your application to paper form and drop it off in the next few weeks.

Thank you so much for using the app. We shall update you with membership updates.

Thanks,

Ryan Wiley (creator of the app)

"""
