# -*- coding: UTF-8 -*-
"""Combined PyBank and PyPoll Script."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

def analyze_financial_data(file_to_load, file_to_output):
    # Define variables to track the financial data
    total_months = 0
    total_net = 0
    months = []
    changes = []

    # Open and read the csv
    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)

        # Skip the header row
        header = next(reader)

        # Extract first row to avoid appending to net_change_list
        first_row = next(reader)
        total_months += 1
        total_net += int(first_row[1])
        previous_profit = int(first_row[1])
        months.append(first_row[0])

        # Process each row of data
        for row in reader:
            total_months += 1
            total_net += int(row[1])

            # Track the net change
            change = int(row[1]) - previous_profit
            changes.append(change)
            months.append(row[0])
            previous_profit = int(row[1])

    # Calculate the average net change across the months
    average_change = sum(changes) / len(changes)
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    greatest_increase_month = months[changes.index(greatest_increase) + 1]
    greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

    # Generate the output summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )

    # Print the output
    print(output)

    # Write the results to a text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

def analyze_election_data(file_to_load, file_to_output):
    # Define variables to track election data
    total_votes = 0
    candidate_votes = {}
    candidates = []

    # Open and read the csv
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Skip the header row
        header = next(reader)

        # Process each row of data
        for row in reader:
            # Count the total votes
            total_votes += 1

            # Extract the candidate's name
            candidate_name = row[2]

            # If the candidate is not in the list, add them
            if candidate_name not in candidates:
                candidates.append(candidate_name)
                candidate_votes[candidate_name] = 0

            # Add a vote to the candidate's count
            candidate_votes[candidate_name] += 1

    # Calculate the results
    winner = ""
    winning_count = 0

    results = []
    for candidate in candidates:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100
        results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")

        # Determine the winner
        if votes > winning_count:
            winning_count = votes
            winner = candidate

    # Generate the output summary
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        + "\n".join(results) + "\n"
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )

    # Print the output
    print(output)

    # Write the results to a text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

# Main function
if __name__ == "__main__":

    analyze_financial_data(
        file_to_load=os.path.join("Resources", "budget_data.csv"),
        file_to_output=os.path.join("analysis", "budget_analysis.txt")
    )

    analyze_election_data(
        file_to_load=os.path.join("Resources", "election_data.csv"),
        file_to_output=os.path.join("analysis", "election_analysis.txt")
    )
