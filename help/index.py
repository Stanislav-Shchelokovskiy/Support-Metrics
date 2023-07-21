import asyncio
from pathlib import Path
from toolbox.utils.converters import Object_to_JSON, file_to_dict


async def get_descriptions() -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, __get_descriptions_json)


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
