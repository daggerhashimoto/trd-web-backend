from fastapi import FastAPI
from duneanalytics import DuneAnalytics
import json, os
from dotenv import load_dotenv

load_dotenv()
DUNE_USER = os.getenv('DUNE_USER')
DUNE_PASS = os.getenv('DUNE_PASS')

def dune():
    # initialize client
    dune = DuneAnalytics(DUNE_USER, DUNE_PASS)

    # try to login
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # fetch query result id using query id
    # query id for any query can be found from the url of the query:
    # for example: 

    # Total USD amount: https://dune.com/queries/1975748/3265623
    # Unique addresses: https://dune.com/queries/1975748/3266155
    # Contributions: https://dune.com/queries/1975748/3266160

    # Contributor list: https://dune.com/queries/1976770/3266196
    # Donations over time chart: https://dune.com/queries/1979561/3271445

    result_id = dune.query_result_id_v3(query_id=1975748)

    # fetch execution result
    data = dune.get_execution_result(result_id)
    json_object = json.dumps(data)

    return json_object

app = FastAPI()

@app.get("/")
async def root():
    return {"result": dune()}

