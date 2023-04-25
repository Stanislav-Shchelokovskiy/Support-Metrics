import asyncio
from pathlib import Path
from toolbox.utils.converters import Object_to_JSON


async def get_customers_activity_descriptions() -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, __get_customers_activity_descriptions_json)


def __get_customers_activity_descriptions_json():
    path = Path('help/customers_activity')
    return Object_to_JSON.convert(__get_files_in_folder(path))


def __get_files_in_folder(folder: Path) -> list[dict[str, str]]:
    res = []
    for obj in sorted(folder.iterdir()):
        if (obj.is_file()):
            title = obj.stem
            title = title[title.find('$') + 1:]
            file = {}
            file['title'] = title
            file['content'] = obj.read_text()
            res.append(file)
    return res
