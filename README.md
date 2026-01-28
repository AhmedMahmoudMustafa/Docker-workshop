# Data Engineering Zoomcamp – Module 1: Docker, SQL & Terraform

This repository contains my work for **Module 1 (Docker, SQL & Terraform)** of the **Data Engineering Zoomcamp (2026)** by DataTalksClub.

The goal of this module was to:
- Set up a reproducible local data engineering environment using Docker
- Load and query NYC Taxi data using PostgreSQL and SQL
- Understand Docker networking and containerized services
- Learn the Terraform workflow for infrastructure provisioning

---

## 📂 Repository Structure
.
├── Homework/ # Module 1 homework (Docker & SQL)
│ ├── data_ingestion.py # CLI script to load data into Postgres
│ ├── docker-compose.yml # Postgres + pgAdmin (provided by course)
│ ├── data/ # Local data (ignored by git)
│ └── README.md # Homework answers + SQL queries
│
├── pipeline/ # Practice code from the module tutorials
├── DOCKER_ARCHITECTURE.md # Notes on Docker concepts and architecture
└── README.md # This file

> **Note:** Raw data files (CSV / Parquet) are intentionally excluded from version control and must be downloaded locally.

---

## 🧰 Technologies Used

- **Docker & Docker Compose** – containerized PostgreSQL and pgAdmin
- **PostgreSQL** – analytical database
- **SQL** – data exploration and aggregation
- **Python 3.13**
- **uv** – Python package & environment manager
- **pandas / pyarrow** – data loading and transformation
- **SQLAlchemy** – database connectivity
- **Click** – command-line interface
- **Terraform** – infrastructure provisioning concepts (theory)

---

## 🚀 Module 1 Highlights

### Docker & SQL
- Ran interactive containers using official Python images
- Understood Docker networking and service hostnames
- Loaded NYC Green Taxi data into Postgres
- Executed analytical SQL queries on real datasets

### Terraform
- Learned the standard Terraform workflow:
  - `terraform init`
  - `terraform apply`
  - `terraform destroy`
- Understood provider plugins, state, and resource lifecycle

---

## 📌 Homework

All homework-related answers, SQL queries, and commands for **Module 1** are documented in:


