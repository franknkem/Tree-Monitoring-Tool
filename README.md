# Tree-Monitoring-Tool
Offline command-line tool for monitoring and reporting mango tree planting activities in low-resource environments.

# Mango Tree Planting Monitoring Tool

# Overview

The Mango Tree Planting Monitoring Tool is a lightweight, offline command-line application built with Python to support the tracking and monitoring of tree planting activities.

This tool was developed as part of a National Youth Service Corps (NYSC) community development initiative to document and monitor the condition of 12 mango trees planted within a camp environment.

It enables simple data tracking, follow-up planning, and report generation in low-resource or offline settings.

---

# Problem Statement

Tree planting initiatives are often carried out without structured systems for:

* tracking planted trees over time
* monitoring survival and health status
* assigning maintenance responsibility
* generating simple reports for documentation

This tool provides a basic, practical solution to support these needs.

---

# Features

# Data Viewing

* View all tree records
* View project summary (total, healthy, weak, dead)
* Identify trees needing attention
* View tree distribution by location
* View assigned teams responsible for maintenance

# Data Management

* Update tree status (Healthy / Needs Water / Dead)
* Update next inspection date
* Update assigned team/person

# Reporting

* Generate a structured text report
* Save report locally for documentation

---

## Project Structure

```
tree-planting-monitoring-tool/
├── trees_monitor.py
├── data/
│   └── trees.csv
├── reports/
│   └── summary_report.txt
├── README.md
└── requirements.txt
```

---

# Data Format

The tool uses a CSV file (`data/trees.csv`) to store tree records.

# Example:

```
tree_id,species,location,date_planted,status,next_check,assigned_to
001,Mango,Camp Gate,2026-03-29,Healthy,2026-04-15,Team A
002,Mango,Admin Block,2026-03-29,Needs Water,2026-04-15,Team B
```

### Field Descriptions:

* tree_id: Unique identifier for each tree
* species: Type of tree (Mango)
* location: Planting location within the camp
* date_planted: Date of planting
* status: Current condition (Healthy, Needs Water, Dead)
* next_check: Scheduled follow-up date
* assigned_to: Responsible team or individual


## Installation

### Requirements

* Python 3.x installed
* No external libraries required

### Clone the repository

```
git clone <your-repo-link>
cd tree-planting-monitoring-tool
```

---

## Usage

All commands are run from the terminal inside the project directory.

# Show all trees

```
python trees_monitor.py --list
```

# Show summary

```
python trees_monitor.py --summary
```

# Show trees needing attention

```
python trees_monitor.py --needs-attention
```

# Show location breakdown

```
python trees_monitor.py --locations
```

# Show team breakdown

```
python trees_monitor.py --teams
```

# Generate report

```
python trees_monitor.py --report
```

# Update a tree record

```
python trees_monitor.py --update <tree_id>
```

Example:

```
python trees_monitor.py --update 004
```

You will be prompted to enter:

* new status
* next check date
* assigned team/person

# Example Workflow

1. Record planted trees in `trees.csv`
2. Conduct periodic inspections
3. Update tree status using the tool
4. Generate reports for monitoring and documentation



# Use Case

This tool is designed for:

* NYSC CDS coordinators
* community environmental projects
* small-scale tree planting initiatives
* offline or low-connectivity environments

# Future Improvements

* Menu-based interface for easier navigation
* Automatic detection of overdue inspections
* Ability to add new tree records from terminal
* Integration with mobile or form-based data collection


# Author

Developed as part of a community-based environmental initiative for the SDGs CDS Tree Planting Project during NYSC Rivers State Orientation Camp 2026 Batch A1.


# License

This project is for educational and non-commercial use.

