from collections.abc import Sequence, Callable
from typing import Any
from toolbox.sql.meta_data import MetaData
from toolbox.sql.field import Field, TEXT
import toolbox.sql.generators.sqlite.statements as sqlite_index


class Platforms(MetaData):
    platform_id = Field(TEXT)
    platform_name = Field(TEXT)

    @classmethod
    def get_name(cls) -> str:
        return PlatformsProducts.get_name()


class Products(MetaData):
    product_id = Field(TEXT)
    product_name = Field(TEXT)

    @classmethod
    def get_name(cls) -> str:
        return PlatformsProducts.get_name()


class PlatformsProducts(MetaData):
    platform_tent_id = Field(TEXT)
    platform_id = Platforms.platform_id
    product_tent_id = Field(TEXT)
    product_id = Products.product_id
    platform_tent_name = Field(TEXT)
    platform_name = Platforms.platform_name
    product_tent_name = Field(TEXT)
    product_name = Products.product_name

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
                    cls.product_tent_id,
                    cls.product_id,
                    cls.product_name,
                ),
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.platform_tent_id,
                    cls.platform_id,
                    cls.platform_name,
                ),
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.platform_id,
                    cls.platform_name,
                ),
            ),
            sqlite_index.create_index(
                tbl=tbl,
                cols=(
                    cls.product_id,
                    cls.product_name,
                ),
            ),
        )
