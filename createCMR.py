import sys
sys.path.append('Desktop\docker\getData')
from getData import getData
from pipedrive.client import Client



clientSecret = '39fcabe84a47bf2351b2fb4e77aa07a05aa0c51b'
clientID = '418c0925f25a9b6e'
apiToken = '65001d59010b6b7edfc9bf1fee0535b82b74b1d2'  # data needs to autoryzation
companyDomain = 'edward-sandbox-9deccb'


def create_organization():
    url = 'https://companydomain.pipedrive.com/v1/organizations?api_token=' + apiToken
    client = Client(domain=url)  # autoryzation
    client.set_api_token(apiToken)

    data = {
        "name": getData.orgName,  # name of the organization
    }
    response = client.organizations.create_organization(data)


def get_organization():
    url = 'https://companydomain.pipedrive.com/v1/organizations?api_token=' + apiToken
    client = Client(domain=url)
    client.set_api_token(apiToken)

    helper = client.organizations.get_all_organizations()
    helper2 = (helper['data'])
    orgID = helper2[0]
    orgID = (orgID['id'])  # ID of company!!!!!!!!!!!!!
    return orgID


def add_users(how):
    # url = 'https://' + companyDomain + '.pipedrive.com/v1/persons/' + '?api_token=' + apiToken
    url = 'https://api.pipedrive.com/v1/persons?start=0&api_token=' + apiToken

    client = Client(domain=url)
    response = client.set_api_token(apiToken)
    count = 0
    orgID = get_organization()
    while count < how:
        data = {
            'name': getData.employees[count],  # add person with organization
            'org_id': orgID
        }

        response = client.persons.create_person(data)
        count += 1


def add_activiy(how):
    url = 'https://companydomain.pipedrive.com/v1/activities?api_token=' + apiToken
    client = Client(domain=url)
    client.set_api_token(apiToken)
    count = 0
    users = []
    while count < how:
        users.append(get_user(count + 1))

        print(users)
        data = {
            'subject': 'Call to the president',
            'type': 'Call',
            'org_id': get_organization(),  # add Call activity
            'done': 1,  # 0 means than activity is done.
            'person_id': users[count]
        }
        data2 = {
            'subject': 'Call to the minister',
            'type': 'Meeting',  # add meeting activity
            'org_id': get_organization(),
            'done': 1,
            'person_id': users[count]
        }
        count += 1
        client = Client(domain=url)
        client.set_api_token(apiToken)
        response = client.activities.create_activity(data)
        response = client.activities.create_activity(data2)


def get_user(howMany):
    url = 'https://api.pipedrive.com/v1/persons?start=0&api_token=' + apiToken
    client = Client(domain=url)
    response = client.set_api_token(apiToken)
    count = 0
    personID = []
    while count < howMany:
        helper = client.persons.get_all_persons()
        helper2 = helper['data']
        personID = helper2[count]
        personID = personID['id']  # ID persons, all persons !!!!!!!!!!!!!
        count += 1

    return personID


howMany = len(getData.employees)
create_organization()
add_users(howMany)
add_activiy(howMany)
get_user(howMany)
