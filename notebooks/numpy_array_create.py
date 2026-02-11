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
    import random


    # Create a state object that will store the index of the
    # clicked button
    get_state, set_state = mo.state(None)

    # Create an mo.ui.array of buttons - a regular Python list won't work.
    buttons = mo.ui.array(
        [
            mo.ui.button(
                label="button " + str(i), on_change=lambda v, i=i: set_state(i)
            )
            for i in range(random.randint(2, 5))
        ]
    )

    mo.hstack(buttons)
    return


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
def _(np, pd):
    x = np.linspace(start=0, stop=100, num=100, dtype=float)
    y = np.zeros_like(x) # dict of two np array

    data = {'x': x, 'y': y}

    df_numberline = pd.DataFrame(data)
    df_numberline.describe()
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
