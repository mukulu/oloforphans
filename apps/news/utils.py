from datetime import datetime, timedelta

def endtime():
    time = datetime.now()
    delta = timedelta(days=30)
    target_date = time + delta
    return target_date