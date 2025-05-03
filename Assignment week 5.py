# Author: Areesha Tariq
# Date: 11/25/2023
# Purpose: to display/change/add movies and their ratings

import sys
def menu():              # display menu
    print("D to display \nA to append \nR to remove \nQ to quit \n")
    

def main():                
    titles = []      # list to store titles
    ratings = []     # list to store ratings

    menu()        # calls menu function
    
    file = open("movies.txt")               # opens text file
    name = file.readline().rstrip('\n')     
    while name != '':                       # loop to look for end of text file
        rating = int(file.readline())       
        titles.append(name)         # stores titles in the titles list
        ratings.append(rating)      #stores ratings in the ratings list
        name = file.readline().rstrip('\n')

    choice = input("Enter your choice: ")   # asks for user choice

    while choice != "Q":        # sentinal loop
        
        # choice A (appends)
        if choice == "A":       
            title = input("Enter title to add: ")
            
            if title not in titles:
                rating = int(input("Enter rating: "))
                
                if rating <1 or rating >5:
                    print("Invalid rating")
                else:
                    titles.append(title)
                    ratings.append(rating)  
            else:
                print("This title already exists")
                
        # choice R
        elif choice == "R":                 
            title = input("Enter title to remove: ")

            if title not in titles:
                print("This title does not exist")
            else:
                position = titles.index(title)
                titles.remove(title)
                rating_to_remove = ratings[position]
                ratings.remove(rating_to_remove)

        # choice D
        elif choice == "D":
            print(f'{"Title:":<25s} {"Rating:":<25s}')
            for index in range (len(titles)):
                print(f'{titles[index]:<25s} {ratings[index]}')
                movie_count = len(titles)
            print(f'There are {movie_count} movies available')
            average = sum(ratings)/len(ratings)
            print(f'The average rating is {average:.2f} ')

        # choice Q
        elif choice == "Q":
            sys.exit()
        print()
        
        choice = input("Enter your choice: ")
        

        
main()    # calls main function




