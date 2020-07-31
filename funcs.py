import plotly.graph_objects as go
import pandas as pd


def make_fig(labels, source, target, value, colors, diagram_name):
    fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = colors
    ),
    link = dict(
      source = source,
      target = target,
      value = value
    ))])

    fig.update_layout(title_text=diagram_name, font_size=10)
    fig.show()

def get_data(csv_file):
    data = pd.read_csv(f"data/{csv_file}")
    df = data.drop("labels", 1)
    labels = [col for col in data.columns if col != "labels"]
    return df.values.tolist() + [labels] # source - target - value - nan - color
