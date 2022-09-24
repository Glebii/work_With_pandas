import numpy as np
import pandas as pd
import matplotlib
import time

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def main():
    print("-----------------EXERCISE D-------------")
    data = pd.read_csv("temp_fuhlsbuettel_akt.txt",
                       delimiter=";",
                       names=['id', 'datetime', 'qn_9', 'temperature', 'rf_tu', 'eor'],
                       )
    dataframe = pd.DataFrame(data)
    dataframe.drop(index=[0], axis=0, inplace=True)
    print(dataframe)

    exercise_e_f(dataframe)


def exercise_e_f(data):
    print("-----------------EXERCISE E & F-------------")
    format_for_parsing = '%Y%m%d%H'
    format_of_datetime_index = '%Y-%m-%d %H:00:00'
    start_date = time.strftime(format_of_datetime_index,
                               time.strptime(
                                   data.iloc[0]['datetime'], format_for_parsing
                               )
                               )
    end_date = time.strftime(format_of_datetime_index,
                             time.strptime(
                                 data.iloc[-1, :]['datetime'], format_for_parsing
                             )
                             )

    data.index = pd.date_range(start=start_date, end=end_date, freq="1H")
    data[['temperature']] = data[['temperature']].astype(float)
    data.drop(['id', 'datetime', 'qn_9', 'rf_tu', 'eor'], axis=1, inplace=True)
    print(data)
    exercise_g(data)


def exercise_g(data):
    print("-----------------EXERCISE G-------------"
          "\n{Temperature change as a percentage relative to the previous value}\n")
    data['relation to the previous value'] = data.pct_change(data["temperature"].any())
    print(data)
    min_temperature = data['temperature'].min()
    max_temperature = data['temperature'].max()
    average_temperature = data['temperature'].mean()
    median_temperature = data['temperature'].median()
    print(
        f'The default statistics:\nMaximum temperature value - {max_temperature}\nMinimum temperature value - {min_temperature}'
        f'\nAverage temperature value - {round(average_temperature, 2)}\nMedian temperatures - {median_temperature}')

    exercise_h(data)


def exercise_h(data):
    # data.plot()
    pass


if __name__ == '__main__':
    main()
