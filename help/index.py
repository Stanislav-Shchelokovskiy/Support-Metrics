from pathlib import Path


class Index:

    @staticmethod
    def get_cwd() -> str:
        return 'help'

    @staticmethod
    def get_customers_activity() -> str:
        return Index.get_cwd() + '/customers_activity'

    @staticmethod
    def get_customers_activity_descriptions() -> list[dict[str, str]]:
        customers_activity_path = Path(Index.get_customers_activity())
        return Index.get_files_in_folder(customers_activity_path)

    @staticmethod
    def get_files_in_folder(folder: Path) -> list[dict[str, str]]:
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
