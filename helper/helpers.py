"""
"""

from datetime import datetime

def cd_to_datetime(calendar_date):
    """ Convert a NASA-formatted calendar data (cd) into a datetime.
    `calendar_date` comes from `cd` variable in `CloseApproach` object.

    Arguments:
    :calendar_date {str} e.g., '2099-Dec-31 20:51'

    Returns:
    : {datatime} datetime.datetime(2099, 12, 31, 20, 51)
    """
    return datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")


def datetime_to_str(dt):
    """ ConvertPython datetime into a human-readable string.

    Arguments:
    :dt {datetime} e.g., datetime.datetime(2099, 12, 31, 20, 51)

    Returns:
    : {str} '2099-12-31 20:51'
    """
    return datetime.strftime(dt, "%Y-%m-%d %H:%M")
