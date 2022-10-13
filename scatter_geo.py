from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px


mydataset = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"

df = pd.read_csv(mydataset, encoding="latin")
df.dropna(inplace=True)
df["Elev"] = abs(df["Elev"])

app = Dash(__name__)
server = app.server


app.layout = html.Div([
    html.Header("Volcano Map Dash App", style={"fontSize": 40,
                                               "textAlign": "center"}),
    dcc.Dropdown(id="mydropdown",
                 options=df["Type"].unique(),
                 value="Stratovolcano",
                 style={"width": "50%", "margin-left": "130px", "margin-top": "60px"}),
    dcc.Graph(id="my_scatter_geo")
])


@app.callback(Output("my_scatter_geo", "figure"),
              Input("mydropdown", "value"))
def sync_input(volcano_selection):
    fig = px.scatter_geo(df.loc[df["Type"] == volcano_selection],
                         lat="Latitude",
                         lon="Longitude",
                         size="Elev",
                         hover_name="Volcano Name")
    return fig


if __name__ == "__main__":
    app.run_server(debug=False)
