from datetime import datetime, timedelta

def endtime():
    """
        Return datetime of 30 days from today.
        >> today+30days
    """
    time = datetime.now()
    delta = timedelta(days=30)
    target_date = time + delta
    return target_date