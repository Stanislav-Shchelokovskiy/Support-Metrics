import pytest
import os
import requests
import filecmp
from pathlib import Path
from toolbox.utils.network import Network
from toolbox.utils.converters import JSON_to_object
from Tests.env import prepare_env


def network_get(url: str) -> str:
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        return Network.get_data(
            end_point=f"http://localhost:{os.environ['SERVER_PORT']}/{url}",
        )


def network_post(url: str, body) -> str:
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_env(monkeypatch)
        if 'start_date' in url:
            url = url.format(
                start_date=os.environ['customers_activity_start_date'],
                end_date=os.environ['customers_activity_end_date'],
            )

        return requests.post(
            url=f"http://localhost:{os.environ['SERVER_PORT']}/{url}",
            json=get_obj_from_file(body),
            headers={
                'content-type': 'application/json'
            },
        ).text


def get_obj_from_file(file):
    return JSON_to_object.convert(
        Path(f'{os.getcwd()}/Tests/params/customers_activity/{file}').read_text(encoding='utf-8')
    )


def response_is_valid(file, check_file, response):
    tmp = Path(f'{os.getcwd()}/Tests/{file}')
    tmp.write_text(response)
    target = f'{os.getcwd()}/Tests/responses/customers_activity/{check_file}'
    files_content_is_the_same = filecmp.cmp(str(tmp), target)
    tmp.unlink()
    return files_content_is_the_same
