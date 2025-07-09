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
    quadrant = df[df[['CGPA', 'Study Satisfaction', 'Sleep Duration', 'Dietary Habits', 'Depression', 'Have you ever had suicidal thoughts ?']].notnull().all(axis=1)].copy()

    sleep_mapping = {
        '7-8 hours': 1,
        '5-6 hours': 0,
        'More than 8 hours': -1,
        'Less than 5 hours': -1
    }
    quadrant['Sleep Duration'] = quadrant['Sleep Duration'].map(sleep_mapping)

    dietary_mapping = {
        'Healthy': 1,
        'Moderate': 0,
        'Unhealthy': -1
    }
    quadrant['Dietary Habits'] = quadrant['Dietary Habits'].map(dietary_mapping)

    depression_mapping = {
        'No': 0,
        'Yes': 1
    }
    quadrant['Depression'] = quadrant['Depression'].map(depression_mapping)

    quadrant['Study Satisfaction'] = pd.to_numeric(quadrant['Study Satisfaction'], errors='coerce')

    study_bins = [-float('inf'), 2.999, 4, float('inf')]
    study_labels = [-1, 0, 1]  # -1 for 'Below 3', 0 for '3 to 4', 1 for 'Above 4

    quadrant['Study Satisfaction'] = pd.cut(quadrant['Study Satisfaction'], bins=study_bins, labels=study_labels)

    quadrant['CGPA'] = pd.to_numeric(quadrant['CGPA'], errors='coerce')

    bins = [-float('inf'), 5.999, 8, float('inf')]
    labels = [-1, 0, 1]  # -1 for 'Below 6', 0 for '6 to 8', 1 for 'Above 8'
    
    quadrant['CGPA'] = pd.cut(quadrant['CGPA'], bins=bins, labels=labels)

    quadrant['CGPA'] = quadrant['CGPA'].astype(int)

    quadrant['Have you ever had suicidal thoughts ?'] = quadrant['Have you ever had suicidal thoughts ?'].map(depression_mapping)

    return quadrant[['CGPA', 'Study Satisfaction', 'Sleep Duration', 'Dietary Habits', 'Depression', 'Have you ever had suicidal thoughts ?']].corr(method='pearson').round(2)


def get_worker_dataframe():
    """ Only evaluate workers, gathering categorical data and numerical data that is relevant for workers. """
    df = gather_data()

    worker_dataframe = df[
        (df['Working Professional or Student'] == 'Working Professional')
    ]

    worker_dataframe.drop(columns=[
        'CGPA', 'Study Satisfaction', 'Working Professional or Student', 'City', 'Name'
    ], inplace=True, errors='ignore')

    return worker_dataframe


def get_worker_metrics_dataframe(df):
    """ Gather metrics data for workers, such as Work Pressure, Job Satisfaction and Financial Stress distribution. """
    # Calculate work pressure distribution
    work_pressure_distribution = df['Work Pressure'].value_counts().reset_index()
    work_pressure_distribution.columns = ['Work Pressure', 'Count']
    work_pressure_distribution = work_pressure_distribution.sort_values(by='Count', ascending=False)

    # Calculate job satisfaction distribution
    job_satisfaction_distribution = df['Job Satisfaction'].value_counts().reset_index()
    job_satisfaction_distribution.columns = ['Job Satisfaction', 'Count']
    job_satisfaction_distribution = job_satisfaction_distribution.sort_values(by='Count', ascending=False)

    # Calculate financial stress distribution
    financial_stress_distribution = df['Financial Stress'].value_counts().reset_index()
    financial_stress_distribution.columns = ['Financial Stress', 'Count']
    financial_stress_distribution = financial_stress_distribution.sort_values(by='Count', ascending=False)

    return work_pressure_distribution, job_satisfaction_distribution, financial_stress_distribution


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
