import logging
import time
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
from user_posts_repository import (
    UserPostsRepository, DbFileIsMissingException, UserPoststByTribesMeta
)


logging.getLogger('werkzeug').setLevel(logging.INFO)

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


# def create_available_tribes_selector() -> dcc.Dropdown:
#     available_tribes = get_available_tribes()
#     available_options = ['All']
#     available_options.extend(available_tribes)
#     return dcc.Dropdown(
#         options=available_options,
#         value='All',
#         id='tribe_selector_dd',
#         style={'width': '80%'}
#     )


def get_user_posts_table() -> dash_table:
    user_posts_df = get_user_posts()
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


def get_user_posts() -> DataFrame:
    while True:
        try:
            repository = get_user_posts_repository()
            user_posts_df = repository.get_user_posts()
            return user_posts_df
        except DbFileIsMissingException:
            time.sleep(2)


app.layout = html.Div(
    [
        html.Div(
            id='user_posts_table_container',
            children=get_user_posts_table(),
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


@app.callback(
    Output('graphs_container', 'children'),
    Input('user_posts_table', 'derived_virtual_data'),
    Input('user_posts_table', 'derived_virtual_selected_rows')
)
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        raise PreventUpdate

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
        create_labeled_tribe_div(metric, df) for metric in [
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_their_all_posts_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc,
        ] if metric in df
    ]


def create_labeled_tribe_div(metric: str, df: DataFrame):
    elements = [html.Label(children=metric)]
    elements.extend(create_graphs(metric, df))
    return html.Div(
        children=elements,
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
        ) for tribe_name in df[UserPoststByTribesMeta.tribe_name].unique()
    ]


def create_graph(metric: str, tribe_name: str, df: DataFrame):
    return dcc.Graph(
        id=tribe_name,
        figure={
            'data':
                [
                    {
                        'x': df[UserPoststByTribesMeta.user_id],
                        'y': df[metric],
                        'type': 'bar',
                        # 'marker': {
                        #     'color': ['#0074D9']
                        # },
                    }
                ],
            'layout':
                {
                    'xaxis': {
                        'automargin': True
                    },
                    'yaxis':
                        {
                            'automargin': True,
                            'title': {
                                'text': tribe_name
                            }
                        },
                    'height': 250,
                    'margin': {
                        't': 10,
                        'l': 10,
                        'r': 10
                    },
                },
        },
    )
