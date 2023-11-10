from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData, KnotMeta
from toolbox.sql.field import Field, TEXT
import toolbox.sql.generators.sqlite.statements as sqlite_index


class CatRepliesTypes(KnotMeta):
    pass


class Components(MetaData):
    component_id = Field(TEXT)
    component_name = Field(TEXT)

    @classmethod
    def get_name(cls) -> str:
        return CatComponentsFeatures.get_name()


class Features(MetaData):
    feature_id = Field(TEXT)
    feature_name = Field(TEXT)

    @classmethod
    def get_name(cls) -> str:
        return CatComponentsFeatures.get_name()


class CatComponentsFeatures(MetaData):
    tent_id = Field(TEXT)
    component_id = Components.component_id
    feature_id = Features.feature_id
    component_name = Components.component_name
    feature_name = Features.feature_name

    @classmethod
    def get_key_fields(
        cls,
        projector: Callable[[Field], Any] = str,
        *exfields: Field,
    ) -> Sequence[Field | str | Any]:
        return tuple()

    @classmethod
    def get_indices(cls) -> Sequence[str]:
        tbl = cls.get_name()
        return (
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.tent_id,
                    cls.component_id,
                    cls.component_name,
                )
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.tent_id,
                    cls.component_id,
                    cls.feature_id,
                    cls.feature_name,
                )
            ),
            sqlite_index.create_index(
                tbl=tbl, cols=(
                    cls.component_id,
                    cls.component_name,
                )
            ),
            sqlite_index.create_index(
                tbl=tbl, cols=(
                    cls.feature_id,
                    cls.feature_name,
                )
            ),
        )
