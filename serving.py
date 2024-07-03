#다익스트라 최단거리 알고리즘
#반환 값: Total distance: n
#반환 값: Turtle Graphic shape 

import turtle
import heapq
#import dijkstra


#목표지점을 이곳에서 수정하시오
end = (2, 8)


    # mappings = {
    #     "table1": [0, 2],   "table2": [0, 4],   "table3": [0, 6],   "table4": [0, 8],   "table5": [0, 10],
    #     "table6": [2, 4],   "table7": [2, 6],   "table8": [2, 8],
    #     "table9": [5, 4],   "table10": [5, 6],  "table11": [5, 8],
    #     "table12": [7, 4],  "table13": [7, 6],  "table14": [7, 8],  "table15": [7, 10]
    # }




##다익스트라 알고리즘 파일 병합
def dijkstra1(graph, start):
    # Create a dictionary to store distances from the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Create a priority queue and push the start node with distance 0
    priority_queue = [(0, start)]
    # Create a dictionary to store the shortest path tree
    shortest_path_tree = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Nodes can get added to the priority queue multiple times. We only
        # process a node the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, shortest_path_tree

##다익스트라 알고리즘 파일 병합

def create_graph_from_matrix(matrix):
    graph = {}
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            graph[(r, c)] = {}
            if r > 0:
                graph[(r, c)][(r - 1, c)] = matrix[r - 1][c]  # Up
            if r < rows - 1:
                graph[(r, c)][(r + 1, c)] = matrix[r + 1][c]  # Down
            if c > 0:
                graph[(r, c)][(r, c - 1)] = matrix[r][c - 1]  # Left
            if c < cols - 1:
                graph[(r, c)][(r, c + 1)] = matrix[r][c + 1]  # Right
    return graph

def find_shortest_path(matrix, start, end):
    graph = create_graph_from_matrix(matrix)
    distances, shortest_path_tree = dijkstra1(graph, start)
    path = []
    step = end
    
    while step is not None:
        path.append(step)
        step = shortest_path_tree[step]
    path.reverse()
    return path, distances[end]

def draw_grid1(matrix):
    rows, cols = len(matrix), len(matrix[0])
    turtle.speed(0)
    turtle.penup()
    for r in range(rows):
        for c in range(cols):
            turtle.goto(c * 20 - 200, -r * 20 + 200)
            turtle.pendown()
            if matrix[r][c] == 5:
                turtle.fillcolor("black")
            elif matrix[r][c] == 10:
                turtle.fillcolor("red")
            elif matrix[r][c] == 8:
                turtle.fillcolor("brown")
            else:
                turtle.fillcolor("white")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

def draw_shortest_path(matrix, path):
    turtle.speed(10)
    turtle.penup()
    turtle.color("red")
    for position in path:
        row, col = position
        turtle.goto(col * 20 - 190, -row * 20 + 190)
        turtle.pendown()
        turtle.dot(10)
    turtle.hideturtle()

# 충전소=(10)
# 테이블=(8)
# 테이블 사이=(9)
# 장애물=(5)

def show():
    
    matrix = [
    [1, 1, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 10, 1, 8, 9, 8, 9, 8, 5, 1],
    [5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
    [5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
    [5, 5, 5, 1, 8, 9, 8, 9, 8, 5, 1],
    [5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 5, 9, 8, 9, 8, 9, 8, 9, 8]
]   
    start = (2, 2) # 충전소(시작점)  
    #end
    path, total_distance = find_shortest_path(matrix, start, end)
    
    turtle.setup(500, 500)
    turtle.setworldcoordinates(-200, -200, 200, 200)
    draw_grid1(matrix)
    draw_shortest_path(matrix, path)
    turtle.done()
    

def main():
    matrix = [
    [1, 1, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 10, 1, 8, 9, 8, 9, 8, 5, 1],
    [5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
    [5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 1],
    [5, 5, 5, 1, 8, 9, 8, 9, 8, 5, 1],
    [5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 5, 9, 8, 9, 8, 9, 8, 9, 8]
]
    
# Serving_System
# find_shortest_path(matrix, start, end)
# draw_grid1(matrix)
# draw_shortest_path(matrix, path)
# return total_distance
    
    start = (2, 2) # 충전소(시작점)  
    

    
    path, total_distance = find_shortest_path(matrix, start, end)
    print(total_distance-8)
    #total_distanc-8 = table의 가중치가 8이므로 이를 제외해야 함

    
    return total_distance

if __name__ == "__main__":
    main()
