import requests

data = {
    "ID": 1,
    "LicAge": 121,
    "RecordBeg": "2008-01-01",
    "RecordEnd": "",
    "VehAge": 40,
    "Gender": "Male",
    "MariStat": "Other",
    "SocioCateg": "CSP50",
    "VehUsage": "Private+trip to office",
    "DrivAge": 63,
    "HasKmLimit": 0,
    "BonusMalus": 0,
    "OutUseNb": 0,
    "RiskArea": 10
}


def send_json(data):
    url = 'http://127.0.0.10:5000/predict'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response


if __name__ == '__main__':
    response = send_json(data)
    print(response.json())