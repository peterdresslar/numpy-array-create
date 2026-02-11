import marimo

__generated_with = "0.19.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import pandas as pd
    import json
    import marimo as mo
    import numpy as np

    return alt, mo, np, pd


@app.cell
def _(mo):
    sliders = mo.ui.array(
        [
            mo.ui.slider(start=0, stop=100, label="Start", value = 0),
            mo.ui.slider(start=0, stop=100, label="Stop", value = 50),
            mo.ui.slider(start=0, stop=100, label="Step / Num", value = 1),
    ])

    return (sliders,)


@app.cell
def _(mo, sliders):
    mo.hstack(sliders)
    return


@app.cell
def _(sliders):
    slider_values = sliders.value
    print(slider_values[0], slider_values[1], slider_values[2])
    return (slider_values,)


@app.cell
def _(np, pd, slider_values):
    x = np.linspace(start=slider_values[0], stop=slider_values[1], num=slider_values[2], dtype=float)
    y = np.zeros_like(x) # dict of two np array

    data = {'x': x, 'y': y}

    df_numberline = pd.DataFrame(data)
    df_numberline.head(3)
    return (df_numberline,)


@app.cell
def _(alt, df_numberline):
    alt.Chart(df_numberline).mark_point().encode(
        x='x',
        y='y',
    ).interactive()
    return


if __name__ == "__main__":
    app.run()
