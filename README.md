# Salt-Spring-Exchange-Notfifier
This tool scrapes a desired page of the salt spring exchange and notifies the user of the latest posting.
I built it to help me find a good deal on a used car, which was a success!
I would leave my computer running with this script on a timer so it wouldnt miss any new postings and would notify me every time a new one came up.
I had my pick of the lot!

Setup: 
1. Use pip to install beautifulSoup and Twillio
2. Make a twillio account, add valid auth_token and account_sid
3. Add desired phone numbers, (will text these numbers when script is run)
4. Add the desired URL (must be a page of the salt spring exchange, obviosly)
5. You can either set up a job to call the .bat file, or simply run the ControlSMSSender.py to recieve a notifcation on what the lastest entry is.
6. It will not notify the user if no new postings exist, but it must be run to discover new postings

Good luck! 
