import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def gather_data():
    df = pd.read_csv("data/depression_dataset.csv")
    return df


def get_student_dataframe():
    """ Only evaluate students, gathering categorical data and numerical data that is relevant for students. """
    df = gather_data()

    student_dataframe = df[
        (df['Working Professional or Student'] == 'Student')
    ]

    student_dataframe.drop(columns=[
        'Profession', 'Work Pressure', 'Job Satisfaction', 'Financial Stress',
        'Family History of Mental Illness', 'Work/Study Hours', 'Working Professional or Student', 'City', 'Name'
    ], inplace=True, errors='ignore')

    return student_dataframe


def get_student_metrics_dataframe(df):
    """ Gather metrics data for students, such as CGPA, Dietary Habits and Sleep Hours distribution. """
    # Calculate CGPA distribution
    cgpa_below_6 = df[df['CGPA'] < 6]
    cgpa_6_to_8 = df[(df['CGPA'] >= 6) & (df['CGPA'] <= 8)]
    cgpa_above_8 = df[df['CGPA'] > 8]
    
    cgpa_distribution = pd.DataFrame({
        'CGPA Range': ['Below 6', '6 to 8', 'Above 8'],
        'Count': [len(cgpa_below_6), len(cgpa_6_to_8), len(cgpa_above_8)]
    })

    # Calculate dietary habits distribution
    dietary_habits_distribution = df['Dietary Habits'].value_counts().reset_index()
    dietary_habits_distribution.columns = ['Dietary Habits', 'Count']
    dietary_habits_distribution = dietary_habits_distribution.sort_values(by='Count', ascending=False)

    # Calculate sleep hours distribution
    sleep_hours_distribution = df['Sleep Duration'].value_counts().reset_index()
    sleep_hours_distribution.columns = ['Sleep Duration', 'Count']
    sleep_hours_distribution = sleep_hours_distribution.sort_values(by='Count', ascending=False)

    return cgpa_distribution, dietary_habits_distribution, sleep_hours_distribution


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
        fit_columns_on_grid_load=False,
    )