import asyncio
from pathlib import Path
from collections.abc import Callable
from toolbox.sql.aggs.metrics import Metric
from toolbox.utils.converters import Object_to_JSON, file_to_dict
from repository.local.aggs import get_metric


async def get_descriptions() -> str:
    return await __run_in_executor(__get_descriptions_json)


async def get_description(metric: str) -> str:
    metric = get_metric(metric=metric)
    return await __run_in_executor(__get_description_json, metric)


async def __run_in_executor(fn: Callable[..., str], *args):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, fn, *args)


def __get_description_json(metric: Metric):

    def normalize(name: str):
        return name.replace(' / ', '_')

    def converter(title):
        return metric.display_name or title

    path = Path(f'help/metrics_descriptions/{normalize(metric.name)}.MD')
    desc = file_to_dict(path, converter)
    return Object_to_JSON.convert(desc)


def __get_descriptions_json():
    path = Path('help/customers_activity')
    return Object_to_JSON.convert(__get_files_in_folder(path))


def __get_files_in_folder(folder: Path) -> list[dict[str, str]]:
    res = []

    def title_converter(title: str) -> str:
        return title[title.find('$') + 1:]

    for obj in sorted(folder.iterdir()):
        if (obj.is_file()):
            desc = file_to_dict(obj, title_converter)
            res.append(desc)
    return res
