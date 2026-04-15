import csv
import argparse
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------
# FILE PATHS
# ---------------------------------------------------------
# These variables tell Python where your data file and report file live.
DATA_FILE = "data/trees.csv"
REPORT_FILE = "reports/summary_report.txt"


# ---------------------------------------------------------
# LOAD TREE DATA
# ---------------------------------------------------------
def load_trees(filename):
    """
    Reads the CSV file and returns a list of tree records.

    Each row in the CSV becomes a dictionary.
    Example:
    {
        'tree_id': '001',
        'species': 'Mango',
        'location': 'Camp Gate',
        'date_planted': '2026-03-29',
        'status': 'Healthy',
        'next_check': '2026-04-15',
        'assigned_to': 'Team A'
    }
    """
    trees = []

    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            trees.append(row)

    return trees


# ---------------------------------------------------------
# SAVE TREE DATA
# ---------------------------------------------------------
def save_trees(filename, trees):
    """
    Saves the updated list of tree dictionaries back into the CSV file.
    This is important when a user updates a tree record.
    """
    fieldnames = [
        "tree_id",
        "species",
        "location",
        "date_planted",
        "status",
        "next_check",
        "assigned_to"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(trees)


# ---------------------------------------------------------
# SUMMARY CALCULATION
# ---------------------------------------------------------
def get_summary(trees):
    """
    Counts the total number of trees and how many are:
    - Healthy
    - Needs Water
    - Dead

    It also calculates survival rate.
    """
    total = len(trees)
    healthy = sum(1 for tree in trees if tree["status"].lower() == "healthy")
    needs_water = sum(1 for tree in trees if tree["status"].lower() == "needs water")
    dead = sum(1 for tree in trees if tree["status"].lower() == "dead")

    # Survival rate = all trees not dead
    survival_rate = ((healthy + needs_water) / total * 100) if total > 0 else 0

    return {
        "total": total,
        "healthy": healthy,
        "needs_water": needs_water,
        "dead": dead,
        "survival_rate": survival_rate
    }


# ---------------------------------------------------------
# SHOW ALL TREES
# ---------------------------------------------------------
def show_all_trees(trees):
    """
    Prints all tree records in a simple readable format.
    Useful for checking what data is currently stored.
    """
    print("All Mango Tree Records")
    print("-----------------------")

    for tree in trees:
        print(
            f"Tree {tree['tree_id']} | "
            f"Location: {tree['location']} | "
            f"Status: {tree['status']} | "
            f"Next Check: {tree['next_check']} | "
            f"Assigned To: {tree['assigned_to']}"
        )


# ---------------------------------------------------------
# SHOW SUMMARY
# ---------------------------------------------------------
def show_summary(trees):
    """
    Displays a summary of the tree project.
    """
    summary = get_summary(trees)

    print("Mango Tree Planting Summary")
    print("----------------------------")
    print(f"Total mango trees planted: {summary['total']}")
    print(f"Healthy: {summary['healthy']}")
    print(f"Needs Water: {summary['needs_water']}")
    print(f"Dead: {summary['dead']}")
    print(f"Survival rate: {summary['survival_rate']:.1f}%")


# ---------------------------------------------------------
# SHOW TREES NEEDING ATTENTION
# ---------------------------------------------------------
def show_needs_attention(trees):
    """
    Shows only trees that are not fully healthy.
    These are the trees that likely need follow-up.
    """
    print("Mango Trees Needing Attention")
    print("------------------------------")
    found = False

    for tree in trees:
        if tree["status"].lower() in ["needs water", "dead"]:
            print(
                f"- Tree {tree['tree_id']} at {tree['location']} "
                f"| Status: {tree['status']} | Assigned to: {tree['assigned_to']}"
            )
            found = True

    if not found:
        print("No trees currently need attention.")


# ---------------------------------------------------------
# SHOW LOCATION BREAKDOWN
# ---------------------------------------------------------
def show_location_breakdown(trees):
    """
    Counts how many trees are planted in each location.
    """
    location_counts = Counter(tree["location"] for tree in trees)

    print("Location Breakdown")
    print("-------------------")
    for location, count in location_counts.items():
        print(f"- {location}: {count} tree(s)")


# ---------------------------------------------------------
# SHOW TEAM BREAKDOWN
# ---------------------------------------------------------
def show_team_breakdown(trees):
    """
    Counts how many trees are assigned to each team/person.
    """
    team_counts = Counter(tree["assigned_to"] for tree in trees)

    print("Assigned Team Breakdown")
    print("------------------------")
    for team, count in team_counts.items():
        print(f"- {team}: {count} tree(s)")


# ---------------------------------------------------------
# UPDATE A TREE RECORD
# ---------------------------------------------------------
def update_tree(trees, tree_id):
    """
    Finds a tree by tree_id and allows the user to update:
    - status
    - next_check
    - assigned_to

    After updating, the CSV file is saved again.
    """
    for tree in trees:
        if tree["tree_id"] == tree_id:
            print("Current Tree Record")
            print("--------------------")
            print(f"Tree ID: {tree['tree_id']}")
            print(f"Location: {tree['location']}")
            print(f"Status: {tree['status']}")
            print(f"Next Check: {tree['next_check']}")
            print(f"Assigned To: {tree['assigned_to']}")
            print()

            # Ask user for new values
            new_status = input("Enter new status (Healthy / Needs Water / Dead): ").strip()
            new_next_check = input("Enter next check date (YYYY-MM-DD): ").strip()
            new_assigned_to = input("Enter assigned team/person: ").strip()

            # Only update if user entered something
            if new_status:
                tree["status"] = new_status
            if new_next_check:
                tree["next_check"] = new_next_check
            if new_assigned_to:
                tree["assigned_to"] = new_assigned_to

            save_trees(DATA_FILE, trees)

            print("\nTree record updated successfully.")
            return

    print(f"Tree with ID {tree_id} not found.")


# ---------------------------------------------------------
# GENERATE REPORT
# ---------------------------------------------------------
def generate_report(trees):
    """
    Creates a text report and saves it to reports/summary_report.txt
    """
    summary = get_summary(trees)
    location_counts = Counter(tree["location"] for tree in trees)
    team_counts = Counter(tree["assigned_to"] for tree in trees)

    report_lines = [
        "Mango Tree Monitoring Report",
        "============================",
        f"Total mango trees planted: {summary['total']}",
        f"Healthy: {summary['healthy']}",
        f"Needs Water: {summary['needs_water']}",
        f"Dead: {summary['dead']}",
        f"Survival rate: {summary['survival_rate']:.1f}%",
        "",
        "Location Breakdown:"
    ]

    for location, count in location_counts.items():
        report_lines.append(f"- {location}: {count} tree(s)")

    report_lines.append("")
    report_lines.append("Assigned Team Breakdown:")

    for team, count in team_counts.items():
        report_lines.append(f"- {team}: {count} tree(s)")

    report_lines.append("")
    report_lines.append("Trees Needing Attention:")

    attention_found = False
    for tree in trees:
        if tree["status"].lower() in ["needs water", "dead"]:
            report_lines.append(
                f"- Tree {tree['tree_id']} at {tree['location']} "
                f"| Status: {tree['status']} | Assigned to: {tree['assigned_to']}"
            )
            attention_found = True

    if not attention_found:
        report_lines.append("No trees currently need attention.")

    report_text = "\n".join(report_lines)

    print(report_text)

    # Create the reports folder if it doesn't exist
    Path("reports").mkdir(exist_ok=True)

    with open(REPORT_FILE, mode="w", encoding="utf-8") as file:
        file.write(report_text)

    print(f"\nReport saved to: {REPORT_FILE}")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
def main():
    """
    Handles command-line arguments and decides what action to run.
    """
    parser = argparse.ArgumentParser(description="Mango Tree Monitoring Tool")

    parser.add_argument("--list", action="store_true", help="Show all tree records")
    parser.add_argument("--summary", action="store_true", help="Show planting summary")
    parser.add_argument("--needs-attention", action="store_true", help="Show trees needing attention")
    parser.add_argument("--locations", action="store_true", help="Show tree count by location")
    parser.add_argument("--teams", action="store_true", help="Show tree count by assigned team")
    parser.add_argument("--report", action="store_true", help="Generate full report")
    parser.add_argument("--update", type=str, help="Update a tree record by tree ID")

    args = parser.parse_args()
    trees = load_trees(DATA_FILE)

    if args.list:
        show_all_trees(trees)
    elif args.summary:
        show_summary(trees)
    elif args.needs_attention:
        show_needs_attention(trees)
    elif args.locations:
        show_location_breakdown(trees)
    elif args.teams:
        show_team_breakdown(trees)
    elif args.report:
        generate_report(trees)
    elif args.update:
        update_tree(trees, args.update)
    else:
        parser.print_help()


# ---------------------------------------------------------
# RUN THE PROGRAM
# ---------------------------------------------------------
# This ensures Python only runs the program when you execute this file directly.
if __name__ == "__main__":
    main()