from collections import deque
from random import shuffle

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
            if new_rooms:
                shuffle(new_rooms)
            for tup in new_rooms:
                stack.append(path + [tup])

    directions = [tup[0] for tup in route[1:]]
    return directions