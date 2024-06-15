import random

def generate_path(maze, N, M):
    path = {}
    for i in range(N):
        for j in range(M):
            path[(i, j)] = 0
    i, j = 0, 0
    path[(i, j)] = 2

    while i < N - 1 or j < M - 1:
        if i == N - 1:
            j += 1
        elif j == M - 1:
            i += 1
        else:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
        path[(i, j)] = 2

    return path

def add_obstacles(maze, path, min_obstacles, N, M):
    count = 0
    while count < min_obstacles:
        i, j = random.randint(0, N-1), random.randint(0, M-1)
        if path[(i, j)] == 0 and maze[i][j] == 0:
            maze[i][j] = 1
            count += 1

def set_obstacle(maze, path, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to set an obstacle, e.g. i,j: ").split())
        if i < 0 or i >= N or j < 0 or j >= M:
            raise IndexError
        if path[(i, j)] == 2:
            print("Obstacle cannot be placed on the path.")
        else:
            maze[i][j] = 1
    except ValueError:
        print("ValueError in set_obstacle function. Need to be coordinates.")
    except IndexError:
        print("KeyError in set_obstacle function. 'Invalid coordinates. Please input coordinates within the range.'")

def remove_obstacle(maze, path, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to remove an obstacle, e.g. i,j: ").split())
        if i < 0 or i >= N or j < 0 or j >= M:
            raise IndexError
        if maze[i][j] == 1:
            maze[i][j] = 0
        else:
            print("Obstacle does not exist at this location.")
    except ValueError:
        print("ValueError in remove_obstacle function. Need to be coordinates.")
    except IndexError:
        print("KeyError in remove_obstacle function. 'Invalid coordinates. Please input coordinates within the range.'")

def print_maze(maze, path, N, M):
    for i in range(N):
        for j in range(M):
            if path[(i, j)] == 2:
                print('O', end=' ')
            elif maze[i][j] == 1:
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print()

def read_maze(file_name):
    try:
        with open(file_name, 'r') as file:
            maze = []
            for line in file:
                if '+' not in line:  # Skip lines with borders
                    maze.append([1 if char == 'X' else 0 for char in line if char in (' ', 'X')])
            return maze
    except IOError:
        print("IOError occurred in main function. File not found. Please enter a valid file.")
        return None

def main():
    while True:
        file_name = input("Enter the maze file name (grid77.txt or grid99.txt): ")
        maze = read_maze(file_name)
        if maze:
            break

    N, M = len(maze), len(maze[0])
    path = generate_path(maze, N, M)

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles (0-55): "))
            if min_obstacles < 0 or min_obstacles > N * M:
                raise ValueError
            break
        except ValueError:
            print("ValueError occurred in main function. Invalid number of obstacles.")

    add_obstacles(maze, path, min_obstacles, N, M)
    print_maze(maze, path, N, M)

    while True:
        print("\nOptions:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        choice = input("Enter your option: ")

        if choice == '1':
            set_obstacle(maze, path, N, M)
            print_maze(maze, path, N, M)
        elif choice == '2':
            remove_obstacle(maze, path, N, M)
            print_maze(maze, path, N, M)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
