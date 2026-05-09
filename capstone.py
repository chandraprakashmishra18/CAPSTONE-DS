# Final Capstone:
# Social Network Explorer (SNE)

# Capstone Summary (aligned to uploaded capstone)
# Design and implement a simplified social network explorer:

# • Profiles (Hashing + Arrays/Lists): add user(), get profile(), update profile()
# • Network (Graph Adjacency List): add/remove friendships/followers, get friends
# • Discovery (BFS): shortest path (degrees of separation) between two users
# • Exploration (DFS): friends-of-friends up to depth d
# • Recommendation (Sorting + Hashing - conceptual): rank by common interests; bonus: geo DS choice
# • Interface: simple text-based CLI

# Minimum Demo Checklist (faculty verifies):
# • Add 6–8 users, update 2 profiles, show at least 3 profiles
# • Create 8–12 connections; remove at least 1 connection
# • Run 2 BFS shortest path queries (print path)
# • Run DFS with depth=2 and depth=3 (print discovered users)
# • Print suggestion list sorted by common interests (even if partial implementation)
# Submission
# • Clean modular structure (profiles, graph, bfs dfs, sorting, main CLI)
# • Test cases + sample run outputs
# • Short report: complexity notes + design decisions

# Aim:
# To design and implement a social network system using graph traversal, hashing, and sorting techniques.

# Data Structures Used:
# Hash Table → Profiles
# Graph (Adjacency List) → Connections
# Queue → BFS
# Recursion → DFS
# Sorting → Recommendations

# Complexity:
# BFS → O(V + E)
# DFS → O(V + E)
# Recommendation → O(V²) (basic version)

# Solution:

from collections import deque, defaultdict

class SocialNetworkExplorer:
    def __init__(self):
        self.profiles = {}  # Hashing
        self.graph = defaultdict(set)  # Adjacency List

    # ---------------- PROFILE ----------------
    def add_user(self, username, interests):
        self.profiles[username] = {
            "interests": set(interests)
        }

    def get_profile(self, username):
        return self.profiles.get(username, "User not found")

    def update_profile(self, username, interests):
        if username in self.profiles:
            self.profiles[username]["interests"] = set(interests)

    # ---------------- GRAPH ----------------
    def add_connection(self, u1, u2):
        self.graph[u1].add(u2)
        self.graph[u2].add(u1)

    def remove_connection(self, u1, u2):
        self.graph[u1].discard(u2)
        self.graph[u2].discard(u1)

    def get_friends(self, user):
        return list(self.graph[user])

    # ---------------- BFS ----------------
    def shortest_path(self, start, end):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path

            visited.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return "No connection found"

    # ---------------- DFS ----------------
    def dfs_depth(self, start, depth):
        visited = set()
        result = []

        def dfs(node, d):
            if d < 0 or node in visited:
                return
            visited.add(node)
            result.append(node)

            for neighbor in self.graph[node]:
                dfs(neighbor, d - 1)

        dfs(start, depth)
        return result

    # ---------------- RECOMMENDATION ----------------
    def recommend(self, user):
        recommendations = {}

        for other in self.profiles:
            if other != user and other not in self.graph[user]:
                mutual = len(self.graph[user].intersection(self.graph[other]))
                if mutual > 0:
                    recommendations[other] = mutual

        # sort by mutual friends
        return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)


# ---------------- DEMO ----------------
if __name__ == "__main__":
    sne = SocialNetworkExplorer()

    # Add Users
    sne.add_user("A", ["music", "sports"])
    sne.add_user("B", ["music", "coding"])
    sne.add_user("C", ["sports", "travel"])
    sne.add_user("D", ["coding", "gaming"])
    sne.add_user("E", ["travel", "food"])
    sne.add_user("F", ["music", "gaming"])

    # Connections
    sne.add_connection("A", "B")
    sne.add_connection("A", "C")
    sne.add_connection("B", "D")
    sne.add_connection("C", "E")
    sne.add_connection("D", "F")
    sne.add_connection("B", "F")

    print("Profiles:", sne.get_profile("A"))
    print("Friends of A:", sne.get_friends("A"))

    # BFS
    print("Shortest Path A -> F:", sne.shortest_path("A", "F"))

    # DFS
    print("DFS from A depth 2:", sne.dfs_depth("A", 2))

    # Recommendations
    print("Recommendations for A:", sne.recommend("A"))