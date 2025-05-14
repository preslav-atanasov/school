towers = [[], [], []]

STACK_SIZE = 7
towers[0] = list(range(STACK_SIZE, 0, -1))


# display towers in a pretty way
def display_towers(towers, max_size):
    for i in range(max_size, -1, -1):  # for each row
        for t in towers:  # for each tower
            if i < len(t):
                space_count = max_size - t[i]
                print((' ' * space_count) + ('=' * (t[i] * 2 + 1)) + (' ' * space_count), end=' ')
                print(' ', end=' ')
            else:
                print((' ' * max_size) + '|' + (' ' * max_size), end=' ')
                print(' ', end=' ')
        print("")


# move disk from one tower to another
def move_disk(towers, from_tower, to_tower):
    if len(towers[from_tower]) == 0:
        print("Invalid move: empty tower")
        return
    if len(towers[to_tower]) > 0 and towers[from_tower][-1] > towers[to_tower][-1]:
        print("Invalid move: cannot place larger disk on smaller disk")
        return
    disk = towers[from_tower].pop()
    towers[to_tower].append(disk)


# using recursion and yield
def solve(n, from_tower, to_tower, aux_tower):
    if n == 1:
        yield from_tower, to_tower
    else:
        yield from solve(n - 1, from_tower, aux_tower, to_tower)
        yield from solve(1, from_tower, to_tower, aux_tower)
        yield from solve(n - 1, aux_tower, to_tower, from_tower)


# main loop
auto = None
while True:
    display_towers(towers, STACK_SIZE)

    # auto mode
    if auto:
        try:
            move = next(auto)
            print("Auto move: ", move)
            move_disk(towers, move[0], move[1])
        except StopIteration:
            print("Done!")
            auto = None
            continue

        if input("Enter to continue (or 's' to stop auto): ") == 's':
            auto = None
        continue

    # manual mode
    move = input("Enter your move (from, to) (or 'a' for auto): ").strip()
    if move == '':
        continue
    if move == 'q':
        break
    if move == 'a':
        auto = solve(STACK_SIZE, 0, 2, 1)
        continue
    move = move.split(',')
    move = [int(m.strip()) for m in move]
    move_disk(towers, move[0] - 1, move[1] - 1)