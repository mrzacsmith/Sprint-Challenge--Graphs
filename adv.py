from room import Room
from player import Player
from world import World

# from link-list import Graph, Queue, Stack
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# -----------------------------------
# visited_rooms = {}
# path = []
# # reverse_direction allows us to go backwards
# reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# visited_rooms[player.current_room.id] = player.current_room.get_exits
# -----------------------------------

# add simple stack


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


paths = Stack()
visited_rooms = set()


def shortest_path(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


while len(visited_rooms) < len(world.rooms):
    exits = player.current_room.get_exits()
    path = []

    # check to see if the exit already is in exits
    for exit in exits:
        if exit is not None and player.current_room.get_room_in_direction(exit) not in visited_rooms:
            path.append(exit)
    # add current_room to set
    visited_rooms.add(player.current_room)

    # if path > 0, generate random and give that step
    # add path(step) to paths
    # use player.travel path(step)
    # run traversal path and append path(step)
    if len(path) > 0:
        step = random.randint(0, len(path) - 1)
        paths.push(path[step])
        player.travel(path[step])
        traversal_path.append(path[step])
    # otherwise, assume the end and pop the path(step)
    # use shortest_path with travel
    # run traversal path and append the shortest step
    else:
        end = paths.pop()
        player.travel(shortest_path(end))
        traversal_path.append(shortest_path(end))

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
# TEST
# Passed Ok 987
# Passed Ok 997
# Passed Ok 998
# Passed Ok 998 all 500 rooms but requires Crtl+c to end and return to terminal
