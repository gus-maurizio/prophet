#!/usr/bin/env python

import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('./example_wp_log_peyton_manning.csv.gz', compression='gzip')
df.head()

