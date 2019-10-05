import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('UserName111')
EMAIL_PASSWORD = os.environ.get('Password')



msg = EmailMessage()
msg['Subject'] = 'Verify yourself here'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'malarahul465@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
	<title>email</title>
	<style type="text/css">
		.email-backgound{
	backgorund: #eee;
	padding:10px;
}
.email-container{
	max-width: 500px
	backgrund: white;
	font-family: sans-serif;
	margin: 0 auto;
	overflow: hidden;
	border-radius: 5px;
	text-align: center;
}
img{max-width: 100%;}
a{
f	color : #3D87F5;
}
p{
	margin: 20px;
	font-size: 18px;
	font-weight: 300;
	color: #666;
	line-height: 1.5;
}
.cta{
	margin: 20px}
	.cta a {
		text-decoration: none;
		display: inline-block;
		background: #3D87F5;
		color: white;
		padding: 10px 20px 10px;
		border-radius: 5px;
	}

.footer-junk{
	@extent .email-container
	background: none;
	padding: 20px;
	font-size: 12px;
}


	</style>
</head>
<body>
<fieldset>
	<legend>.</legend>
	<div class="email-background">
		<div class="email-container" style="max-width: 500px
	backgrund: white;font-family: sans-serif;margin: 0 auto;overflow: hidden;border-radius: 5px;text-align: center;">
			<img src="https://content-static.upwork.com/blog/uploads/sites/3/2018/08/30134609/LogoMakr.png" hight="70" width= "100" style="max-width: 100%;">
			<h2>Hey user!,</h2>
			<p style="margin: 20px;font-size: 18px;font-weight: 300;color: #666;line-height: 1.5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thanks for signing up for a &lt;our_site/project_name&gt;</p>
			<p style="margin: 20px;font-size: 18px;font-weight: 300;color: #666;line-height: 1.5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Here's the verification code you need to continue with &lt;our_site/project_name&gt;</p>
			<div class="cta" style="margin: 20px;">
				<a href="#!"style="color: white;text-decoration: none;display: inline-block;background: #3D87F5;padding: 10px 20px 10px;border-radius: 5px;">Verify</a>
			</div>
			
		</div>
	</div>
</fieldset>
<div class="footer-junk" style="@extent .email-container
	background: none;padding: 20px;font-size: 12px;">
				&lt;our_site/project_name&gt; | <a href="#!" style="color: #3D87F5;">Unsubscribe</a>
			</div></body></html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



print("done")
