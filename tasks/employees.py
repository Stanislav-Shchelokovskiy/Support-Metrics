import os
import toolbox.utils.network as network
from toolbox.utils.selectors import employees


def get_employees(start_date: str) -> str:
    emps_json = network.get_data(
        end_point=os.environ['EMPS_ENDPOINT'],
        headers={
            'X-ApplicationId': os.environ['EMPS_APPID'],
            'X-UserId': os.environ['EMPS_USERID'],
            'User-Agent': 'SupportMetrics',
        },
    )
    return employees.select(emps_json=emps_json, start=start_date)
