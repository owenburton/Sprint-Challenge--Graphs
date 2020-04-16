#### PLAN
# start exploring (dfs)
# keep track of your path
# once you get to a room w/ no other ways to go or with no more unexplored routes
# retrace your steps to the last room w unexplored routes
# add those retrace steps to your path
# start exploring again

def next_ways_and_rooms(visited, room):
    d_r_tups = tuple((d, room.get_room_in_direction(d)) for d in room.get_exits() \
                        if room.get_room_in_direction(d) not in visited)
    return d_r_tups


def opp_way(direction_string):
    opposite = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
    return opposite[direction_string]


def answer(a_world, a_player, num_rooms):
    start = a_player.current_room
    explored = set()
    s = [[('start', start)]]
    route = []

    while len(s)>0:
        path = s.pop()
        room = path[-1][1]
        # print(path)

        # if the current room has been explored, then do nothing and loop again
        if room not in explored:
            ways_to_go = next_ways_and_rooms(explored, room)
            # print(explored)
            # print(ways_to_go)

            # record your new directions if there's nowhere to go
            if not ways_to_go:
                # if you have started recording the map
                if route:
                    last_checkpoint = s.pop()
                    s.append(last_checkpoint)
                    num_new_steps = len(path) - (len(last_checkpoint) - 1) # minus 1 bc last_checkpoint includes next room to be explored
                    new_path = path[-(num_new_steps):]
                    new_steps = [d for d in new_path]
                    retraced_steps = [opp_way(d) for d in new_steps]
                    route = route + new_steps + retraced_steps
                # if you haven't started the map yet
                else:
                    route = [tup[0] for tup in path]
            
            # if there are ways to go, then add those paths to the stack
            else:
                for tup in ways_to_go:
                    explored.add(tup[1])
                    s.append(path + [tup])

    return route