from typing import Tuple

import panel as pn
import param


class PhoneNumberModel(param.Parameterized):

    value: str = param.String(label="Phone Number")

    country: str = param.Selector(objects=["DK", "DE"], label="Country")
    local: str = param.String(label="Local")

    def __init__(self, value, **params):
        super().__init__(value=value, **params)

    @staticmethod
    def to_value(country: str, local: str) -> str:
        if country == "DK":
            return "+45 " + local
        return "+49 " + local


    @staticmethod
    def from_value(value: str) -> Tuple[str, str]:
        if " " in value:
            country, local = value.split(" ")
            if country == "+45":
                country = "DK"
            else:
                country = "DE"
        else:
            country = "DK"
            local = ""
        return country, local

    @param.depends("country", "local", watch=True)
    def _handle_input_changed(self):
        self.value = self.to_value(self.country, self.local)

    @param.depends("value", watch=True, on_init=True)
    def _handle_value_changed(self):
        self.country, self.local = self.from_value(self.value)


def phone_number_view(model: PhoneNumberModel, **params):
    country = pn.widgets.Select.from_param(model.param.country, sizing_mode="fixed", width=75)
    local = pn.widgets.TextInput.from_param(model.param.local, sizing_mode="stretch_width")
    return pn.Row(country, local, **params)



class PhoneNumberInput(PhoneNumberModel, pn.viewable.Viewer):

    def __init__(self, value, view=phone_number_view, **params):
        super().__init__(value=value, **params)

        self._panel = view(model=self, **params)

    def __panel__(self):
        return self._panel


if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    phone_number = PhoneNumberInput("+45 97182099")
    component = pn.Column(
        phone_number,
        pn.widgets.TextInput.from_param(phone_number.param.value, disabled=True),
        width=400,
        sizing_mode="fixed",
    )
    pn.template.FastListTemplate(title="Viewer Widget", main=[component],).servable()
