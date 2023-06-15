import repository.local.tables_builder as TablesBuilder
from repository.local.db_statements.indexes import get_create_index_statements
from repository.local.db_statements.table_defs import get_create_table_statements
import repository.local.repository as LocalRepository


class RepositoryFactory:
    import repository.remote.factory as factory
    remote = factory
