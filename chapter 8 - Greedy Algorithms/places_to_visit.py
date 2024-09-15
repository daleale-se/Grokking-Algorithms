# Locally Optimal Choice: At each step, the algorithm makes the locally optimal choice by selecting the place with the
# best points-to-time ratio.
# Irrevocable Choices: Once a place is selected (i.e., added to preferred_places), it is removed from the places list
# and won't be reconsidered in the next steps.
# No Backtracking: The algorithm never revisits or re-evaluates previous decisions. It only looks at the remaining
# places and selects the current best option based on the points-to-time ratio.

def places_to_visit():

    places = [
        {
            "name": "a",
            "points": 5,
            "time": 1
        },
        {
            "name": "b",
            "points": 4,
            "time": .5
        },
        {
            "name": "c",
            "points": 4,
            "time": 2
        },
        {
            "name": "d",
            "points": 3,
            "time": 1
        },
        {
            "name": "e",
            "points": 5,
            "time": .25
        },
        {
            "name": "f",
            "points": 3,
            "time": .25
        },
        {
            "name": "g",
            "points": 5,
            "time": 1.5
        },
        {
            "name": "h",
            "points": 4,
            "time": .5
        }
    ]
    preferred_places = []
    timeleft = 4

    # while timeleft > 0:
    #     best_place = max(places, key=lambda place: place["points"] / place["time"])
    #     timeleft -= best_place["time"]
    #     if timeleft >= 0:
    #         places = [x for x in places if x != best_place]
    #         preferred_places.append(best_place)
    #
    # print(preferred_places)

    while timeleft > 0 and places:
        best_place = max(places, key=lambda x: x["points"] / x["time"])
        if best_place["time"] <= timeleft:
            preferred_places.append(best_place)
            timeleft -= best_place["time"]
        places = [place for place in places if place != best_place]

    print(preferred_places)