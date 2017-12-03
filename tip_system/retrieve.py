import urllib3, requests, json

def get_tip(pcts):
    #
    wml_service_credentials_url, wml_service_credentials_username, wml_service_credentials_password = [line.rstrip('\n') for line in open('credentials.txt')]

    # retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
    # Service credentials associated with your IBM Cloud Watson Machine Learning Service instanceIBM Cloud Watson Machine Learning Service instance 
    wml_credentials={
            "url": wml_service_credentials_url,
            "username": wml_service_credentials_username,
            "password": wml_service_credentials_password
            }

    headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
    url = '{}/v3/identity/token'.format(wml_credentials['url'])
    response = requests.get(url, headers=headers)
    mltoken = json.loads(response.text).get('token')

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"fields": ["COLUMN1", "COLUMN2", "COLUMN3", "COLUMN4"], "values": [pcts]}

    response_scoring = requests.post('https://ibm-watson-ml.mybluemix.net/v3/wml_instances/1ed4b0ab-6734-4240-9d03-88d635793d5d/published_models/34f4e1d2-f2f5-4dd7-9801-59cf65d3676b/deployments/c7e8e90c-05f4-4a95-9205-04ba4fe29e39/online', json=payload_scoring, headers=header)
    dic = response_scoring.json()
    values = dic['values']
    return int(values[-1][-3])
