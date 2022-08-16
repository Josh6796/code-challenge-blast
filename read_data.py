import pandas as pd
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, "%m/%d/%Y - %H:%M:%S")

for line in pd.read_table("data/NAVIvsVitaGF-Nuke.txt", chunksize=1, header=None, encoding="utf-8"):
    line_string = line.iloc[0,0]
    log_timestamp = dateparse(line_string[:21])
    actual_message = line_string[23:]