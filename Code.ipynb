#create an empty list to store url list of movies.
url_list = []

# Iterate through a range of numbers from 1 to 42 (inclusive)
for i in range(1,43):
    # url is mo metacritic website
    url = 'https://www.metacritic.com/browse/movie/?releaseYearMin=1910&releaseYearMax=2023&page=' + str(i)
    #append the url in the 'url_list'
    url_list.append(url)
# print url list    
url_list

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define user-agent header
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# Initialize an empty list to store URLs of individual movie pages
movie_1000 = []

#use for loop to store the url in the list
for i in url_list:
    html = requests.get(i, headers = headers)
    soup = BeautifulSoup(html.content, "html.parser")
    hyperlink_list = soup.find_all('a', class_ = "c-finderProductCard_container g-color-gray80 u-grid")
    for i in hyperlink_list:
        movie_page = 'https://www.metacritic.com' + i['href']
        movie_1000.append(movie_page)

print(len(movie_1000))
print(movie_1000)

#import requests
#from bs4 import BeautifulSoup

# Initialize an empty dictionary to store information about directors and cast for each movie
dict_1000 = {}
# Initialize variable for tracking the number of processed movies
n = 0

for i in movie_1000:
    # getting all the 3 information from each movie
    n = n + 1 
    print(n)
    # Send an HTTP GET request to the current movie page URL
    movie_page = requests.get(i, headers=headers)
    
    # Create a BeautifulSoup object to parse the HTML content of the movie page
    movie_page_soup = BeautifulSoup(movie_page.content, "html.parser") 
    
    # Find all elements containing movie names on the page
    movie_name_list = movie_page_soup.find_all('div', class_="c-productHero_title g-inner-spacing-bottom-medium g-outer-spacing-top-medium")

    # Iterate through the found movie name elements
    for movie_name_tag in movie_name_list:
        movie_name = movie_name_tag.get_text().strip()
        print('movie name:',movie_name)
        
        # Find all elements containing "View All" links on the page
        view_all = movie_page_soup.find_all('a', class_="c-globalHeader_viewMore g-color-gray50 g-text-xxsmall u-text-uppercase")

         # Iterate through the found "View All" links
        for view_all_link_tag in view_all:
            view_all_link = 'https://www.metacritic.com' + view_all_link_tag['href']

         # Send an HTTP GET request to the "View All" page
        view_all_page = requests.get(view_all_link, headers=headers)
        view_all_soup = BeautifulSoup(view_all_page.content, "html.parser")
        
        # Find all elements containing credit tables on the "View All" page
        credit_tables_list = view_all_soup.find_all('div', class_="c-productCredits g-outer-spacing-bottom-xlarge")

        # Initialize a dictionary for directors and cast
        directors_dict = {}  
        casts = []

        # Iterate through the found credit tables
        for credit_table in credit_tables_list:
            # Check if the table contains information about directors
            if "Directed By" in credit_table.get_text().strip():
                # Extract director names
                director_names = [director_tag.get_text().strip() 
                for director_tag in credit_table.find_all('a')]
                #print(director_names)
                
                # Add directors to the directors_dict
                for director_name in director_names:
                    directors_dict[director_name] = {}
                    
            # Check if the table title contains "cast"
            table_title = credit_table.find('h3')
            if table_title and "cast" in table_title.get_text().strip().lower():
                # Extract cast names
                cast_names = [j.get_text().strip() 
                for j in credit_table.find_all('a')]
                 # Add cast names to the casts list
                casts.extend(cast_names)
        
        # Create a sub-dictionary for the current movie, containing directors and casts
        sub_dict = {}
        sub_dict[tuple(directors_dict.keys())] = casts
        dict_1000[movie_name] = sub_dict
 # print dictionary
  print(dict_1000)
        
# Writing to CSV file
import csv
csv_file_path = 'movie_info_final.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Movie Name', 'Directors', 'Cast']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for movie_name, sub_dict in dict_1000.items():
        for directors, cast in sub_dict.items():
            writer.writerow({
                'Movie Name': movie_name,
                'Directors': ', '.join(directors),
                'Cast': ', '.join(cast)
            })

print(f"CSV file created successfully: {csv_file_path}")   


# Prompt the user to choose what they want to check on Metacriticprint("What do you want to check on Metacrtitics? (Please choose ‘movie’, ‘people’, or ‘comparison’)")
print("What do you want to check on Metacrtitics? (Please choose ‘movie’, ‘people’, or ‘comparison’)")
choice = input('Input:')

# checking information about a specific movie
if choice == 'movie':
    print("What movie do you want to check?")
    choice2 = input('input: ')
    
    # Iterate through collected data to find information about the specified movie
    for movie_name, director_dict in dict_1000.items():
        for director_name_tuple, cast in director_dict.items():
            director_name = director_name_tuple[0]
            
            # Check if the current movie matches the specified movie name
            if movie_name.lower() == choice2.lower():
                print('Output :\n')
                print(f'The director of the movie {choice2} is {director_name}')
                print(f'The cast of the movie {choice2} :', ', '.join(cast))
                
#checking information about a specific person (likely a director)                
if choice == 'people':
    choice2 = input('Who do you want to check? ')
    movie_list = []
    cast_list = []
    director_cast_count = {}

    # Iterate through collected data to find movies directed by the specified person
    for movie_name, director_dict in dict_1000.items():
        for director_name_tuple, cast in director_dict.items():
            director_name = director_name_tuple[0]
            
            # Check if the specified person is part of the director's name
            if choice2.lower() in director_name.lower():
                movie_list.append(movie_name)
                cast_list.extend(cast)
                for cast_member in cast:
                    director_cast_count[cast_member] = director_cast_count.get(cast_member, 0) + 1

    print('Output:')
    print(f'{choice2} has directed :', ', '.join(movie_list))
    print('He has work together with these people:', ', '.join(f"{member} ({count})" for member, count in director_cast_count.items()))

#comparing two directors 
import math

if choice == 'comparison':
    print('Who do you want to compare?')
    choice1 = input('Input 1: ')
    choice2 = input('Input 2: ')
    
    # Lists and dictionaries to store information about each individual's directed movies and collaborations
    movie_list1 = []
    cast_list1 = []
    director_cast_count1 = {}  
    
    movie_list2 = []
    cast_list2 = []
    director_cast_count2 = {}  
    
    # Iterate through collected data to find movies directed by each specified individual
    for movie_name, director_dict in dict_1000.items():
        for director_name_tuple, cast in director_dict.items():
            director_name = director_name_tuple[0]

            # Check if the first specified individual is part of the director's name
            if choice1.lower() in director_name.lower():
                movie_list1.append(movie_name)
                cast_list1.extend(cast)
                for cast_member in cast:
                    director_cast_count1[cast_member] = director_cast_count1.get(cast_member, 0) + 1
                

            # Check if the second specified individual is part of the director's name
            if choice2.lower() in director_name.lower():
                movie_list2.append(movie_name)
                cast_list2.extend(cast)
                for cast_member in cast:
                    director_cast_count2[cast_member] = director_cast_count2.get(cast_member, 0) + 1

    print("Output:")
    print(f'{choice1} has directed : {", ".join(movie_list1)}')
    print(f'He has worked together with these people : {", ".join(f"{member} ({count})" for member, count in director_cast_count1.items())}')
    
    print(f'\n {choice2} has directed: {", ".join(movie_list2)}')
    print(f'He has worked together with these people: {", ".join(f"{member} ({count})" for member, count in director_cast_count2.items())}')

    # Calculate Cosine Similarity
    common_casts = set(director_cast_count1.keys()).intersection(director_cast_count2.keys())

    dot_product = sum(director_cast_count1[cast] * director_cast_count2[cast] for cast in common_casts)
    magnitude1 = math.sqrt(sum(count**2 for count in director_cast_count1.values()))
    magnitude2 = math.sqrt(sum(count**2 for count in director_cast_count2.values()))

    cosine_similarity = dot_product / (magnitude1 * magnitude2)

    print('\n')
    print(f'Based on that, they have a cosine similarity score of {cosine_similarity}')
   # print(f'Common cast members: {", ".join(common_casts)}')








































