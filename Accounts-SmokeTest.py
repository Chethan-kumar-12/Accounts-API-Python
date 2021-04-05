import json
import requests
# import sys

# sys.stdout = open('D:\Project\kote.txt', 'w')

from Generic import *

# Populate Access Token for Accounts App
data = {'grant_type': grant_type, 'username': Username, 'password': Password, 'scope': Scope}

# Get access token
access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=True,
                                      auth=(client_id, client_secret))

# Print access token
print(access_token_response.text)
tokens = json.loads(access_token_response.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

# POST ADD ADMIN TO COMPANY ACCOUNT
print("Post Add admin to Company account")
parameters = {
    "email": "chethan.kumar@mineraltree.com"
}

response = requests.post(url + CompanyAccounts + administrators, data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result1 = 'PASS'
else:
    result1 = 'FAIL'

# GET APPLICATIONS OF COMPANY ACCOUNT
print("Get Applications of Company account")
response = requests.get(url + CompanyAccounts + applications, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
ApplicationID1 = data['result'][1]['id']
print(ApplicationID1)
ApplicationID2 = data['result'][2]['id']
print(ApplicationID2)
ApplicationID3 = data['result'][3]['id']
print(ApplicationID3)
if response.status_code == ExpectedCode200:
    result2 = 'PASS'
else:
    result2 = 'FAIL'

# GET  COMPANY ACCOUNT INFO
print("Get Company account Info")
response = requests.get(url + CompanyAccounts, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result3 = 'PASS'
else:
    result3 = 'FAIL'

# ENTITY

# ADD AN ENTITY 1
print("Post Add Entity 1 to Company account")
parameters = {
    "name": "Entity1_" + str(random_value),
    "address1": address1,
    "address2": address2,
    "address3": address3,
    "city": city,
    "state": state,
    "zip": zip,
    "country": country,
    "countryCode": countryCode
}

response = requests.post(url + Entity, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
entityID1 = data['result']
print(entityID1)
if response.status_code == ExpectedCode200:
    result4 = 'PASS'
else:
    result4 = 'FAIL'

# ADD AN ENTITY 2
print("Post Add Entity 2 to Company account")
parameters = {
    "name": "Entity2_" + str(random_value),
    "address1": address1,
    "address2": address2,
    "address3": address3,
    "city": city,
    "state": state,
    "zip": zip,
    "country": country,
    "countryCode": countryCode
}

response = requests.post(url + Entity, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
entityID2 = data['result']
print(entityID2)
if response.status_code == ExpectedCode200:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

# UPDATE AN ENTITY
print("Put Update Entity to Company account")
parameters = {
    "name": "UpdatedEntity" + str(random_value),
    "address1": address1,
    "address2": address2,
    "address3": address3,
    "city": city,
    "state": state,
    "zip": zip,
    "country": country,
    "countryCode": countryCode
}

response = requests.put(url + Entity + '/' + entityID1, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result6 = 'PASS'
else:
    result6 = 'FAIL'

# ADD APPLICATIONS TO AN ENTITY 1
print("Post Add Applications to An Entity 1")
parameters = {
    "applicationIds": [
        ApplicationID1,
        ApplicationID2,
        ApplicationID3
    ]
}
response = requests.post(url + Entity + '/' + entityID1 + applications, data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

# ADD APPLICATIONS TO AN ENTITY 2
print("Post Add Applications to An Entity 2")
parameters = {
    "applicationIds": [
        ApplicationID1,
        ApplicationID2
    ]
}
response = requests.post(url + Entity + '/' + entityID2 + applications, data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

# GET APPLICATIONS OF AN ENTITY
print("Get Applications of an Entity")
response = requests.get(url + Entity + '/' + entityID1 + applications, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
permissionID1 = data['result'][0]['permissions'][0]['id']
print(permissionID1)
if response.status_code == ExpectedCode200:
    result9 = 'PASS'
else:
    result9 = 'FAIL'

# GET ALL ENTITIES
print("Get All Entities")
response = requests.get(url + Entity, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result10 = 'PASS'
else:
    result10 = 'FAIL'

# GROUPS & USERS

# ADD GROUP TO AN COMPANY ACCOUNT
print("Post Add Group 1 to Company Account")
parameters = {
    "groupName": "First_Group" + str(random_value),
    "groupDescription": "Desc" + str(random_value),
    "entityId": entityID1
}
response = requests.post(url + Groups, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
groupID1 = data['result']
print(groupID1)
if response.status_code == ExpectedCode200:
    result11 = 'PASS'
else:
    result11 = 'FAIL'

print("Post Add Group 2 to Company Account")
parameters = {
    "groupName": "Second_Group" + str(random_value),
    "groupDescription": "Desc" + str(random_value),
    "entityId": entityID2
}
response = requests.post(url + Groups, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
groupID2 = data['result']
print(groupID2)
if response.status_code == ExpectedCode200:
    result12 = 'PASS'
else:
    result12 = 'FAIL'

# UPDATE GROUP
print("PUT Update Group 2 to Company Account")
parameters = {
    "groupName": "UpdatedSecond_Group" + str(random_value),
    "groupDescription": "Desc" + str(random_value)
}
response = requests.put(url + Groups + '/' + groupID1, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result13 = 'PASS'
else:
    result13 = 'FAIL'

# CLONE GROUP
print("Clone Groups to Company Account")
parameters = {
    "entityIds": [
        entityID2
    ]
}
response = requests.post(url + Groups + '/' + groupID1 + clone, data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result14 = 'PASS'
else:
    result14 = 'FAIL'

# ADD PERMISSIONS TO GROUP
print("Post Permissions to Group")
parameters = {
    "permissionIds": [
        permissionID1
    ]
}
response = requests.post(url + Groups + '/' + groupID1 + permissions, data=json.dumps(parameters), headers=headers,
                         verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result15 = 'PASS'
else:
    result15 = 'FAIL'

# GET ALL PERMISSIONS FOR GROUP
print("Get Permissions for Group")
response = requests.get(url + Groups + '/' + groupID1 + permissions, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result16 = 'PASS'
else:
    result16 = 'FAIL'

# INVITE AN USER
print("Invite An User")
parameters = {
    "email": "ruchita.sardesai@mineraltree.com",
    "groupIds": [
        groupID1
    ]
}
response = requests.post(url + Users, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
userID1 = data['result']
print(userID1)
if response.status_code == ExpectedCode200:
    result17 = 'PASS'
else:
    result17 = 'FAIL'



# INVITE ANOTHER USER
print("Invite Another User")
parameters = {
    "email": "ruchita@regal-us.com",
    "groupIds": [
        groupID1
    ]
}
response = requests.post(url + Users, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
userID2 = data['result']
print(userID2)
if response.status_code == ExpectedCode200:
    result18 = 'PASS'
else:
    result18 = 'FAIL'



# ADD USERS TO A GROUP
print("Add Users to Group")
parameters = {
    "userIds": [
        userID1,
        userID2
    ]
}
response = requests.post(url + Groups + '/' + groupID1 + users, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result19 = 'PASS'
else:
    result19 = 'FAIL'


# ADD USERS TO A GROUP
print("Add Users to Group")
parameters = {
 "applicationGroupIds": [
      groupID1,
      groupID2
 ]
}
response = requests.post(url + Users + '/' + userID1 + Groups, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result20 = 'PASS'
else:
    result20 = 'FAIL'



# GET GROUP INFO
print("Get Group Info")
response = requests.get(url + Groups + '/' + groupID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result21 = 'PASS'
else:
    result21 = 'FAIL'


# GET ENTITY INFO
print("Get Entity Info")
response = requests.get(url + Entity + '/' + entityID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result22 = 'PASS'
else:
    result22 = 'FAIL'


# GET ALL USERS OF A GROUP
print("Get All Users Of a Group")
response = requests.get(url + Groups + '/' + groupID1 + users, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result23 = 'PASS'
else:
    result23 = 'FAIL'


# GET ALL GROUPS
print("Get All Groups")
response = requests.get(url + Groups, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result24 = 'PASS'
else:
    result24 = 'FAIL'


# GET ALL USERS OF AN COMPANY-ACCOUNT
print("Get All Users Of Company Account")
response = requests.get(url + Users, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result25 = 'PASS'
else:
    result25 = 'FAIL'


# GET USER DETAILS OF AN COMPANY-ACCOUNT
print("Get User Details Of Company Account")
response = requests.get(url + Users + '/' + userID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result26 = 'PASS'
else:
    result26 = 'FAIL'


# REMOVE APIS
# DELETE APPLICATION FROM ENTITY
print("Delete Application from Entity")
response = requests.delete(url + Entity + '/' + entityID1 + applications + '/' + ApplicationID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result27 = 'PASS'
else:
    result27 = 'FAIL'

# DELETE PERMISSIONS FROM GROUP
print("Delete Permissions from Group")
response = requests.delete(url + Groups + '/' + groupID1 + permissions + '/' + permissionID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result28 = 'PASS'
else:
    result28 = 'FAIL'


# DELETE ADMIN ACCESS
print("Delete Admin Access")
response = requests.delete(url + CompanyAccounts + administrators + '/' + userID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result29 = 'PASS'
else:
    result29 = 'FAIL'


# DELETE USER FROM THE GROUP
print("Delete User from the group")
response = requests.delete(url + Groups + '/' + groupID1 + users + '/' + userID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result30 = 'PASS'
else:
    result30 = 'FAIL'


# DELETE APPLICATION FROM THE GROUP
print("Delete Application from the group")
response = requests.delete(url + Groups + '/' + groupID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result30 = 'PASS'
else:
    result30 = 'FAIL'


# DELETE USER FROM THE COMPANY ACCOUNT
print("Delete User from the Company Account")
response = requests.delete(url + Users + '/' + userID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result31 = 'PASS'
else:
    result31 = 'FAIL'


# DELETE ADMIN USER FROM THE COMPANY ACCOUNT
print("Delete Admin User from the Company Account")
response = requests.delete(url + Users + '/' + userID1, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result32 = 'PASS'
else:
    result32 = 'FAIL'