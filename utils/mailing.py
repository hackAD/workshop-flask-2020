import smtplib, utils.emailconfig

def email(addr, msg):
    message = '''Subject: {sub}\nFrom: {fro}\nTo: {users}\n{msg}'''.format(
			sub = "Hi", 
			fro = utils.emailconfig.EmailAddress, 
			users = addr,
			msg = msg)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(utils.emailconfig.EmailAddress, 
    utils.emailconfig.Password)
    
    server.sendmail(utils.emailconfig.EmailAddress,addr,message)
    server.quit()
    