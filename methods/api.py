import requests, requests.auth, os, datetime, json
from dotenv import load_dotenv

load_dotenv()
BASE_URI = os.getenv("BASE_URI")
AGENCY_KEY = str(os.getenv("AGENCY_KEY"))
ENCUMBRANCE_API_KEY = str(os.getenv("ENCUMBRANCE_API_KEY"))
USERTYPECODES = list(str(os.getenv("USERTYPECODES")).split(','))
ENCUMBRANCETYPE = list(str(os.getenv("ENCUMBRANCETYPE")).split(','))
PERMITTYPE = list(str(os.getenv("PERMITTYPE")).split(','))

class CreateToken():
    def __new__(cls):
        if not hasattr(cls, 'instance') or cls.time < datetime.datetime.now():
            cls.instance = super(CreateToken, cls).__new__(cls)
            url = f"{BASE_URI}api/v1/External/Authorize/CreateToken"
            response = requests.get(url, auth= requests.auth.HTTPBasicAuth(f"{AGENCY_KEY}", f"{ENCUMBRANCE_API_KEY}"))
            cls.token = response.json()["data"]["token"]
            cls.time = datetime.datetime.now() + datetime.timedelta(minutes=20)
        return cls.instance

def Encumbrances(mode: list = USERTYPECODES, date: str = datetime.datetime.now().strftime('%Y-%m-%d')) -> dict:
    data = {}
    headers = {
                'Authorization': f'{CreateToken().token}',
                'Content-Type': 'application/json'
                }
    
    for type in ENCUMBRANCETYPE:
        url = f"{BASE_URI}api/v1/Accounting/Encumbrance/{type}"
        for i in mode:
            payload = json.dumps({
                "encumbranceDate": date,
                "userTypeCode": i
                })
            response = requests.post(url, headers=headers, data=payload)
            data[f'{i}_Encumbrance_{type}_response'] = response.json()

    return data

def Permits():
    data = {}
    headers = {
            'Authorization': f'{CreateToken().token}',
            'Content-Type': 'application/json'
            }
    for type in PERMITTYPE:
        url = f"{BASE_URI}api/v1/External/Permit/{type}"
        match type:
            case 'GetPermitSalesDetailReport':
                payload = json.dumps({
                    "purchaseDate": "2024-06-03"
                    })
            case 'GetAllActivePermit':
                payload = json.dumps({
                    "pageSize": "0"
                    })
        response = requests.post(url, headers=headers, data=payload)
        data[f'{type}_Permit_response'] = response.json()
        
    return data