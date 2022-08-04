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
    )


def get_user_posts_table(tribes: list[str]) -> dash_table:
    user_posts_df = get_user_posts(tribes)
    return dash_table.DataTable(
        id='user_posts_table',
        data=user_posts_df.to_dict('records'),
        columns=[{
            'name': i,
            'id': i
        } for i in user_posts_df.columns],
        filter_action='native',
        sort_action='native',
        sort_mode='multi',
        row_selectable='multi',
        page_size=10,
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
    Output('user_posts_table_container', 'children'),
    [Input('tribe_selector_cl', 'value')],
)
def filter_user_posts_table(tribes):
    if tribes is None:
        raise PreventUpdate

    return get_user_posts_table(tribes)


@app.callback(
    Output('user_posts_table', 'selected_rows'),
    [Input('select_all', 'n_clicks'),
     Input('clear_selection', 'n_clicks')],
    State('user_posts_table', 'derived_virtual_data'),
    prevent_initial_call=True,
)
def select_all_in_posts_table(select_all, clear_selection, rows):
    ctx = callback_context
    if ctx.triggered:
        trigger = (ctx.triggered[0]['prop_id'].split('.')[0])
        if trigger == 'select_all':
            return [i for i in range(len(rows))]
    return []


@app.callback(
    Output('graphs_container', 'children'),
    [
        Input('user_posts_table', 'derived_virtual_data'),
        Input('user_posts_table', 'derived_virtual_selected_rows')
    ],
    prevent_initial_call=True,
)
def update_graphs(rows, derived_virtual_selected_rows):
    # if derived_virtual_selected_rows is None:
    #     raise PreventUpdate

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
                html.Label(children=metric),
                create_labeled_tribe_div(metric, df)
            ]
        ) for metric in [
            UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_their_all_posts_perc,
        ] if metric in df
    ]


def create_labeled_tribe_div(metric: str, df: DataFrame):
    return html.Div(
        children=create_graphs(metric, df),
        style={
            'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'flex-start',
            'align-items': 'flex-start',
            'flex-wrap': 'nowrap',
        },
    )


def create_graphs(metric: str, df: DataFrame) -> list[dcc.Graph]:
    return [
        create_graph(
            metric,
            tribe_name,
            df[df[UserPoststByTribesMeta.tribe_name] == tribe_name],
            df[metric].max(),
        ) for tribe_name in df[UserPoststByTribesMeta.tribe_name].unique()
    ]


def create_graph(metric: str, tribe_name: str, df: DataFrame, y_limit: float):
    return dcc.Graph(
        id=tribe_name,
        figure={
            'data':
                [
                    {
                        'x': df[UserPoststByTribesMeta.user_name],
                        'y': df[metric],
                        'type': 'bar',
                        # 'marker': {
                        #     'color': ['#0074D9']
                        # },
                    }
                ],
            'layout':
                {
                    'title': {
                        'text': get_title(metric, tribe_name)
                    },
                    'xaxis': {
                        'automargin': True,
                    },
                    'yaxis': {
                        'automargin': False,
                        'range': [0, y_limit]
                    },
                    'height': 250,
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
                html.Button('Select All', id='select_all', n_clicks=0),
                html.Button(
                    'Clear Selection',
                    id='clear_selection',
                    n_clicks=0,
                ),
            ],
            style={
                'padding': 10,
                'flex': 1
            },
        ),
        html.Div(
            id='user_posts_table_container',
            #children=get_user_posts_table([]),
            style={
                'padding': 10,
                'flex': 1
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