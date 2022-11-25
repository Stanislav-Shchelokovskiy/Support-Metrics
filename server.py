import os
import urllib3
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from toolbox.utils.converters import JSON_to_object
import repository.server_repository as server_repository

from typing import Dict

from repository.factory import RepositoryFactory


urllib3.disable_warnings()


def query_query_service(
    method: str,
    params: Dict[str, str],
) -> str:
    headers = {}
    return requests.get(
        url=os.environ['QUERY_SERVICE_NAME'] + method,
        headers=headers,
        params=params,
        verify=False,
    ).text


app = FastAPI()

origins = JSON_to_object.convert(os.environ['CORS_ORIGINS'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_response(json_data: str) -> Response:
    return Response(
        content=json_data,
        media_type='application/json',
    )


@app.get('/get_tickets_with_iterations_period')
def customers_activity_get_tickets_with_iterations_period():
    # yapf: disable
    df_json = server_repository.customers_activity_get_tickets_with_iterations_period()
    # yapf: enable
    return get_response(json_data=df_json)


@app.get('/get_available_tribes')
def get_available_tribes():
    return query_query_service(method='/get_available_tribes')


@app.get('/get_customers_groups')
def customers_activity_get_customers_groups():
    df_json = server_repository.customers_activity_get_customers_groups()
    return get_response(json_data=df_json)
