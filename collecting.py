import turtle
import heapq
import sys

#목표지점 3개를 이곳에서 설정하시오
table_requests = [[0, 6], [7, 6], [2, 8]]

    # mappings = {
    #     "table1": [0, 2],   "table2": [0, 4],   "table3": [0, 6],   "table4": [0, 8],   "table5": [0, 10],
    #     "table6": [2, 4],   "table7": [2, 6],   "table8": [2, 8],
    #     "table9": [5, 4],   "table10": [5, 6],  "table11": [5, 8],
    #     "table12": [7, 4],  "table13": [7, 6],  "table14": [7, 8],  "table15": [7, 10]
    # }



# 가중치가 있는 이동 경로 계산을 위한 함수 (다익스트라 알고리즘)
def dijkstra2(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    distances = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_position = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_position]:
            continue
        
        neighbors = [
            (current_position[0] + 1, current_position[1]),
            (current_position[0] - 1, current_position[1]),
            (current_position[0], current_position[1] + 1),
            (current_position[0], current_position[1] - 1)
        ]
        
        for neighbor in neighbors:
            r, c = neighbor
            if 0 <= r < rows and 0 <= c < cols and matrix[r][c] != 5:  # 유효한 좌표 및 장애물 체크
                weight = matrix[r][c]
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 모든 테이블 간의 최단 경로 계산
def compute_all_pairs_shortest_path(matrix, points):
    shortest_paths = {}
    for point in points:
        shortest_paths[point] = dijkstra2(matrix, point)
    return shortest_paths

# TSP를 그리디 방식으로 해결 (각 단계에서 가장 가까운 테이블 선택)
def greedy_tsp(matrix, start, table_requests):
    start = tuple(start)
    table_requests = [tuple(req) for req in table_requests]
    
    points = [start] + table_requests
    shortest_paths = compute_all_pairs_shortest_path(matrix, points)
    
    visited = [start]
    current_position = start
    total_distance = 0
    
    while table_requests:
        next_point = min(table_requests, key=lambda x: shortest_paths[current_position][x])
        visited.append(next_point)
        total_distance += shortest_paths[current_position][next_point]
        current_position = next_point
        table_requests.remove(next_point)
    
    return visited, total_distance

# 터틀 그래픽을 사용하여 그리드 그리기
def draw_grid2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    turtle.speed(0)
    turtle.penup()
    
    for r in range(rows):
        for c in range(cols):
            turtle.goto(c * 20 - 100, -r * 20 + 100)
            turtle.pendown()
            
            if matrix[r][c] == 5:  # 장애물
                turtle.fillcolor("black")
            elif matrix[r][c] == 8:  # 테이블
                turtle.fillcolor("brown")
            elif matrix[r][c] == 9:  # 테이블 (white)
                turtle.fillcolor("white")
            elif matrix[r][c] == 10:  # 충전소
                turtle.fillcolor("red")
            else:
                turtle.fillcolor("white")
            
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

# 기계의 경로 시각화
def draw_path(path):
    turtle.speed(1)
    turtle.color("blue")
    turtle.penup()
    for pos in path:
        turtle.goto(pos[1] * 20 - 90, -pos[0] * 20 + 90)
        turtle.pendown()
        turtle.dot(10)
        turtle.penup()
        
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

    start = [2, 2]
    
    visited, total_distance = greedy_tsp(matrix, start, table_requests)

    turtle.setup(500, 500)
    turtle.setworldcoordinates(-120, -120, 120, 120)
    draw_grid2(matrix)
    draw_path(visited)

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

    start = [2, 2]
    # table_requests = [[0, 2], [7, 8], [2, 4]]
        
    # 함수 호출
    visited, total_distance = greedy_tsp(matrix, start, table_requests)

    
    print( total_distance-26)

    return total_distance

if __name__ == "__main__":
    main()
