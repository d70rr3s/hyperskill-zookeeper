duration = int(input())
food_cost = int(input())
one_way_flight_cost = int(input())
night_cost = int(input())

total_cost = one_way_flight_cost * 2
total_cost += (food_cost * duration)
total_cost += ((duration - 1) * night_cost)

print(total_cost)
