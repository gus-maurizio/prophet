#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from fbprophet import Prophet



def colorPoints(	forecast=None,
					m=None,
					axe=None, 	
					forecolor=['b+','g+','r+','c+','m+','y+','k+'],
					modelcolor=['b.','g.','r.','c.','m.','y.','k.'],
				):
	colors_fcst = forecolor
	colors_orig = modelcolor

	b_patch = mpatches.Patch(color='blue',  label='Monday')
	g_patch = mpatches.Patch(color='green', label='Tuesday')
	r_patch = mpatches.Patch(color='red',   label='Wednesday')
	c_patch = mpatches.Patch(color='cyan',  label='Thursday')
	m_patch = mpatches.Patch(color='magenta', label='Friday')
	y_patch = mpatches.Patch(color='yellow',  label='Saturday')
	k_patch = mpatches.Patch(color='black',   label='Sunday')
	for day in range(7):
		day_forecast = forecast[forecast['ds'].dt.dayofweek == day] 
		day_samples  = m.history[m.history['ds'].dt.dayofweek == day] 
		axe.plot(day_forecast['ds'], day_forecast['yhat'], colors_fcst[day])
		axe.plot(day_samples['ds'], day_samples['y'], colors_orig[day])
	plt.legend(handles=[b_patch,g_patch,r_patch,c_patch,m_patch,y_patch,k_patch])


df = pd.read_csv('./example_wp_log_peyton_manning.csv.gz', compression='gzip')
print(df.head())
print(df.describe())

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
print(future.tail(10))

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


fig1 = m.plot(	forecast, 
				xlabel='time',
				ylabel='Peyton',
				figsize=(28,16))
# Extract the axis from the figure
ax1 = fig1.gca()
# add a color for each day in the 0-6 range 0 Monday 6 is Sunday
colorPoints(m=m, forecast=forecast,axe=ax1)
plt.show()


fig2 = m.plot_components(forecast, figsize=(28,16))
plt.show()
