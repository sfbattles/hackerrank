"""
Complete the function compareTriplets in the editor below. 
It must return an array of two integers, 
the first being Alice's score and the second being Bob's.

compareTriplets has the following parameter(s):

a: an array of integers representing Alice's challenge rating
b: an array of integers representing Bob's challenge rating
"""
def compareTriplets(triplet1,triplet2):
    points_array = [0, 0]
    for x,y in zip(triplet1,triplet2):
        if x > y:
            points_array[0] += 1
        elif x < y:
            points_array[1] += 1
    return(points_array)


user1,user2 = [],[]
#map converts the input to an int
#split will get rid of spaces
#list will convert the input to a list
#x.isdigit() make sure its a didgit to include in my list
#mak sure its x <= 100
def input_list_of_numbers():
    user = list(input("Enter a list of 3 integers space-separated -->").split())
    user = list(map(int,[ x for x in user if x.isdigit() and int(x) <= 100 and int(x) >= 0 ]))
    while len(user) != 3:        
        user = list(input(f"Error only found {len(user)} valid numbers Enter only 3 integers separated by a space -->").split())    
        user = list(map(int,[ x for x in user if x.isdigit() and int(x) <= 100 and int(x) >= 0 ]))
    return(user)

user1 = input_list_of_numbers()
user2 = input_list_of_numbers()

result = compareTriplets(user1,user2)
for x in result:
    print(x,end=' ')
print("\n")