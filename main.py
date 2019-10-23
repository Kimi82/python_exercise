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
    # url = 'https://' + companyDomain + '.pipedrive.com/v1/persons/' + '1906' + '?api_token=' + apiToken
    url = 'https://api.pipedrive.com/v1/persons?start=0&api_token=' + apiToken

    client = Client(domain=url)
    response = client.set_api_token(apiToken)
    count = 0
    while count < how:
        data = {
            'name': 'Employe' + str(count),
            'org_id': get_organization()
        }
        count += 1
        response = client.persons.create_person(data)




def add_activiy():
    url = 'https://companydomain.pipedrive.com/v1/activities?api_token=' + apiToken
    client = Client(domain=url)
    client.set_api_token(apiToken)

    data = {
        'subject':'Call to the president ',
        'type':'Call'
    }
    response = client.activities.create_activity(data)

def get_user(how):
    url = 'https://api.pipedrive.com/v1/persons?start=0&api_token=' + apiToken
    client = Client(domain=url)
    response = client.set_api_token(apiToken)
    count = 0
    personID = []
    helper2 = []
    while count < how:
        helper = client.persons.get_all_persons()
        helper2.appe(helper['data'])
        personID = helper2[count]
        personID[1] = (personID['id'])  # ID of company!!!!!!!!!!!!!
        count +=1
        print(helper2)

#create_organization()
#add_users(1)
#add_activiy()
get_user(2)
