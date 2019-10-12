import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': './data/chicago.csv',
              'New York': './data/new_york_city.csv',
              'Washington': './data/washington.csv' }

city_list = ['Washington', 'New York', 'Chicago']
month_list = ['January', 'February', 'March', 'April', 'May', 'June']
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Your choices are Washington, New York or Chicago")

    city = input("Enter the name of the city you would like to explore: ")
    
    print("Great your chosen city is: " + city)

    while (city not in city_list or city == ''):
        city = input("Incorrect entry, please enter the name of one of the three selected cities: ")


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month you would like to investigate: ")

    while(month not in month_list or month == ''):
        month = input("Incorrect Entry, please enter the correct month with capital letters: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day would like to investigate: ")
    while(day not in day_list or day == ''):
        day = input("Incorrect Entry, please enter correct day with capital letters: ")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = month_list
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print("The Most popular month is " + str(month_list[popular_month - 1]))


    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day of the week is " + str(popular_day))


    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The Most popular hour is " + str(popular_hour) + ":00 h")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_station_start = df['Start Station'].mode()[0]
    print("The most popular start station is " + str(popular_station_start))

    # Display most commonly used end station
    popular_station_end = df['End Station'].mode()[0]
    print("The most popular end station is " + str(popular_station_end))

    # Display most frequent combination of start station and end station trip
    overall_station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print("The most popular combination is " + str(overall_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
   # """Displays statistics on the total and average trip duration."""

 #   print('\nCalculating Trip Duration...\n')
  #  start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


   # print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


#def user_stats(df):
 #   """Displays statistics on bikeshare users."""

 #   print('\nCalculating User Stats...\n')
  #  start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


   # print("\nThis took %s seconds." % (time.time() - start_time))
   # print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
      #  trip_duration_stats(df)
       # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
