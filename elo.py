#project 4 kdu5
import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import random

# Task 1: Calculate player ratings based on past matches.
def calculate_ratings(past_matches_filename):
    # Initialize dictionary to store player ratings
    player_ratings = {0: 1500, 1: 1500, 2: 1500, 3: 1500, 4: 1500, 5: 1500, 6: 1500, 7: 1500}

    # Constant for Elo rating calculation
    c = 100

    try:
        with open(past_matches_filename, 'r') as file:
            # Read matches from CSV file
            matches_reader = csv.reader(file)
            next(matches_reader)  # Skip header row
            for row in matches_reader:
                # Extract player indices from the match data and convert to integers
                player_a_idx, player_b_idx = int(row[1]), int(row[2])

                # Calculate probabilities of player A and B winning
                delta = (player_ratings[player_a_idx] - player_ratings[player_b_idx]) / c
                prob_a_wins = 1 / (1 + np.exp(-delta))
                prob_b_wins = 1 - prob_a_wins

                # Update player ratings based on match outcome and convert winner index to integer
                winner_idx = int(row[3])
                if winner_idx == player_a_idx:
                    player_ratings[player_a_idx] += 5 * (1.0 - prob_a_wins)
                    player_ratings[player_b_idx] += 5 * (0.0 - prob_b_wins)
                elif winner_idx == player_b_idx:
                    player_ratings[player_a_idx] += 5 * (0.0 - prob_a_wins)
                    player_ratings[player_b_idx] += 5 * (1.0 - prob_b_wins)
    except Exception as e:
        print("Error:", e)
        print("Failed to read the input file.")
        return None

    return player_ratings

# Task 2: Display player ratings in a bar chart.
def display_ratings(player_ratings):
    # Extract player names and ratings from the dictionary
    players = list(player_ratings.keys())
    ratings = list(player_ratings.values())

    # Plot the ratings
    plt.figure(figsize=(10, 6))
    plt.bar(players, ratings, color='skyblue')
    plt.xlabel('Players')
    plt.ylabel('Ratings')
    plt.title('Player Ratings')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

    # Save the plot to a PDF file
    plt.savefig('projections.pdf')

# Task 3: Simulate matches and project win probabilities.
def calculate_win_probability(rating_A, rating_B, c):
    delta = (rating_A - rating_B) / c
    return math.exp(delta) / (1 + math.exp(delta))

def simulate_match(player_ratings, player_A, player_B, c):
    rating_A = player_ratings[player_A]
    rating_B = player_ratings[player_B]
    prob_A = calculate_win_probability(rating_A, rating_B, c)
    return player_A if random.random() < prob_A else player_B

def project_win_probs(player_ratings, c=400, n=100):
    # Initialize dictionary to store win probabilities for each player
    win_probabilities = {player: 0 for player in player_ratings.keys()}

    # Simulate the tournament n times
    for _ in range(n):
        # Copy the original player ratings to avoid modification
        simulated_ratings = player_ratings.copy()

        # Simulate each round of the tournament
        for round_num in range(3):
            matches_in_round = [(0, 7), (3, 4), (1, 6), (2, 5)]
            next_round = {}

            # Simulate matches in the current round
            for match in matches_in_round:
                winner = simulate_match(simulated_ratings, match[0], match[1], c)
                next_round[match[0] // 2] = winner

            # Update simulated ratings with winners for the next round
            simulated_ratings.update(next_round)

        # Increment win count for the winner of the simulated tournament
        winner = next_round[0]
        win_probabilities[winner] += 1

    # Convert win counts to probabilities
    total_simulations = n
    for player, wins in win_probabilities.items():
        win_probabilities[player] = wins / total_simulations

    return win_probabilities

# Task 4: Display win probabilities in a pie chart and save to file.
def display_probs(win_probabilities):
    # Sort win probabilities in descending order
    sorted_probs = sorted(win_probabilities.items(), key=lambda x: x[1], reverse=True)

    # Write win probabilities to probs.csv
    with open('probs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Player', 'Probability'])
        for player, prob in sorted_probs:
            writer.writerow([player, prob])

    # Generate pie chart and save it to projections_pie.pdf
    labels = [f'Player {player}' for player, _ in sorted_probs]
    probabilities = [prob for _, prob in sorted_probs]
    plt.figure(figsize=(8, 8))
    plt.pie(probabilities, labels=labels, autopct='%1.1f%%')
    plt.title('Tournament Win Probabilities')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('projections_pie.pdf')
    plt.show()
