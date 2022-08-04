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


def create_available_tribes_selector() -> dcc.Dropdown:
    available_tribes = get_available_tribes()
    available_options = ['All']
    available_options.extend(available_tribes)
    return dcc.Dropdown(
        options=available_options,
        value='All',
        id='tribe_selector_dd',
        style={'width': '80%'}
    )


def get_user_posts_table(selected_tribe: str) -> dash_table:
    print('get_user_posts_table')
    user_posts_df = get_user_posts(selected_tribe)
    return dash_table.DataTable(
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


def get_user_posts(selected_tribe) -> DataFrame:
    while True:
        try:
            repository = get_user_posts_repository()
            user_posts_df = repository.get_user_posts(
                tribe_name=selected_tribe
            )
            return user_posts_df
        except DbFileIsMissingException:
            time.sleep(2)


app.layout = html.Div(
    [
        # html.Div(
        #     id='tribe_selector',
        #     children=[
        #         html.Label(
        #             children='Tribe:',
        #             style={
        #                 'padding': '10px',
        #                 'width': '40%'
        #             },
        #         ),
        #         create_available_tribes_selector(),
        #     ],
        #     style={
        #         'display': 'flex',
        #         'flex-direction': 'row',
        #         'justify-content': 'flex-start',
        #         'align-items': 'center',
        #         'flex-wrap': 'nowrap',
        #         'width': '50%'
        #     },
        # ),
        html.Div(
            id='user_posts_table',
            children=get_user_posts_table(selected_tribe='All'),
            style={
                'padding': 10,
                'flex': 1
            },
        ),
        html.Div(id='graphs-container')
    ]
)


@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows")
)
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = get_user_posts_table(selected_tribe='All'
                               ) if rows is None else DataFrame(rows)

    colors = [
        '#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
        for i in range(len(dff))
    ]

    return [
        dcc.Graph(
            id=column,
            figure={
                "data":
                    [
                        {
                            "x": dff[UserPoststByTribesMeta.user_id],
                            "y": dff[column],
                            "type": "bar",
                            "marker": {
                                "color": colors
                            },
                        }
                    ],
                "layout":
                    {
                        "xaxis": {
                            "automargin": True
                        },
                        "yaxis":
                            {
                                "automargin": True,
                                "title": {
                                    "text": column
                                }
                            },
                        "height": 250,
                        "margin": {
                            "t": 10,
                            "l": 10,
                            "r": 10
                        },
                    },
            },
        )

        # yapf: disable
        for column in [
            UserPoststByTribesMeta.user_posts_by_tribe_from_their_all_posts_perc,
            UserPoststByTribesMeta.
            user_posts_by_tribe_from_posts_from_all_users_perc,
            UserPoststByTribesMeta.user_posts_from_posts_from_all_users_perc,
        ] if column in dff
        # yapf: enable
    ]


# @app.callback(
#     Output(component_id='user_posts_table', component_property='children'),
#     [
#         Input(component_id='tribe_selector_dd', component_property='value'),
#     ],
#     # prevent_initial_call=True,
# )
# def update_output(tribe):
#     if not tribe:
#         raise PreventUpdate
#     return get_user_posts_table(selected_tribe=tribe)
