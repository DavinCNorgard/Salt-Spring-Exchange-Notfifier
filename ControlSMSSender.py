from twilio.rest import *
import SSIEScraper

def formatMessage(formattedArticle):
    formattedString = formattedArticle.title + formattedArticle.price + formattedArticle.time + '\n' + formattedArticle.link
    return formattedString

def sendToClients(formatted):

    client.messages.create(
        to="2502216574",
        from_="+19124913486",
        body=formatted
    )

    client.messages.create(
        to="2502210051",
        from_="+19124913486",
        body=formatted
    )



account_sid = 'AC694d00904b775b76a46011c864c84999'
auth_token = '0b5fe67ad3fa4633c42050b088536012' #Good luck using this
client = Client(account_sid, auth_token)
changed = False

formattedArticlesWithTime = SSIEScraper.ScrapeExchangePage("https://saltspringexchange.com/list/?s=&scat=21&lat=0&lng=0&radius=50&st=ad_listing")

f = open('latestEntry.txt', 'r')
previousEntry = f.read()
f.close()
for formattedArticle in formattedArticlesWithTime:

    if(previousEntry == formattedArticle.title):
        break
    else:
        print(formatMessage(formattedArticle))
        sendToClients(formatMessage(formattedArticle));
        changed = True;

if(changed):
    print('writing to file')
    f = open('latestEntry.txt', 'w')
    f.write(formattedArticlesWithTime[0].title)
    f.close()

