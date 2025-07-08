import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def gather_data():
    df = pd.read_csv("data/penguins.csv")
    df.rename(columns={
        "culmen_length_mm": "Culmen Length (mm)",
        "culmen_depth_mm": "Culmen Depth (mm)",
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "sex": "Sex"
    }, inplace=True)
    return df

def with_empty_values(df):
    return df[df.isnull().any(axis=1)]

def without_empty_values(df):
    return df.dropna()

def display_dataframe(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_side_bar()
    gridOptions = gb.build()

    AgGrid(
        df,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        allow_unsafe_jscode=True,
        theme="streamlit",
        fit_columns_on_grid_load=True,
    )