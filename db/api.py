import pathlib
import greenplumpython as gp


db = gp.database(
        host="",
        dbname="dev",
        user="gpadmin",
        password="",
    )

def get_wind_data(start, end):
    """
    Query wind data rows between two ranges

    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    """

    df  = db.table('wind_speed_generation')
    df = df[lambda t: t["index"] > start and t['index'] <  end ]
    df = df.to_dataframe()

    return df


def get_wind_data_by_id(id):
    """
    Query a row from the Wind Table

    :params id: a row id
    :returns: pandas dataframe object
    """

    df = db.table('wind_speed_generation')
    df = df[lambda t: t["index"] == id ]
    df = df.to_dataframe()

    return df
