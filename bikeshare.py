import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': './data/chicago.csv',
              'New York': './data/new_york_city.csv',
              'Washington': './data/washington.csv' }

city_list = ['Washington', 'New York', 'Chicago']
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Your choices are Washington, New York or Chicago")

    city = input("Enter the name of the city you would like to explore: ")
    
    print("Great your chosen city is: " + city)

    while (city not in city_list or city == ''):
        city = input("Incorrect entry, please enter the name of one of the three selected cities")


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

city_x, month_y, day_z = get_filters()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Create the data frame based on user filters
    df = pd.read_csv(CITY_DATA[city])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.week_day
    

    #Filter by month if required
    if month != 'All':
        months = month_list
        months = months.index(month) + 1

        #Filter data frame by month
        df = df[df['month'] == month]

    #Filter by month if required
    

    return df

data_frame = load_data(city_x, month_y, day_z)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#def station_stats(df):
  #  """Displays statistics on the most popular stations and trip."""

 #   print('\nCalculating The Most Popular Stations and Trip...\n')
  #  start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


   # print("\nThis took %s seconds." % (time.time() - start_time))
   # print('-'*40)


#def trip_duration_stats(df):
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


#def main():
 #   while True:
  #      city, month, day = get_filters()
   #     df = load_data(city, month, day)

    #    time_stats(df)
     #   station_stats(df)
      #  trip_duration_stats(df)
       # user_stats(df)

       # restart = input('\nWould you like to restart? Enter yes or no.\n')
       # if restart.lower() != 'yes':
        #    break


#if __name__ == "__main__":
#	main()
