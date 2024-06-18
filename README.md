This is intended to help Ellucian Banner Schools with their implementation of ARMS Parking API

This projects requires a .env file be placed in the root directory with the following format:

# API VARIABLES
BASE_URI = 'https://parkingtest.arms.app/'
AGENCY_KEY = <INSERT_YOUR_KEY_HERE>
ENCUMBRANCE_API_KEY = <INSERT_YOUR_KEY_HERE>

#SCRIPT VARIABLES
USERTYPECODES = <insert user type codes here seperated by a comma ex. RSTU,FAC,STAFF>
ENCUMBRANCETYPE = Citation,Credit,Permit
PERMITTYPE = GetPermitSalesDetailReport,GetAllActivePermit

# Banner DB configs
BAN_DB_URL=<INSERT BANNER URL HERE>
BAN_DB_USER=< INSERT USER HERE>
BAN_DB_PASSWORD=<ENCODED PASSWORD STRING HERE>
BAN_DB_REFKEY=<ENCODED REFKEY HERE>
BAN_DB_PORT=<DB PORT>
BAN_DB_SERVICE_NAME=<SERVICE NAME>
BAN_DIALECT=<DIALECT>

To populate the encoded password and refkey, run ./methods/password_encryptor.py and update line 5 with your password as a string ex. PASSWORD='mypassword123'
Once it is run, it will output an encrypted password and encrypted reference key to be used as a .env variable.