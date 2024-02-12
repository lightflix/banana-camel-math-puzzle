import math

def trip(stop_at_km, initial_banana_pool):

    camel_consumption_rate_per_km = 1
    camel_capacity = 1000

    i = 0
    bananas_moved = 0
    bananas_at_stop = 0

    # print("\nStop at KM: ", stop_at_km)
    while initial_banana_pool > 0:

        # print("\nIteration: -------------------------> ", i+1)
        # print("Initial bananas pool: ", initial_banana_pool)

        if initial_banana_pool > camel_capacity:
            bananas_consumed = stop_at_km * camel_consumption_rate_per_km * 2

            if bananas_consumed > camel_capacity:
                print("Error: Camel not able to return")
                return False

            bananas_moved = bananas_moved + camel_capacity - bananas_consumed
            initial_banana_pool = initial_banana_pool - bananas_moved - bananas_consumed
        else:
            bananas_consumed = stop_at_km * camel_consumption_rate_per_km
            bananas_moved = bananas_moved + initial_banana_pool - bananas_consumed
            initial_banana_pool = initial_banana_pool - initial_banana_pool

        bananas_at_stop = bananas_at_stop + bananas_moved
        bananas_moved = 0
        
        if initial_banana_pool == 0:
            # print("Initial bananas pool remaining: ", initial_banana_pool)
            # print("Bananas at stop: ", bananas_at_stop)
            # print("\n")

            return bananas_at_stop

        i+=1


def journey(stop_at_km, total_distance, bananas_at_stop):
    camel_at_point = 0
    number_of_onward_journeys = math.floor(total_distance / stop_at_km)

    remainder_km = total_distance % stop_at_km

    if remainder_km > 0:
        number_of_onward_journeys += 1

    # print("Number of onward journeys: ", number_of_onward_journeys)

    while camel_at_point != total_distance:

        # print("Camel at point: ", camel_at_point)

        for i in range(0, number_of_onward_journeys):

            if total_distance - camel_at_point < stop_at_km:
                bananas_at_stop = trip(remainder_km, bananas_at_stop)
                camel_at_point += remainder_km
            else:
                bananas_at_stop = trip(stop_at_km, bananas_at_stop)
                camel_at_point += stop_at_km

            if bananas_at_stop < total_distance - camel_at_point:
                return 0
            
            print("Camel at point: ", camel_at_point, "bananas at stop: ", bananas_at_stop)

            

            # print("Main loop >> Camel is at distance: ", camel_at_point)
        return bananas_at_stop
    

if __name__ == "__main__":

    total_bananas = 3000
    total_distance = 1000
    stop_at_km = 1

    # for i in range(1, 501):

    #     bananas_left = journey(i, total_distance, total_bananas)
    #     print(i, ",", bananas_left)

    print(journey(stop_at_km, total_distance, total_bananas))


