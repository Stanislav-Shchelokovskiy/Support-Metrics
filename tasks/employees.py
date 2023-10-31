import os
import toolbox.utils.network as network


def get_employees() -> str:
    return network.get_data(
        end_point=os.environ['EMPS_ENDPOINT'],
        headers={
            'X-ApplicationId': os.environ['EMPS_APPID'],
            'X-UserId': os.environ['EMPS_USERID'],
            'User-Agent': 'SupportMetrics',
        },
        params={
            'expandDetails': True,
            'expandDataForAnalytics': True,
        },
    ).replace('":', '": ')
