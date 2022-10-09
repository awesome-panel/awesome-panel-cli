"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Altair. It supports both light and dark theme.
"""
import altair as alt
import panel as pn
from vega_datasets import data


def get_panel_theme() -> str:
    """Returns the name of the active theme"""
    try:
        return pn.state.session_args["theme"][0].decode(encoding="utf8")
    except:
        return "default"


def set_altair_theme(panel_theme):
    """Sets the Altair Theme"""
    if panel_theme == "dark":
        alt.themes.enable("dark")
    else:
        alt.themes.enable("default")


def get_plot():
    return (
        alt.Chart(data.cars())
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .properties(
            height="container",
            width="container",
        )
        .interactive()
    )


pn.extension("vega", sizing_mode="stretch_width")

theme = get_panel_theme()
set_altair_theme(theme)

plot = get_plot()

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Altair",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    main=[__doc__, pn.panel(plot, min_height=600, sizing_mode="stretch_both")],
).servable()
