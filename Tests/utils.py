import os
import filecmp
from fastapi.testclient import TestClient
from httpx import Response
from pathlib import Path
from toolbox.utils.converters import JSON_to_object
from Tests.env import with_env


@with_env
def network_get(client: TestClient, url: str, params: str = '') -> str:
    res: Response = client.get(
        url=f'/{url}{get_obj_from_file(params)}',
        headers={'content-type': 'application/json'},
    )
    return res.text


@with_env
def network_post(client: TestClient, url: str, body) -> str:
    if 'start_date' in url:
        url = url.format(
            start_date=os.environ['start_date'],
            end_date=os.environ['end_date'],
        )
    res: Response = client.post(
        url=url,
        json=get_json_obj_from_file(body),
        headers={'content-type': 'application/json'},
    )
    return res.text


def get_json_obj_from_file(file):
    return JSON_to_object.convert(get_obj_from_file(file))


def get_obj_from_file(file):
    if not file:
        return ''
    file = f'{os.getcwd()}/Tests/params/{file}'
    return Path(file).read_text(encoding='utf-8')


def response_is_valid(file, check_file, response):
    tmp = Path(f'{os.getcwd()}/Tests/{file}')
    tmp.write_text(response)
    target = f'{os.getcwd()}/Tests/responses/{check_file}'
    files_content_is_the_same = filecmp.cmp(str(tmp), target)
    tmp.unlink()
    return files_content_is_the_same
