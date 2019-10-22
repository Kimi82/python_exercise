from pipedrive.client import Client

clientSecret = '39fcabe84a47bf2351b2fb4e77aa07a05aa0c51b'
clientID = '418c0925f25a9b6e'
apiToken = '65001d59010b6b7edfc9bf1fee0535b82b74b1d2'
companyDomain = 'edward-sandbox-9deccb'
#url = 'https://' + companyDomain + '.pipedrive.com/v1/deals?api_token=' + apiToken
rly = 'https://edward-sandbox-9deccb.pipedrive.com/v1/deals?api_token=65001d59010b6b7edfc9bf1fee0535b82b74b1d2'

client = Client(clientID, clientSecret)

url = client.authorization_url(rly)
token = client.exchange_code(rly, 'CODE')
client.set_access_token('ACCESS_TOKEN')
token = client.refresh_token('REFRESH_TOKEN')


def create_organization():
    data = {
        "title": 'NIE',
    }
    response = client.organizations.create_organization(data)

def add_users(how):
    count = 0
    while count < how:
        data = {
         'title': 'Employee'+ str(count)
        }
        response = client.persons.create_person(data)
        count+=1

create_organization()
#add_users(2)