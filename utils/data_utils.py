import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import seaborn as sb


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


def get_metric_correlation_quadrant(df):
    """ Get the correlation quadrant for the previous metric """
    quadrant = df[df[['CGPA', 'Study Satisfaction', 'Sleep Duration', 'Dietary Habits', 'Depression']].notnull().all(axis=1)]

    # If 7-8 hours, rate as 3, more than that rate as 2, less than 7 rate as 1 and less than 5 rate as 0
    # the values appear as 7-8 hours, 5-6 hours, More than 8 hours, Less than 5 hours
    sleep_mapping = {
        '7-8 hours': 3,
        '5-6 hours': 2,
        'More than 8 hours': 2,
        'Less than 5 hours': 0
    }
    quadrant['Sleep Duration'] = quadrant['Sleep Duration'].map(sleep_mapping)

    dietary_mapping = {
        'Healthy': 3,
        'Moderate': 2,
        'Unhealthy': 1
    }
    quadrant['Dietary Habits'] = quadrant['Dietary Habits'].map(dietary_mapping)

    depression_mapping = {
        'No': 0,
        'Yes': 1
    }
    quadrant['Depression'] = quadrant['Depression'].map(depression_mapping)

    return quadrant[['CGPA', 'Study Satisfaction', 'Sleep Duration', 'Dietary Habits', 'Depression']].corr(method='pearson').round(2)


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
