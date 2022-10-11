import panel as pn

RAW_CSS = """
.avatar {
  vertical-align: middle;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}
"""
if not RAW_CSS in pn.config.raw_css:
    pn.config.raw_css.append(RAW_CSS)


def avatar(
    user: str, image: str, height: int = 50, width: int = 50, sizing_mode: str = "fixed", **params
):
    """An Avatar defined"""
    return pn.pane.HTML(
        f"""<img src="{image}" alt="Avatar" class="avatar" title="{user}">""",
        height=height,
        width=width,
        sizing_mode=sizing_mode,
        **params,
    )


if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    component = pn.Row(
        avatar("Philipp", "https://avatars.githubusercontent.com/u/1550771?v=4"),
        avatar(user="Marc", image="https://avatars.githubusercontent.com/u/42288570?v=4",),
    )

    pn.template.FastListTemplate(title="View HTML", main=[component]).servable()