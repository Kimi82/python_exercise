from pipedrive.client import Client

clientSecret = '39fcabe84a47bf2351b2fb4e77aa07a05aa0c51b'
clientID = '418c0925f25a9b6e'
apiToken = '65001d59010b6b7edfc9bf1fee0535b82b74b1d2'
companyDomain = 'edward-sandbox-9deccb'


def create_organization():
    url = 'https://companydomain.pipedrive.com/v1/organizations?api_token=' + apiToken
    client = Client(domain=url)
    client.set_api_token(apiToken)

    data = {
        "name": 'My Organization',
    }
    response = client.organizations.create_organization(data)

def get_organization():
    url = 'https://companydomain.pipedrive.com/v1/organizations?api_token=' + apiToken
    client = Client(domain=url)
    client.set_api_token(apiToken)

    helper = client.organizations.get_all_organizations()
    helper2 = (helper['data'])
    orgID = helper2[0]
    orgID = (orgID['id']) #ID of company!!!!!!!!!!!!!
    return orgID

def add_users(how):

    #url = 'https://' + companyDomain + '.pipedrive.com/v1/persons/' + '1906' + '?api_token=' + apiToken
    url = 'https://api.pipedrive.com/v1/persons?start=0&api_token=' + apiToken

    client = Client(domain=url)
    response = client.set_api_token(apiToken)
    count = 0
    while count < how:
        data = {
            'name': 'Employe' + str(count),
            'org_id': get_organization()
      }
        count +=1
        response = client.persons.create_person(data)



create_organization()
add_users(5)
