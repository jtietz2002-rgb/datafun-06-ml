import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    from sklearn.datasets import fetch_california_housing

    housing = fetch_california_housing()
    print(housing.data.shape, housing.target.shape)
    print(housing.feature_names[0:6])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
