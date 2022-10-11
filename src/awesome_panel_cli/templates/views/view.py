import panel as pn


def view(value):
    return f"view of {value}"
    
if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")
    component = view("something")
    
    pn.template.FastListTemplate(title="View", main=[component]).servable()
