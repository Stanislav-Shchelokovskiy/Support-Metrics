import time
from dash import (
    Dash,
    dash_table,
    dcc,
    html,
    Input,
    Output,
    State,
    callback_context,
)
from pandas import DataFrame
from dash.exceptions import PreventUpdate
from user_posts_repository import (
    UserPostsRepository, DbFileIsMissingException, UserPoststByTribesMeta
)


app = Dash(
    name=__name__,
    title='User posts by tribes',
)
server = app.server


def get_user_posts_repository() -> UserPostsRepository:
    return UserPostsRepository()


def get_available_tribes() -> list[str]:
    while True:
        try:
            repository = get_user_posts_repository()
            return repository.get_available_tribes()
        except DbFileIsMissingException:
            time.sleep(2)


def create_available_tribes_selector() -> dcc.Checklist:
    available_tribes = get_available_tribes()
    return dcc.Checklist(
        options=available_tribes,
        value=[],
        id='tribe_selector_cl',
        inline=True,
        style={'font-family': 'Segoe UI'},
    )


def get_user_posts_table(tribes: list[str]) -> dash_table:
    user_posts_df = get_user_posts(tribes)
    user_posts_df['id'] = user_posts_df.index.values
    user_posts_df['graph_name'] = (
        user_posts_df[UserPoststByTribesMeta.user_name] + ' ('
        + user_posts_df[UserPoststByTribesMeta.user_id] + ', '
        + user_posts_df[UserPoststByTribesMeta.license_status] + ')'
    )
    user_posts_df['graph_name_common'] = (
        user_posts_df[UserPoststByTribesMeta.user_name] + ' ('
        + user_posts_df[UserPoststByTribesMeta.user_id] + ')'
    )
    return dash_table.DataTable(
        id='user_posts_table',
        data=user_posts_df.to_dict('records'),
        columns=[
            {
                'name': i,
                'id': i
            } for i in user_posts_df.columns if i not in ('id', 'graph_name', 'graph_name_common')
        ],
        filter_action='native',
        sort_action='native',
        sort_mode='multi',
        row_selectable='multi',
        page_size=10,
        style_cell={'font-family': 'Segoe UI'},
    )


def get_user_posts(tribes: list[str]) -> DataFrame:
    while True:
        try:
            repository = get_user_posts_repository()
            user_posts_df = repository.get_user_posts(tribes)
            return user_posts_df
        except DbFileIsMissingException:
            time.sleep(2)


@app.callback(
    Output('download_original_data', 'data'),
    Input('btn_csv', 'n_clicks'),
    State('tribe_selector_cl', 'value'),
    prevent_initial_call=True,
)
def download_original_data(n_clicks, tribes):
    user_posts_df = get_user_posts(tribes)
    return dcc.send_data_frame(user_posts_df.to_csv, 'user_posts.csv')


@app.callback(
    Output('user_posts_table_container', 'children'),
    [Input('tribe_selector_cl', 'value')],
    prevent_initial_call=True,
)
def filter_user_posts_table(tribes):
    if tribes is None:
        raise PreventUpdate

    return get_user_posts_table(tribes)


@app.callback(
    [Output('user_posts_table', 'selected_rows')],
    [
        Input('select_all', 'n_clicks'),
        Input('clear_selection', 'n_clicks'),
    ],
    State('user_posts_table', 'derived_virtual_data'),
    prevent_initial_call=True,
)
def select_all_in_posts_table(select_all, clear_selection, rows):
    ctx = callback_context
    if ctx.triggered:
        trigger = ctx.triggered[0]['prop_id']
        if trigger == 'select_all.n_clicks':
            return [[row['id'] for row in rows]]
    return [[]]


@app.callback(
    Output('graphs_container', 'children'),
    [
        Input('user_posts_table', 'derived_virtual_data'),
        Input('user_posts_table', 'derived_virtual_selected_rows')
    ],
    prevent_initial_call=True,
)
def update_graphs(rows, derived_virtual_selected_rows):
    if not derived_virtual_selected_rows:
        return []

    user_posts_df = DataFrame(rows)
    user_posts_df = user_posts_df.iloc[derived_virtual_selected_rows]

    return create_graphs_div(user_posts_df)


def create_graphs_div(df: DataFrame):
    return html.Div(
        children=create_labeled_tribe_divs(df),
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'flex-start',
            'align-items': 'flex-start',
            'flex-wrap': 'nowrap',
        },
    )


def create_labeled_tribe_divs(df: DataFrame):
    return [
        html.Div(
            children=[
                html.Label(
                    children=get_metric_public_name(metric),
                    style={
                        'font-size': '20px',
                        'font-family': 'Segoe UI'
                    },
                ),
                create_labeled_tribe_div(metric, df)
            ],
            style={
                'margin': '2em',
            }
        ) for metric in [
            UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_their_all_posts_perc,
        ] if metric in df
    ]


def get_metric_public_name(original_metric_name: str) -> str:
    return {
        UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc:
            'What part user posts take from all posts from all users in percent',
        UserPoststByTribesMeta.user_posts_by_tribe_from_posts_from_all_users_perc:
            'What part user posts by tribes take from all posts from all users in percent',
        UserPoststByTribesMeta.user_posts_by_tribe_from_their_all_posts_perc:
            'What part user posts by tribes take from all posts by this user',
    }[original_metric_name]


def create_labeled_tribe_div(metric: str, df: DataFrame):
    return html.Div(
        children=create_graphs(metric, df),
        style={
            'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'flex-start',
            'align-items': 'flex-start',
            'flex-wrap': 'nowrap',
            'margin': '1em',
        },
    )


def create_graphs(metric: str, df: DataFrame) -> list[dcc.Graph]:
    if metric == UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc:
        return greate_graphs_by_users(metric, df)
    return create_graphs_by_tribes(metric, df)


def greate_graphs_by_users(metric: str, df: DataFrame) -> list[dcc.Graph]:
    x_col_name = 'graph_name_common'
    df = get_df_slice(
        [
            x_col_name,
            metric,
        ],
        df,
    )
    return [create_graph(
        x_col_name,
        metric,
        '',
        df,
        df[metric].max(),
    )]


def get_df_slice(cols: list[str], df: DataFrame) -> DataFrame:
    df = df[cols].drop_duplicates()
    return df


def create_graphs_by_tribes(metric: str, df: DataFrame) -> list[dcc.Graph]:
    x_col_name = 'graph_name'
    df = get_df_slice(
        [
            x_col_name,
            metric,
            UserPoststByTribesMeta.tribe_name,
        ],
        df,
    )
    return [
        create_graph(
            x_col_name,
            metric,
            tribe_name,
            df[df[UserPoststByTribesMeta.tribe_name] == tribe_name],
            df[metric].max(),
        ) for tribe_name in df[UserPoststByTribesMeta.tribe_name].unique()
    ]


def create_graph(
    x_col_name: str,
    metric: str,
    tribe_name: str,
    df: DataFrame,
    y_limit: float,
):

    return dcc.Graph(
        id=tribe_name,
        figure={
            'data': [{
                'x': df[x_col_name],
                'y': df[metric],
                'type': 'bar',
            }],
            'layout':
                {
                    'barmode': 'group',
                    'title': {
                        'text': get_title(metric, tribe_name)
                    },
                    'xaxis': {
                        'automargin': True,
                    },
                    'yaxis':
                        {
                            'automargin': True,
                            'range': [0, y_limit * 1.2],
                            'autorange': False,
                        },
                    'height': 500,
                    'margin': {
                        't': 50,
                        'l': 100,
                        'r': 10
                    },
                },
        },
    )


def get_title(metric, tribe_name) -> str:
    return '' if metric == UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc else tribe_name


app.layout = html.Div(
    [
        html.Div(
            id='commands',
            children=[
                create_available_tribes_selector(),
                html.Button(
                    'Select All',
                    id='select_all',
                    style={'font-family': 'Segoe UI'},
                ),
                html.Button(
                    'Clear Selection',
                    id='clear_selection',
                    style={'font-family': 'Segoe UI'},
                ),
                html.Button(
                    'Download original data',
                    id='btn_csv',
                    style={'font-family': 'Segoe UI'},
                ),
                dcc.Download(id='download_original_data'),
            ],
            style={
                'padding': 10,
                'flex': 1
            },
        ),
        html.Div(
            id='user_posts_table_container',
            style={
                'padding': 10,
                'flex': 1,
            },
        ),
        html.Div(
            id='graphs_container',
            style={
                'padding': 10,
                'flex': 1
            },
        )
    ]
)