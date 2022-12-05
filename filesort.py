import os
from datetime import date
from datetime import timedelta


if __name__ == "__main__":
    source = "Z:/imgs/"
    destination = "Z:/imgs/sort/"

    for f in os.listdir(source):
        if os.path.isdir(source + f):
            continue

        timestamp = os.stat(source + f).st_ctime
        creation_date = date.fromtimestamp(timestamp)
        week_day = creation_date.weekday()
        save_date = str(creation_date - timedelta(days=week_day))

        # todo -  add different treatment for videos vs images?

        if os.path.isdir(destination + save_date + "/") is False:
            os.makedirs(destination + save_date + "/")

        if os.path.exists(destination + save_date + "/" + f):
            continue
            
        os.rename(source + f, destination + save_date + "/" + f)
        