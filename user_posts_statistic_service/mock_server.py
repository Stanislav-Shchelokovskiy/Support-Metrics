from fastapi import FastAPI
from fastapi.responses import Response
from sql.base_repository import BaseRepository
from sql.sql_query import SqlQuery
from sql.query_executors import SQLiteQueryExecutor
from utils.df_json_converter import DF_to_JSON


app = FastAPI()


@app.get("/user_posts")
def user_posts():
    repository = BaseRepository(
        sql_query_type=SqlQuery,
        query_executor=SQLiteQueryExecutor(),
    )
    df = repository.get_data(
        query_file_path='sql_queries/cached_posts_by_tribes.sql',
        query_format_params={},
        must_have_columns=[]
    )
    return Response(
        content=DF_to_JSON.convert(df=df),
        media_type='application/json',
    )

    # ../.venv/bin/uvicorn mock_server:app --host 0.0.0.0 --port 12000 --reload
