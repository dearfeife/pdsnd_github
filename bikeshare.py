import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
           city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
           if city not in ('chicago','new york city','washington'):
                print("Please enter a valid input")
                continue
           break
           
   
              
    while True:
                    
           month = input("Which month - January, February, March, April, May, or June?").lower()
           if month not in ("january", "february", "march", "april", "may", "june","all"):
                 print("Please enter a valid input")
                 continue
           break
        
    while True:
       
           day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()  
           if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",'all'):
                print("Please enter a valid input")
                continue
           break
             
            
    return city,month,day    
    print('-'*40)
    


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    try:
        # TO DO: display the most common month
        most_common_month = df['month'].mode()[0]
        print("The most popular month : "+ str(most_common_month))
        # TO DO: display the most common day of week
        most_common_dayofweek = df['day_of_week'].mode()[0]
        print("The most popular day of week : "+ str(most_common_dayofweek))
        # TO DO: display the most common start hour
        most_common_hour = df['hour'].mode()[0]
        print("The most popular hour : "+ str(most_common_hour))
    except KeyError:
        print("No data for times of travel")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
            # TO DO: display most commonly used start station
        most_common_start = df['Start Station'].value_counts().idxmax()
        print("The most common start station: " + most_common_start)
        # TO DO: display most commonly used end station
        most_common_end = df['End Station'].value_counts().idxmax()
        print("The most common end station: " + most_common_end)
        # TO DO: display most frequent combination of start station and end station trip
        combine_stations = df['Start Station'] + " and "+ df['End Station']
        most_comb_station = combine_stations.value_counts().idxmax()
        print("The most frequent combination of start station and end station trip station: " + most_comb_station)
        
    except KeyError:
        print("No data for station")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        # TO DO: display total travel time
        total_duration = df['Trip Duration'].sum()
        print("Total travel time " + str(total_duration))
        # TO DO: display mean travel time
        mean_duration = df['Trip Duration'].mean()
        print("Average travel time " + str(mean_duration))
    except KeyError:
        print("No data for trip duration")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        count_usertype = df['User Type'].value_counts()
        print("User types: \n" + str(count_usertype))
        # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts()
        print("Genders:\n " + str(count_gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year is " + str(int(earliest_year)))
        recent_year = df['Birth Year'].max()
        print("The most recent birth year is " + str(int(recent_year)))
        common_year = df['Birth Year'].mode()[0]
        print("The most common birth year is " + str(int(common_year)))
    except KeyError:
        print("No data for user type")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    i = 0
    raw = input('Do you want to see raw data? yes/no ')
    while True:
        if raw.lower() == 'yes':
            print(df.iloc[i:i+5])
            see_more = input("Do you want to see more 5 lines of raw data?").lower()
            if see_more == 'yes':
                i += 5
                continue
            else:
                break
        break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
