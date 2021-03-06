__author__ = 'sms'
from pandas import *
from ggplot import *
import brewer2mpl
import pylab
import matplotlib.pyplot as plt

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    turnstile_dt = turnstile_weather[["DATETIMEn", "ENTRIESn_hourly", "EXITSn_hourly"]] \
               .set_index("DATETIMEn") \
               .sort_index()
    print turnstile_dt.head(n=3)
    turnstile_day = turnstile_dt
    turnstile_day["day"] = turnstile_day.index.weekday
    turnstile_day = turnstile_day[["day", "ENTRIESn_hourly"]].groupby("day").agg(sum)
    fig, ax = plt.subplots(figsize=(12, 7))
    turnstile_day.plot(ax=ax, kind="bar")
    ax.set_title("Ridership by day of week")
    ax.set_ylabel("Entries per hour")
    ax.set_xticklabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                   rotation=360)
    ax.set_xlabel("Day of the week")
    plt.show()


if __name__ == "__main__":
    turnstile_weather = pandas.read_csv("C:/learning/Udacity/Intro to Data Scinece/intro_to_ds_programming_files/project_3/plot_histogram/turnstile_data_master_with_weather.csv")
    turnstile_weather["DATETIMEn"] = pandas.to_datetime(turnstile_weather["DATEn"] + " " + turnstile_weather["TIMEn"], format="%Y-%m-%d %H:%M:%S")
    plot_weather_data(turnstile_weather)