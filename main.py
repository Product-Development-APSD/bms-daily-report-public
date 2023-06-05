# Daily Report Potensi Kepadatan BMS

# import package
from dash import Dash, dcc, html
from dash import dash_table

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

import io
import base64
import datetime
import locale

import functions


# = start code = #

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Daily Report BMS"


## Get today's date
today = datetime.datetime.today().strftime('%Y-%m-%d')

# Set the locale to Indonesian
locale.setlocale(locale.LC_ALL, 'id_ID.utf8')
# Format the date as per Indonesian locale
hari_ini = datetime.date.today().strftime("%A, %d %B %Y")

# Collecting data
data_t1, df_t1, time_t1, list_ovtime_t1, meanT1, mean_plusT1, mean_minT1 = functions.collect_data(today, 1)
data_t2, df_t2, time_t2, list_ovtime_t2, meanT2, mean_plusT2, mean_minT2 = functions.collect_data(today, 2)
data_t3, df_t3, time_t3, list_ovtime_t3, meanT3, mean_plusT3, mean_minT3 = functions.collect_data(today, 3)

## Generating graph
image_t1 = functions.generate_graph(df_t1, 1, today, hari_ini)
image_t2 = functions.generate_graph(df_t2, 2, today, hari_ini)
image_t3 = functions.generate_graph(df_t3, 3, today, hari_ini)

## generating text
text_t1 = functions.generate_text(list_ovtime_t1)
text_t2 = functions.generate_text(list_ovtime_t2)
text_t3 = functions.generate_text(list_ovtime_t3)


# Main APP
app.layout = html.Div(
    style={
        "background-image": "url('assets/Bg.png')",
        "background-repeat": "no-repeat",
        # "background-position": "center center",
        "background-size": "cover",
        "height": "3000px",
        "width": "100%"
    },
    children=[
        html.Div(
            style={
                   "position": "absolute", 
                   "top": "100px",
                    "right": "230px",
                    'fontSize': '30px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold',
                    'color' : 'white',
                    },
            children=[
                html.H1(
                    children="Report Analisis Potensi Kepadatan Penumpang", className="header-title", 
                    style={"text-align": "center"},
                ),
            ],
            className="header",
        ),
        html.Div(
            style={
                   "position": "absolute", 
                   "top": "95px",
                    "right": "225px",
                    'fontSize': '30px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold',
                    'color' : 'black',
                    },
            children=[
                html.H1(
                    children="Report Analisis Potensi Kepadatan Penumpang", className="header-title", 
                    style={"text-align": "center"},
                ),
            ],
            className="header",
        ),
        html.Div(
            style={
                   "position": "absolute", 
                   "top": "200px",
                    "right": "210px",
                    'fontSize': '26px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold',
                    'color' : 'black',
                    },
            children=[
                html.H1(
                    children="Berdasarkan Scheduled Arrival Flight di Setiap Terminal", className="header-title", 
                    style={"text-align": "center"},
                ),
            ],
            className="header",
        ),
        html.Div(
            style={
                   "position": "absolute", 
                   "top": "300px",
                    "right": "550px",
                    'fontSize': '24px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold',
                    'color' : 'black',
                    },
            children=[
                html.H1(
                    children="Pada Hari "+hari_ini, className="header-title", 
                    style={"text-align": "center"},
                ),
            ],
            className="header",
        ),
        ### TEXT TERMINAL 1 - START
       html.P(
           style={"position": "absolute", 
                    "top": "1100px", 
                    "left": "210px",
                    'fontSize': '25px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold'
                            },
            children=[
                'Pada pukul ',
                html.Span(time_t1[0]+' – '+time_t1[-1], style={'color': 'red'}),
                ' memiliki jumlah jumlah scheduled arrival flight',
                html.Br(),
                ' yang lebih dari rata-rata, ',
                html.Span('sehingga perlu disiapkan antisipasi', style={'color': 'red'}),
                html.Br(),
                ' pada rentang waktu tersebut.'
            ]
        ),

        html.Div(
            style={"position": "absolute", 
                    "top": "800px", 
                    "right": "90px",},
            children=[                
                html.P(
                    style={
                        'fontSize': '25px',
                        'font-family': 'Roboto',
                        'fontWeight': 'bold'
                                },
                    children=[
                        'Estimasi lonjakan penumpang ',
                    html.Br(),
                        'terjadi pada pukul: ',
                    dcc.Markdown(children=text_t1,
                                style={
                                    'fontSize': '25px',
                                    'font-family': 'Roboto',
                                    'fontWeight': 'bold',
                                    'color': 'red',
                                    }),      
                    'Di Terminal 1 pada rentang waktu tersebut',
                    html.Br(),
                    'memerlukan perhatian khusus oleh ',
                    html.Br(),
                    'tim yang bertugas.']),
                ]
        ),### TEXT TERMINAL 1 - END

       ### TEXT TERMINAL 2 - START
       html.P(
           style={"position": "absolute", 
                    "top": "1900px", 
                    "left": "210px",
                    'fontSize': '25px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold'
                            },
            children=[
                'Pada pukul ',
                html.Span(time_t2[0]+' – '+time_t2[-1], style={'color': 'red'}),
                ' memiliki jumlah jumlah scheduled arrival flight',
                html.Br(),
                ' yang lebih dari rata-rata, ',
                html.Span('sehingga perlu disiapkan antisipasi', style={'color': 'red'}),
                html.Br(),
                ' pada rentang waktu tersebut.'
            ]
        ),

        html.Div(
            style={"position": "absolute", 
                    "top": "1600px", 
                    "right": "90px",},
            children=[                
                html.P(
                    style={
                        'fontSize': '25px',
                        'font-family': 'Roboto',
                        'fontWeight': 'bold'
                                },
                    children=[
                        'Estimasi lonjakan penumpang ',
                    html.Br(),
                        'terjadi pada pukul: ',
                    dcc.Markdown(children=text_t2,
                                style={
                                    'fontSize': '25px',
                                    'font-family': 'Roboto',
                                    'fontWeight': 'bold',
                                    'color': 'red',
                                    }),      
                    'Di Terminal 2 pada rentang waktu tersebut',
                    html.Br(),
                    'memerlukan perhatian khusus oleh ',
                    html.Br(),
                    'tim yang bertugas.']),
                ]
        ), ### TEXT TERMINAL 2 - END

        ### TEXT TERMINAL 3 - START
       html.P(
           style={"position": "absolute", 
                    "top": "2700px", 
                    "left": "210px",
                    'fontSize': '25px',
                    'font-family': 'Roboto',
                    'fontWeight': 'bold'
                            },
            children=[
                'Pada pukul ',
                html.Span(time_t3[0]+' – '+time_t3[-1], style={'color': 'red'}),
                ' memiliki jumlah jumlah scheduled arrival flight',
                html.Br(),
                ' yang lebih dari rata-rata, ',
                html.Span('sehingga perlu disiapkan antisipasi', style={'color': 'red'}),
                html.Br(),
                ' pada rentang waktu tersebut.'
            ]
        ),

        html.Div(
            style={"position": "absolute", 
                    "top": "2400px", 
                    "right": "90px",},
            children=[                
                html.P(
                    style={
                        'fontSize': '25px',
                        'font-family': 'Roboto',
                        'fontWeight': 'bold'
                                },
                    children=[
                        'Estimasi lonjakan penumpang ',
                    html.Br(),
                        'terjadi pada pukul: ',
                    dcc.Markdown(children=text_t3,
                                style={
                                    'fontSize': '25px',
                                    'font-family': 'Roboto',
                                    'fontWeight': 'bold',
                                    'color': 'red',
                                    }),      
                    'Di Terminal 3 pada rentang waktu tersebut',
                    html.Br(),
                    'memerlukan perhatian khusus oleh ',
                    html.Br(),
                    'tim yang bertugas.']),
                ]
        ), ### TEXT TERMINAL 3 - END
    
        ### DESIGN TERMINAL 1 - START
        html.Div(
            style={"display": "flex"},
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(image_t1),
                    style={"position": "absolute",
                            "top": "725px", 
                            "left": "120px",
                            'height': '400px', 
                            'width': '950px'
                            }
                           ),        
                html.Div(
                    style={"position": "absolute", 
                           "top": "700px", 
                            "right": "31%",
                           },
                    children=[
                        dash_table.DataTable(
                            id='table',
                            columns=[{'name': col, 'id': col} for col in data_t1[0].keys()],
                            data=data_t1,
                            style_data_conditional=[
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT1}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT1} && {{ARRIVAL FLIGHT}} < {mean_plusT1}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT1}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT1}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT1} && {{ARRIVAL FLIGHT}} < {mean_plusT1}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT1}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                            ],
                            style_data={'backgroundColor': '#f2f2f2', 'color': 'black'},
                            style_header={'backgroundColor': 'black', 'fontWeight': 'bold', 'color': 'white', 'width': '20px'},
                            style_cell={
                                        'textAlign': 'center',
                                        'fontSize': '17px',
                                        'height': '30px',
                                        'width': '100px'
                                        }
                        )
        
                    ]
                ),
            ],
            className="wrapper",
        ), ### DESIGN TERMINAL 1 - END

        ### DESIGN TERMINAL 2 - START
        html.Div(
            style={"display": "flex"},
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(image_t2),
                    style={"position": "absolute",
                            "top": "1525px", 
                            "left": "200px",
                            'height': '350px', 
                            'width': '800px'
                            }
                           ),        
                html.Div(
                    # style={'font-family': 'Arial, sans-serif'},
                    style={"position": "absolute", 
                           "top": "1500px", 
                            "right": "31%",
                           },
                    children=[
                        dash_table.DataTable(
                            id='table',
                            columns=[{'name': col, 'id': col} for col in data_t2[0].keys()],
                            data=data_t2,
                            style_data_conditional=[
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT2}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT2} && {{ARRIVAL FLIGHT}} < {mean_plusT2}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT2}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT2}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT2} && {{ARRIVAL FLIGHT}} < {mean_plusT2}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT2}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                            ],
                            style_data={'backgroundColor': '#f2f2f2', 'color': 'black'},
                            style_header={'backgroundColor': 'black', 'fontWeight': 'bold', 'color': 'white', 'width': '20px'},
                            style_cell={
                                        'textAlign': 'center',
                                        'fontSize': '17px',
                                        'height': '30px',
                                        'width': '100px'
                                        }
                        )
        
                    ]
                ),
            ],
            className="wrapper",
        ), ### DESIGN TERMINAL 2 - END   
        ### DESIGN TERMINAL 3 - START
        html.Div(
            style={"display": "flex"},
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(image_t3),
                    style={"position": "absolute",
                            "top": "2325px", 
                            "left": "200px",
                            'height': '350px', 
                            'width': '800px'
                            }
                           ),        
                html.Div(
                    # style={'font-family': 'Arial, sans-serif'},
                    style={"position": "absolute", 
                           "top": "2300px", 
                            "right": "31%",
                           },
                    children=[
                        dash_table.DataTable(
                            id='table',
                            columns=[{'name': col, 'id': col} for col in data_t3[0].keys()],
                            data=data_t3,
                            style_data_conditional=[
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT3}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT3} && {{ARRIVAL FLIGHT}} < {mean_plusT3}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'ARRIVAL FLIGHT',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT3}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} < {meanT3}'
                                    },
                                    'backgroundColor': 'lightgreen',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {meanT3} && {{ARRIVAL FLIGHT}} < {mean_plusT3}'
                                    },
                                    'backgroundColor': 'lemonchiffon',
                                    'color': 'black'
                                },
                                {
                                    'if': {
                                        'column_id': 'TIME',
                                        'filter_query': f'{{ARRIVAL FLIGHT}} >= {mean_plusT3}'
                                    },
                                    'backgroundColor': 'lightcoral',
                                    'color': 'black'
                                },
                            ],
                            style_data={'backgroundColor': '#f2f2f2', 'color': 'black'},
                            style_header={'backgroundColor': 'black', 'fontWeight': 'bold', 'color': 'white', 'width': '20px'},
                            style_cell={
                                        'textAlign': 'center',
                                        'fontSize': '17px',
                                        'height': '30px',
                                        'width': '100px'
                                        }
                        )
        
                    ]
                ),
            ],
            className="wrapper",
        ), ### DESIGN TERMINAL 3 - END           
    ]
)

# Print Report
print("\n\n== REPORT START HERE ==\n\n")
print(
    "Assalamu'alaikum warrahmatullahi wabarakatuh\n"
    "Selamat pagi rekan2 semua\n"
    "Izin Chief,  Bu yuni, Bapak/ Ibu leader, dan rekan-rekan semua.\n"
    f"izin menginformasikan Daily Report potensi kepadatan penumpang BMS sebagai berikut:\n\n"
    "*Daily Report Potensi Kepadatan Penumpang BMS*\n"
    f"_{hari_ini}_"
    "\n\n"
    "*TERMINAL 1*\n"
    f"Pada pukul {time_t1[0]} - {time_t1[-1]} memiliki jumlah est. jumlah arrival flight yang lebih dari rata-rata, sehingga perlu disiapkan antisipasi pada rentang waktu tersebut.\n"
    "Estimasi lonjakan penumpang terjadi pada pukul: ")
functions.get_info(df_t1, 1)
print(
    "\n\n"
    "*TERMINAL 2*\n"
    f"Pada pukul {time_t2[0]} - {time_t2[-1]} memiliki jumlah est. jumlah arrival flight yang lebih dari rata-rata, sehingga perlu disiapkan antisipasi pada rentang waktu tersebut.\n"
    "Estimasi lonjakan penumpang terjadi pada pukul: ")
functions.get_info(df_t2, 2)
print(
    "\n\n"
    "*TERMINAL 3*\n"
    f"Pada pukul {time_t3[0]} - {time_t3[-1]} memiliki jumlah est. jumlah arrival flight yang lebih dari rata-rata, sehingga perlu disiapkan antisipasi pada rentang waktu tersebut.\n"
    "Estimasi lonjakan penumpang terjadi pada pukul: ")
functions.get_info(df_t3, 3)
print(
    "\n\n"
    "Demikian disampaikan, atas perhatian dan perkenannya, diucapkan terimakasih\n"
    "Semangat untuk tim yang bertugas!"
    "\n\n"
)
print("== END REPORT ==")






                # ## Graph
                # html.Div(
                #     style={'height': '400px', 'width': '400px'},
                #     children=dcc.Graph(                      

                #         id="price-chart",
                #         config={"displayModeBar": False},
                #         figure={
                #             "data": [
                #                 {
                #                     "x": data1["Date"],
                #                     "y": data1["AveragePrice"],
                #                     "type": "lines",
                #                     "hovertemplate": (
                #                         "$%{y:.2f}<extra></extra>"
                #                     ),
                #                 },
                #             ],
                #             "layout": {
                #                 "title": {
                #                     "text": "Average Price of Avocados",
                #                     "x": 0.05,
                #                     "xanchor": "left",
                #                 },
                #                 "xaxis": {"fixedrange": True},
                #                 "yaxis": {
                #                     "tickprefix": "$",
                #                     "fixedrange": True,
                #                 },
                #                 "colorway": ["#17b897"],
                #             },
                #         },
                #     ),
                #     className="card",
                # ),


        #         html.Div(
        #     children=[
        #         html.Img(src=image_path),
        #         html.Img(src=app.get_asset_url('my-image.png')),
        #     ],
        #     style={"display": "flex"}
        # ),
                # html.Div(
                #     children=dcc.Graph(
                #         id="volume-chart",
                #         config={"displayModeBar": False},
                #         figure={
                #             "data": [
                #                 {
                #                     "x": data["Date"],
                #                     "y": data["Total Volume"],
                #                     "type": "lines",
                #                 },
                #             ],
                #             "layout": {
                #                 "title": {
                #                     "text": "Avocados Sold",
                #                     "x": 0.05,
                #                     "xanchor": "left",
                #                 },
                #                 "xaxis": {"fixedrange": True},
                #                 "yaxis": {"fixedrange": True},
                #                 "colorway": ["#E12D39"],
                #             },
                #         },
                #     ),
                #     className="card",
                # ),



if __name__ == "__main__":
    app.run_server(debug=True)


    