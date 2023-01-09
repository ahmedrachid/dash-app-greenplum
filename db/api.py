import pathlib
import pandas as pd
from sqlalchemy import create_engine

con  = create_engine('postgresql+psycopg2://gpadmin:changeme@10.208.134.51/test2')
#db = gp.database(
#        host="35.241.130.38",
#        dbname="dev",
#        user="gpadmin",
#        password="79kq97lCaWrFn",
#    )

#db = gp.database(
#        host="10.208.134.51",
#        dbname="test2",
#        user="gpadmin",
#        password="changeme",
#    )

def get_wind_data(start, end):
    """
    Query wind data rows between two ranges

    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    """
    print(start, end)
    statement = f'SELECT index,speed, speederror, direction FROM wind_speed WHERE index > {start} AND index <= {end};'
    df = pd.read_sql_query(statement, con)
    print(len(df))
    return df

def get_data_count():
    """
    Query wind data rows between two ranges

    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    """
    statement = f'SELECT count(*) FROM wind_speed;'
    df = pd.read_sql_query(statement, con)
    return df



def get_wind_data_by_id(id):
    """
    Query a row from the Wind Table

    :params id: a row id
    :returns: pandas dataframe object
    """


    statement = f'SELECT index,speed, speederror, direction FROM wind_speed WHERE index = {id};'
    df = pd.read_sql_query(statement, con)
    return df

