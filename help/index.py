from pathlib import Path
from toolbox.utils.converters import Object_to_JSON


def get_customers_activity_descriptions() -> str:
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
