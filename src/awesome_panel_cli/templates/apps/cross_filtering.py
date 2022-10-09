"""*Cross Filtering* is a very powerful technique. It's also known as
*Linked Selections* or *Linked brushing*.

This example is inspired by the HoloViews [Linked Brushing Reference Guide]\
(http://holoviews.org/user_guide/Linked_Brushing.html) and the Plotly blog post
[Introducing Dash HoloViews]\
(https://medium.com/plotly/introducing-dash-holoviews-6a05c088ebe5).
This example uses the *Iris* dataset.
"""
import holoviews as hv
import hvplot.pandas
import panel as pn
from bokeh.sampledata.iris import flowers

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

accent_color = "#ff286e"


def get_plot():
    scatter = flowers.hvplot.scatter(
        x="sepal_length", y="sepal_width", c=accent_color, responsive=True, height=300
    )
    hist = flowers.hvplot.hist("petal_width", c=accent_color, responsive=True, height=300)

    scatter.opts(size=10)

    selection_linker = hv.selection.link_selections.instance()

    scatter = selection_linker(scatter)
    hist = selection_linker(hist)

    scatter.opts(tools=["hover"], active_tools=["box_select"])
    hist.opts(tools=["hover"], active_tools=["box_select"])

    return (scatter + hist).cols(1)


plot = get_plot()

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Cross Filtering",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    header_background=accent_color,
    main=[__doc__, plot],
).servable()
