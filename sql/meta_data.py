from typing import Dict, List


class MetaData:

    @classmethod
    def _get_dict(cls) -> Dict[str, str]:
        res = {}
        while cls != None:
            res.update(
                {
                    k: v
                    for k, v in cls.__dict__.items()
                    if not k.startswith('_') and not k.startswith('get_')
                }
            )
            cls = cls.__base__
        return res

    @classmethod
    def get_attrs(cls) -> Dict[str, str]:
        return cls._get_dict()

    @classmethod
    def get_values(cls) -> List[str]:
        return list(cls._get_dict().values())
