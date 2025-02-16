from collections import deque
import heapq

def stable_job_matching(companies_prefs, candidates_prefs):
    """
    Implements the Stable Job Matching algorithm.
    This function takes in the preferences of companies and candidates and returns a stable matching
    where no company-candidate pair would prefer each other over their current matches.
    Parameters:
    companies_prefs (dict): A dictionary where keys are company names and values are lists of candidate names in order of preference.
    candidates_prefs (dict): A dictionary where keys are candidate names and values are lists of company names in order of preference.
    Returns:
    dict: A dictionary where keys are company names and values are the names of the candidates they have hired.

    Pseudo-code:
    1. Initialize a list of free companies.
    2. Initialize an empty dictionary to store the final company-candidate pairs.
    3. Initialize a dictionary to keep track of each candidate's current employer (initially None).
    4. While there are free companies:
        a. Pick the first free company.
        b. Get the company's preference list.
        c. For each candidate in the company's preference list:
            i. Check the candidate's current employer.
            ii. If the candidate is free:
                - Hire the candidate.
                - Update the candidate's current employer.
                - Break the loop.
            iii. If the candidate prefers the new company over the current employer:
                - Make the current employer free again.
                - Hire the candidate.
                - Update the candidate's current employer.
                - Break the loop.
    5. Return the final company-candidate pairs.
    """
    free_companies = list(companies_prefs.keys())  # Companies start as "unmatched"
    hires = {}  # Stores final company-candidate pairs
    candidate_choices = {c: None for c in candidates_prefs}  # Candidates initially unassigned

    while free_companies:
        company = free_companies.pop(0)  # Pick a free company
        company_prefs = companies_prefs[company]

        for candidate in company_prefs:
            current_employer = candidate_choices[candidate]  # Check candidate's current employer

            if current_employer is None:
                # Candidate is free, hire them
                hires[company] = candidate
                candidate_choices[candidate] = company
                break
            else:
                # Candidate prefers new company over the current one?
                candidate_prefs = candidates_prefs[candidate]
                if candidate_prefs.index(company) < candidate_prefs.index(current_employer):
                    # Candidate prefers new company → Switch jobs
                    free_companies.append(current_employer)  # Old employer is free again
                    hires.pop(current_employer)
                    hires[company] = candidate
                    candidate_choices[candidate] = company
                    break

    return hires

# Example Data
companies_prefs = {
    "Google": ["Alice", "Bob", "Charlie"],
    "Amazon": ["Charlie", "Alice", "Bob"],
    "Microsoft": ["Alice", "Charlie", "Bob"]
}

candidates_prefs = {
    "Alice": ["Google", "Amazon", "Microsoft"],
    "Bob": ["Amazon", "Google", "Microsoft"],
    "Charlie": ["Microsoft", "Amazon", "Google"]
}

matches = stable_job_matching(companies_prefs, candidates_prefs)
print("Stable Job Matches:", matches)

def bfs(graph, start):
    visited = []
    queue = [start]
    order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example Usage
start_node = 'A'
bfs_order = bfs(graph, start_node)
print("BFS Order starting from node", start_node, ":", bfs_order)

# Tests
def test_bfs():
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']
    assert bfs(graph, 'B') == ['B', 'A', 'D', 'E', 'C', 'F']
    assert bfs(graph, 'C') == ['C', 'A', 'F', 'B', 'E', 'D']
    assert bfs(graph, 'D') == ['D', 'B', 'A', 'E', 'C', 'F']
    assert bfs(graph, 'E') == ['E', 'B', 'F', 'A', 'D', 'C']
    assert bfs(graph, 'F') == ['F', 'C', 'E', 'A', 'B', 'D']
    print("All tests passed.")

test_bfs()

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    E = []
    for u in graph:
        for v, weight in graph[u].items():
            E.append((u, v, weight))
    
    E.sort(key=lambda x: x[2])  # Sort edges by weight
    
    vertices = list(graph.keys())
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    
    CMG = []
    
    for u, v, weight in E:
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            CMG.append((u, v, weight))
            union(parent, rank, x, y)
            print(f"Added edge: {u} - {v} with weight {weight}")
    
    return sorted(CMG, key=lambda x: (x[2], x[0], x[1]))

# Tests
def test_kruskal():
    # Test case 1: Simple graph
    graph1 = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    result1 = kruskal(graph1)
    expected1 = [('B', 'C', 1), ('A', 'C', 2), ('D', 'E', 2), ('E', 'F', 3), ('A', 'B', 4)]
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed. Expected {expected1}, but got {result1}"
    
    # Test case 2: Disconnected graph
    graph2 = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2},
        'E': {'F': 3},
        'F': {'E': 3}
    }
    result2 = kruskal(graph2)
    expected2 = [('A', 'B', 1), ('C', 'D', 2), ('E', 'F', 3)]
    assert sorted(result2) == sorted(expected2), f"Test case 2 failed. Expected {expected2}, but got {result2}"
    
    # Test case 3: Complete graph
    graph3 = {
        'A': {'B': 1, 'C': 4, 'D': 3},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 6},
        'D': {'A': 3, 'B': 5, 'C': 6}
    }
    result3 = kruskal(graph3)
    expected3 = [('A', 'B', 1), ('B', 'C', 2), ('A', 'D', 3)]
    assert sorted(result3) == sorted(expected3), f"Test case 3 failed. Expected {expected3}, but got {result3}"
    
    print("All tests passed!")

# Run the tests
# test_kruskal()

def prim(graph, start):
    mst = []
    visited = [start]
    edges = []
    for to, weight in graph[start].items():
        edges.append((start, to, weight))
    # edges = [(start, to, weight) for to, weight in graph[start].items()]

    while edges:
        edges.sort(key=lambda x: x[2])  # Sort edges by weight
        frm, to, weight = edges.pop(0)
        if to not in visited:
            visited.append(to)
            mst.append((frm, to, weight))

            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    edges.append((to, to_next, weight))

    return mst

# Tests
def test_prim():
    # Test case 1: Simple graph
    graph1 = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    result1 = prim(graph1, 'A')
    expected1 = [('A', 'C', 2), ('C', 'B', 1), ('D', 'E', 2), ('E', 'F', 3), ('B', 'D', 5)]
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed. Expected {expected1}, but got {result1}"
    
    # Test case 2: Disconnected graph
    graph2 = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2},
        'E': {'F': 3},
        'F': {'E': 3}
    }
    result2 = prim(graph2, 'A')
    expected2 = [('A', 'B', 1)]
    assert sorted(result2) == sorted(expected2), f"Test case 2 failed. Expected {expected2}, but got {result2}"
    
    # Test case 3: Complete graph
    graph3 = {
        'A': {'B': 1, 'C': 4, 'D': 3},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 6},
        'D': {'A': 3, 'B': 5, 'C': 6}
    }
    result3 = prim(graph3, 'A')
    expected3 = [('A', 'B', 1), ('B', 'C', 2), ('A', 'D', 3)]
    assert sorted(result3) == sorted(expected3), f"Test case 3 failed. Expected {expected3}, but got {result3}"
    
    print(graph1)
    print(result1) 
    

# Run the tests
test_prim()