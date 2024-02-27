#project 3 kdu5
import random


class Node:
    def __init__(self, node_id, connected_nodes, min_price, frac_price):
        self.id = node_id
        self.connected_nodes = connected_nodes
        self.minimum_price = Fraction(min_price)
        self.fractional_price = Fraction(frac_price)
        self.revenue = Fraction(0)


class Buyer:
    def __init__(self, current_node_id, remaining_budget):
        self.current_node_id = current_node_id
        self.remaining_budget = Fraction(remaining_budget)


def run_simulation(connectivity_file, pricing_file, budget_file):
    # Read connectivity file and create graph
    graph = {}
    with open(connectivity_file, 'r') as file:
        for line in file:
            u, v = line.strip().split()
            if u not in graph:
                graph[u] = Node(u, [], 0, 0)
            if v not in graph:
                graph[v] = Node(v, [], 0, 0)
            graph[u].connected_nodes.append(v)

    # Read pricing file and update Node pricing scheme
    with open(pricing_file, 'r') as file:
        for line in file:
            building_id, min_price_num, min_price_denom, frac_price_num, frac_price_denom = line.strip().split()
            graph[building_id].minimum_price = Fraction(int(min_price_num), int(min_price_denom))
            graph[building_id].fractional_price = Fraction(int(frac_price_num), int(frac_price_denom))

    # Create list of buyers with budgets
    buyers = []
    with open(budget_file, 'r') as file:
        budget_list = [int(budget) for budget in file.readline().strip().split()]
        for i, budget in enumerate(budget_list):
            buyer = Buyer(str(i), budget)
            buyers.append(buyer)

    # Simulate movement and purchasing
    for buyer in buyers:
        while True:
            current_node = graph[buyer.current_node_id]
            next_node_id = random.choice(current_node.connected_nodes)
            next_node = graph[next_node_id]
            price = calculate_price(buyer.remaining_budget, next_node.minimum_price, next_node.fractional_price)
            if price > 0:
                next_node.revenue += price
                buyer.remaining_budget -= price
                buyer.current_node_id = next_node_id
            else:
                break

    # Calculate total revenue and fraction of total revenue for each building
    total_revenue = sum(node.revenue for node in graph.values())
    revenue_fraction = {node.id: node.revenue / total_revenue for node in graph.values()}

    return total_revenue, revenue_fraction
