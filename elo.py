# project 4 kdu5
# Task 1: Calculate player ratings based on past matches.

import csv

def calculate_ratings(past_matches_filename):
    # Initialize dictionary to store player ratings
    player_ratings = {}

    # Initialize all players with a rating of 1500
    initial_rating = 1500

    try:
        with open(past_matches_filename, 'r') as file:
            # Read matches from CSV file
            matches_reader = csv.reader(file)
            for row in matches_reader:
                # Extract player names from the match data
                player_a, player_b = row[0], row[1]

                # If player not already in dictionary, add with initial rating
                if player_a not in player_ratings:
                    player_ratings[player_a] = initial_rating
                if player_b not in player_ratings:
                    player_ratings[player_b] = initial_rating

                # Calculate delta for Elo rating calculation
                delta = (player_ratings[player_a] - player_ratings[player_b]) / 100

                # Calculate probabilities of player A and B winning
                prob_a_wins = 1 / (1 + 10 ** (-delta))
                prob_b_wins = 1 - prob_a_wins

                # Update player ratings based on match outcome
                if row[2] == 'A':
                    player_ratings[player_a] += 32 * (1 - prob_a_wins)
                    player_ratings[player_b] -= 32 * prob_b_wins
                elif row[2] == 'B':
                    player_ratings[player_a] -= 32 * prob_a_wins
                    player_ratings[player_b] += 32 * (1 - prob_b_wins)
    except Exception as e:
        print("Error:", e)
        print("Failed to read the input file.")
        return None

    return player_ratings


# Task 2: Display player ratings in a bar chart.

import matplotlib.pyplot as plt

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

import numpy as np

def simulate_match(player_ratings, player_a, player_b):
    # Calculate delta for Elo rating calculation
    delta = (player_ratings[player_a] - player_ratings[player_b]) / 100

    # Calculate win probability for player A
    prob_a_wins = np.exp(delta) / (1 + np.exp(delta))

    # Generate a random number in [0.0, 1.0)
    random_num = np.random.rand()

    # Determine the winner based on the random number and win probability
    if random_num < prob_a_wins:
        return player_a
    else:
        return player_b

def project_win_probs(player_ratings, n=100):
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
                winner = simulate_match(simulated_ratings, match[0], match[1])
                next_round[match[0] // 2] = winner

            # Update simulated ratings with winners for the next round
            simulated_ratings.update(next_round)

        # Increment win count for the winner of the simulated tournament
        winner = next_round[0]
        win_probabilities[winner] += 1 / n

    return win_probabilities

# Task 4: Display projected win probabilities in a pie chart.

import csv
import matplotlib.pyplot as plt

def display_probs(win_probabilities):
    # Sort win probabilities in descending order
    sorted_probs = sorted(win_probabilities.items(), key=lambda x: x[1], reverse=True)

    # Write sorted probabilities to probs.csv
    with open('probs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Player', 'Probability'])
        for player, prob in sorted_probs:
            writer.writerow([player, prob])

    # Plot pie chart and save to projections_pie.pdf
    labels = [f'Player {player}' for player, _ in sorted_probs]
    sizes = [prob for _, prob in sorted_probs]

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Player Win Probabilities')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig('projections_pie.pdf')

    # Show the pie chart
    plt.show()
