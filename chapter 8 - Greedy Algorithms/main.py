
def main():

    # set-covering problem (NP-complete) solved with a approximation algorithm (greedy algorthm)
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            # select subset with most states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        # reduce the set states_needed with the states_covered
        states_needed -= states_covered
        final_stations.add(best_station)

    print(final_stations)

    return


main()
