# Credentials/Input to get the token
from random import randint

#
token_url = 'https://identity.qa-regalpay.io/connect/token'
Username = 'chethan@regal-us.com'
Password = 'Chethan@1995'
client_id = 'AdminPortal'
client_secret = 'QN9wyWRJPdr2KTYp'
grant_type = 'password'
Scope = ' iam:company-account:admin openid'


# Urls
url = 'https://api.qa-regalpay.io'
CompanyAccounts = '/iam/company-account'
Entity = '/iam/entities'
Groups = '/iam/groups'
Users = '/iam/users'
administrators = '/administrators'
applications = '/applications'
clone = '/clone'
permissions = '/permissions'
users = '/users'
#
random_value = randint(100, 20000000)
random_value1 = randint(11111, 99999)

ExpectedCode200 = 200
ExpectedCode201 = 201
ExpectedCode400 = 400


address1 = 'Lakeview'
address2 = 'Sunend'
address3 = 'RiverBay'
city = 'Boston'
state = 'Washington'
zip = '12345'
country = 'USA'
countryCode = 'US'