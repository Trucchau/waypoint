                        #Waypoint 1:
def hello(name):

    name = name.strip()
    name = 'Hello ' + name + '!'
    return name

name = input("What is your name: ")
print(hello(name))

                        #Waypoint 2:
import math
def calculate_hypotenuse(a, b):
   c =  math.sqrt(a**2 + b**2)
   return c
a = int(input("Enter a: "))
b = float(input("Enter b: "))
print(calculate_hypotenuse(a, b))

                        #Waypoint 3:
def are_all_conditions_true(conditions):
    conditions = [True, True]
    if not conditions == []:
        for idx, value in enumerate(conditions):
            if value == False:
                return False
        return True
    else:
        print("None")

print(are_all_conditions_true([True, True]))


                        #Waypoint 4:
def is_a_condition_true(conditions):
    conditions = [False, False, True]
    if not conditions == []:
        for idx, value in enumerate(conditions):
            if value == True:
                return True
        else:
            print("None")
print(is_a_condition_true([False, False, True]))


                        #Waypoint 5:
def filter_integers_greater_than(l, n):
    l = [0, 3, 5, -2, 9, 8]
    result = []
    for i in l:
        if i > n:
            result.append(i)
        i += 1
    return result
n = int(input("Enter n: "))
print(filter_integers_greater_than([0, 3, 5, -2, 9, 8], n))



                        #Waypoint 6:
def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    result = []
    for i in hotel_daily_rates:
        if i[1] <= maximum_daily_rate:
            result.append(i[0])
    result.sort()
    return result

hotel_daily_rates = [('Majestic Saigon Hotel', 93),
                     ('Hotel Grand Saigon', 80),
                     ('Sofitel Saigon Plaza', 123),
                     ('Hotel Continental', 62),
                     ('Caravelle Hotel', 180),
                     ('Sheraton Saigon Hotel', 216),
                     ('Park Hyatt Saigon', 209)]
maximum_daily_rate = int(input("Nhap gia:"))
print(find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate))


                    #Waypoint 7:
import math
def calculate_euclidean_distance_between_2_points(p1, p2):

    result = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    return result

p1= [0,0]
p2= [3,4]
print(calculate_euclidean_distance_between_2_points(p1, p2))
