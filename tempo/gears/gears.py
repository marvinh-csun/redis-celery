from rgsync import RGWriteBehind, RGWriteThrough
from rgsync.Connectors import MySqlConnector, MySqlConnection

'''
Create MySQL connection object
'''

connection = MySqlConnection('sail', 'password', 'host.docker.internal:13305/laravel')

'''
Create MySQL persons connector
'''
userConnector = MySqlConnector(connection, 'users', 'id')

userMappings = {
	'name':'name',
	'email':'email',
	'password':'password'
}

RGWriteBehind(GB,  keysPrefix='user', mappings=userMappings, connector=userConnector, name='UsersWriteBehind',  version='99.99.99')