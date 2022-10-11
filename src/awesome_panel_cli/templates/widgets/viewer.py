import panel as pn
import param


class CustomModel(param.Parameterized):
    value = param.String()


def custom_view(model, **params):
    return pn.widgets.TextInput.from_param(
        model.param.value, name="🚀 Enter your value below", **params
    )


class CustomWidget(CustomModel, pn.viewable.Viewer):
    def __init__(self, value, view=custom_view, **params):
        super().__init__(value=value)

        self._panel = view(self, **params)

    def __panel__(self):
        return self._panel


if __name__.startswith("bokeh"):
    pn.extension()
    widget = CustomWidget("value")

    pn.template.FastListTemplate(
        title="Widget Viewer",
        main=[widget, widget.param.value],
    ).servable()
