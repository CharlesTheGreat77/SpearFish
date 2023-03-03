# SpearFish
Spear Phishing Presentation


# Prerequisites
1. Enable 2FA
2. Go to https://myaccount.google.com/u/4/apppasswords and create a name for your "app" and copy the token gmail generates for you.
3. Copy TOKEN and save it to a notepad or of that sort. ( we are gonna need it )

# Edit Fish.py file
1. change "<gmail_account@gmail.com>" to YOUR email. 
2. Change "<TOKEN>" with your gmail token. 
3. Save file

# usage
```
python3 fish.py -t example@gmail.com -u https://phishingURL.com -n John
```
Were -t is the target email, -u is your phishing url, and -n is the first name of your target
