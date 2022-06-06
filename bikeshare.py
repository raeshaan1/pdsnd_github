import time
import pandas as pd
import numpy as np

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nWhat is the name of the city that you will be analysing? (Choose between chicago, new york city, washington)\n")
    while city.lower() not in CITY_DATA:
        print("We do not have data for inputted city, please try again")
        city = input("\nWhat is the name of the city that you will be analysing? (Choose between chicago, new york city, washington)\n")

    print('Your selection is: ', city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWhat month would you like to filter to? (You may choose from january to june, or alternatively filter to 'all' for no filter)\n")
    while month.lower() not in MONTH_DATA:
        print("We might not have data for the inputted month, please try again")
        month = input("\nWhat month would you like to filter to? (You may choose from january to june, or alternatively filter to 'all' for no filter)\n")

    print('Your selection is: ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich day of the week would you like to filter to? (Choose any day of the week except 'thursday', or alternatively 'all' for no filter)\n")
    while day.lower() not in DAY_DATA:
        print("We do not have data for that inputted day please try again")
        day = input("\nWhich day of the week would you like to filter to? (Choose any day of the week except 'thursday', or alternatively 'all' for no filter)\n")

    print('Your selection is: ', day)

    print('-'*40)
    return city, month, day


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

    #Load city data
    print("\nLoading the data.....")
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #Filter by month
    if month != 'all':
        month = MONTH_DATA.index(month.lower())
        df = df.loc[df['month'] == month]

    #Filter by day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
       # TO DO: Display counts of gender
       gender = df['Gender'].value_counts()
       print("The count of user gender is: \n" + str(gender))

       # TO DO: Display earliest, most recent, and most common year of birth
       earliest_birth = df['Birth Year'].min()
       most_recent_birth = df['Birth Year'].max()
       most_common_birth = df['Birth Year'].mode()[0]
       print('Earliest birth is: {}\n'.format(earliest_birth))
       print('Most recent birth is: {}\n'.format(most_recent_birth))
       print('Most common birth is: {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):

    print(df.head())
    next = 0
    #Option to view next 10 rows
    while True:
        view_raw_data = input("\nWould you like to view next 10 rows of data? 'y'or'n'.\n")
        if view_raw_data.lower() != 'y':
            return
        next = next + 10
        print(df.iloc[next:next+10])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input("\nWould you like to view next 10 rows of data? 'y'or'n'.\n")
            if view_raw_data.lower() != 'y':
                break
            display_raw_data(df)
            break

        restart = input("\nWould you like to restart? 'y' or 'n'.\n")
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
