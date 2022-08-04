from dash import (
    Dash,
    dash_table,
    dcc,
    html,
    Input,
    Output,
)
from pandas import DataFrame
from dash.exceptions import PreventUpdate
from application_service.user_posts_repository import (
    UserPostsRepository,
    DbFileIsMissingException,
)


app = Dash(
    name=__name__,
    title='User posts by tribes',
)
server = app.server


def get_user_posts_repository() -> UserPostsRepository:
    return UserPostsRepository()


def get_available_tribes() -> list[str]:
    try:
        repository = get_user_posts_repository()
        return repository.get_available_tribes()
    except DbFileIsMissingException:
        return []


def create_available_tribes_selector() -> dcc.Dropdown:
    available_tribes = get_available_tribes()
    return dcc.Dropdown(
        options=available_tribes,
        value=available_tribes[0] if available_tribes else None,
        id='groupby_dd',
        style={'width': '80%'}
    )


def get_user_posts_table(selected_tribe: str) -> dash_table:
    user_posts_df = get_user_posts(selected_tribe)
    return dash_table.DataTable(
        data=user_posts_df.to_dict('records'),
        columns=[{
            'name': i,
            'id': i
        } for i in user_posts_df.columns]
    )


def get_user_posts(selected_tribe) -> DataFrame:
    try:
        repository = get_user_posts_repository()
        user_posts_df = repository.get_user_posts(
            tribe_name=selected_tribe
        )
        return user_posts_df
    except DbFileIsMissingException:
        return DataFrame()


app.layout = html.Div(
    [
        html.Div(
            id='tribe_selector',
            children=[
                html.Label(
                    children='Tribe:',
                    style={
                        'padding': '10px',
                        'width': '40%'
                    },
                ),
                create_available_tribes_selector(),
            ],
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'flex-start',
                'align-items': 'center',
                'flex-wrap': 'nowrap',
                'width': '50%'
            },
        ),
        html.Div(
            id='user_posts_table',
            style={
                'padding': 10,
                'flex': 1
            },
        ),
    ]
)


@app.callback(
    Output(component_id='user_posts_table', component_property='children'),
    [
        Input(component_id='tribe_selector', component_property='value'),
    ],
    # prevent_initial_call=True,
)
def update_output(tribe):
    if not tribe:
        raise PreventUpdate
    return get_user_posts_table(selected_tribe=tribe)
