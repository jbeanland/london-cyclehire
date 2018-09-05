import pandas as pd
import requests
from datetime import datetime

secrets = dict()
with open('secrets', 'r') as f:
    for line in f:
        l = line.strip('\n').split('=')
        secrets[l[0]] = l[1]
secrets.keys()

base_url = 'https://oslobysykkel.no/api/v1'
auth_header = {'Client-Identifier': secrets['OSLO_BYSYKKEL_API_KEY']}
file_path = '/home/jack/projects/cyclehire/oslo/oslo_sykkel_records.csv'
log_path = '/home/jack/projects/cyclehire/oslo/oslo_sykkel_log.txt'

r = requests.get(f'{base_url}/stations/availability', headers=auth_header)

res = r.json()

if r.status_code == 200:
    updated = res['updated_at']
    stations = res['stations']

    records = []
    for x in stations:
        d = x['availability']
        d['id'] = x['id']
        records.append(d)
    records = pd.DataFrame(records)
    records['date'] = updated

    try:
        all_records = pd.read_csv(file_path, index_col=0)
        all_records = pd.concat([all_records, records]).reset_index(drop=True)
    except FileNotFoundError:
            all_records = records

    all_records.to_csv(file_path)
    log = f"got records successfully at {datetime.now().strftime('%H:%M - %d/%m/%Y')}\n"
else:
    log = f"failed with status {r.status_code} at time {datetime.now().strftime('%H:%M - %d/%m/%Y')}\n"

with open(log_path, "a") as f:
    f.write(f'{log}\n')
