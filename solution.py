#### PLAN
# start exploring (dfs)
# keep track of your path
# once you get to a room w/ no other ways to go or with no more unexplored routes
# retrace your steps to the last room w unexplored routes
# add those retrace steps to your path
# start exploring again

# def get_rooms(visited, room):
#     lis = {room.get_room_in_direction(d):d for d in room.get_exits()}
#     return lis


# def opp_way(direction_string):
#     opposite = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
#     return opposite[direction_string]


# def answer(a_world, a_player, num_rooms):
#     start = a_player.current_room
#     explored = set()
#     s = [[('start', start)]]
#     route = []

#     while len(s)>0:
#         path = s.pop()
#         room = path[-1][1]
#         print(s)
#         print(room)
#         if room not in explored: 
#             explored.add(room)

#             ways_to_go = next_ways_and_rooms(explored, room)

#             # record your new directions if there's nowhere to go
#             if not ways_to_go:
#                 # check if there's no more rooms to explore
#                 if len(s)==0:
#                     break
#                 # if you have started recording the map
#                 if len(route)>0:
#                     print('route greater than zero')
#                     last_checkpoint = s.pop()
#                     s.append(last_checkpoint)
#                     num_new_steps = len(path) - (len(last_checkpoint) - 1) # minus 1 bc last_checkpoint includes next room to be explored
#                     new_path = path[-(num_new_steps):]
#                     new_steps = [d for d in new_path]
#                     retraced_steps = [opp_way(d) for d in new_steps]
#                     route = route + new_steps + retraced_steps
#                 # if you haven't started the map yet
#                 else:
#                     print('filling empty route')
#                     route = [tup[0] for tup in path]
            
#             # if there are ways to go, then add those paths to the stack
#             else:
#                 for tup in ways_to_go:
#                     # print(tup)
#                     # print(route)
#                     explored.add(tup[1])
#                     s.append(path + [tup])
#                     print(f'after: {s}')
#     print(route[1:])
#     return route[1:] # don't include 'start'
from collections import deque

def get_rooms(room):
    lis = {room.get_room_in_direction(d):d for d in room.get_exits()}
    return lis

def bfs(start, dest):
    q = deque([[('start', start)]])
    visited = set()
    route = []
    while len(q)>0:
        path = q.pop()
        v = path[-1][1]
        if v not in visited:
            visited.add(v)
            if v==dest:
                return path
            new_rooms = [(d, v.get_room_in_direction(d)) for d in v.get_exits()]
            for tup in new_rooms:
                q.appendleft(path + [tup])

def dft(a_player):
    stack = deque([[('start', a_player.current_room)]])
    visited = set()
    route = [('start', a_player.current_room)]
    while len(stack)>0:
        path = stack.pop()
        v = path[-1][1]
        if v not in visited:
            # check if current room is connected to prev room in route
            if v in get_rooms(route[-1][1]):
                route.append(path[-1])
                visited.add(v)
            else:
                shortest_path = bfs(route[-1][1], v)
                for tup in shortest_path[1:]: # don't include the room where you start
                    route.append(tup)
                    visited.add(tup[1])

            new_rooms = [(d, v.get_room_in_direction(d)) for d in v.get_exits()]
            for tup in new_rooms:
                stack.append(path + [tup])

    directions = [tup[0] for tup in route[1:]]
    return directions