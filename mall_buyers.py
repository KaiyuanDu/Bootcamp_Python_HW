#project 3 kdu5
# Importing the random module for random selection
import random
from fractions import Fraction  # Import Fraction for handling fractional prices

# Defining the Node class to represent buildings
class Node:
    def __init__(self, node_id, connected_nodes, min_price, frac_price):
        self.id = node_id  # Unique identifier for the node
        self.connected_nodes = connected_nodes  # List of connected node ids
        self.minimum_price = Fraction(min_price)  # Minimum price to move to this node
        self.fractional_price = Fraction(frac_price)  # Fractional price to move to this node
        self.revenue = Fraction(0)  # Revenue generated from this node

# Defining the Buyer class to represent buyers with budgets
class Buyer:
    def __init__(self, current_node_id, remaining_budget):
        self.current_node_id = current_node_id  # Current node where the buyer is located
        self.remaining_budget = Fraction(remaining_budget)  # Remaining budget of the buyer

# Function to run the simulation
def run_simulation(connectivity_file, pricing_file, budget_file):
    # Read connectivity file and create graph
    graph = {}
    with open(connectivity_file, 'r') as file:
        for line in file:
            u, v = line.strip().split()  # Splitting each line to get node connections
            if u not in graph:
                graph[u] = Node(u, [], 0, 0)  # Create node if not already present
            if v not in graph:
                graph[v] = Node(v, [], 0, 0)  # Create node if not already present
            graph[u].connected_nodes.append(v)  # Adding connected node to the graph

    # Read pricing file and update Node pricing scheme
    with open(pricing_file, 'r') as file:
        for line in file:
            # Splitting line to get building id, minimum price, and fractional price
            building_id, min_price_num, min_price_denom, frac_price_num, frac_price_denom = line.strip().split()
            # Updating the node's pricing scheme
            graph[building_id].minimum_price = Fraction(int(min_price_num), int(min_price_denom))
            graph[building_id].fractional_price = Fraction(int(frac_price_num), int(frac_price_denom))

    # Create list of buyers with budgets
    buyers = []
    with open(budget_file, 'r') as file:
        # Reading budget from the first line and converting to integer list
        budget_list = [int(budget) for budget in file.readline().strip().split()]
        # Creating Buyer objects with budget and adding to the buyers list
        for i, budget in enumerate(budget_list):
            buyer = Buyer(str(i), budget)
            buyers.append(buyer)

    # Simulate movement and purchasing
    for buyer in buyers:
        while True:
            current_node = graph[buyer.current_node_id]  # Get the current node of the buyer
            next_node_id = random.choice(current_node.connected_nodes)  # Choose a random connected node
            next_node = graph[next_node_id]  # Get the next node from the graph
            # Calculate the price to move to the next node
            price = calculate_price(buyer.remaining_budget, next_node.minimum_price, next_node.fractional_price)
            if price > 0:  # If the price is positive, meaning buyer can afford to move
                next_node.revenue += price  # Increment revenue of the next node
                buyer.remaining_budget -= price  # Deduct price from buyer's remaining budget
                buyer.current_node_id = next_node_id  # Update buyer's current node
            else:
                break  # If price is zero or negative, break the loop

    # Calculate total revenue and fraction of total revenue for each building
    total_revenue = sum(node.revenue for node in graph.values())  # Calculate total revenue
    revenue_fraction = {node.id: node.revenue / total_revenue for node in graph.values()}  # Calculate revenue fraction for each building

    return total_revenue, revenue_fraction

# Function to calculate the price to move to the next node
def calculate_price(remaining_budget, min_price, frac_price):
    # Return the minimum price if it's less than or equal to the remaining budget
    if min_price <= remaining_budget:
        return min_price
    # Otherwise, return the fractional price if it's less than or equal to the remaining budget
    elif frac_price <= remaining_budget:
        return frac_price
    else:
        return 0  # Return 0 if both prices are greater than the remaining budget
