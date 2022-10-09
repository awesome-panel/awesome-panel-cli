"""This example shows a streaming dashboard with Panel.
Panel runs on top of the Tornado server. Tornado is a fast, asynchronous web server built to
support streaming use cases.

You can run `some_function` periodically via
`pn.state.add_periodic_callback(some_function, period=1000, count=200)`.
"""
import numpy as np
import panel as pn

pn.extension(sizing_mode="stretch_width")

layout = pn.layout.FlexBox(
    *(
        pn.indicators.Trend(
            data={"x": list(range(10)), "y": np.random.randn(10).cumsum()},
            width=150,
            height=100,
            plot_type=pn.indicators.Trend.param.plot_type.objects[i % 4],
        )
        for i in range(32)
    )
)


def stream():
    for trend in layout:
        trend.stream(
            {"x": [trend.data["x"][-1] + 1], "y": [trend.data["y"][-1] + np.random.randn()]},
            rollover=20,
        )


periodic_callback = pn.state.add_periodic_callback(stream, 1000)

period_input = pn.widgets.IntInput.from_param(periodic_callback.param.period, sizing_mode="fixed")
checkbox_input = pn.widgets.Checkbox.from_param(
    periodic_callback.param.running, align="end", sizing_mode="fixed"
)
controls = pn.Row(period_input, checkbox_input)

pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Streaming Indicators",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
    main=[
        pn.Column(
            __doc__,
            controls,
        ),
        layout,
    ],
).servable()
