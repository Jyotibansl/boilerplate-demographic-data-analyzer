import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    adultdata_path = 'adult_data.csv'
    df = pd.read_csv(adultdata_path)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex']== 'Male']
    average_age_men = df_men['age'].mean().__round__(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_people = len(df[df['education']=='Bachelors'])
    percentage_bachelors = ((bachelors_people*100)/total_people).__round__(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'] .isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_higher_education = len(higher_education)
    salary_advanced = higher_education[higher_education['salary'] == '>50K']
    total_salary_advanced = len(salary_advanced)
    lower_education = df[~df['education'] .isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_lower_education = len(lower_education)
    salary_less = lower_education[lower_education['salary'] == '>50K']
    total_salary_less = len(salary_less)

    # percentage with salary >50K
    higher_education_rich = ((total_salary_advanced*100)/total_higher_education).__round__(1)
    lower_education_rich = ((total_salary_less*100)/total_lower_education).__round__(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_hour_workercount = len(num_min_workers)
    salary_more = num_min_workers[num_min_workers['salary'] == '>50K']
    salary_more_count = len(salary_more)
    rich_percentage = ((salary_more_count*100)/min_hour_workercount).__round__(1)

    # What country has the highest percentage of people that earn >50K?
    total_per_country = df['native-country'].value_counts()
    over_50k_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_over_50k_per_country = ((over_50k_per_country / total_per_country) * 100).round(1)  
    highest_earning_country = percentage_over_50k_per_country.idxmax()

    highest_earning_country_percentage = percentage_over_50k_per_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    India_earnmorethan50k = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    occupation_count = India_earnmorethan50k['occupation'].value_counts()
    top_IN_occupation = occupation_count.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
