import pytest
from user_posts_statistic_service.sql.sqlite_data_base import SQLiteDataBase


def test_connections():
    with pytest.MonkeyPatch.context() as monkeypatch:
        prepare_environment(monkeypatch)
        db = SQLiteDataBase(db_file_name='test')
        db._connect_or_reuse_connection()
        db._connect_or_reuse_connection()
        assert db._db_connections_count == 2
        db._try_disconnect()
        assert db._db_connections_count == 1
        db._try_disconnect()
        assert db._db_connections_count == 0
        db._try_disconnect()
        assert db._db_connections_count == 0


def prepare_environment(monkeypatch: pytest.MonkeyPatch):

    def mock_connect(self):
        pass

    def mock_disconnect(self):
        pass

    monkeypatch.setattr(
        SQLiteDataBase,
        '_connect',
        mock_connect,
    )

    monkeypatch.setattr(
        SQLiteDataBase,
        '_disconnect',
        mock_disconnect,
    )