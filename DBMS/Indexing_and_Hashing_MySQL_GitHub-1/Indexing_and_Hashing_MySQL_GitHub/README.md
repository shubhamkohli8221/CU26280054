# DBMS Lab: Indexing and Hashing Using MySQL

SQL code booklet converted into a GitHub-ready project.

## Requirements
- MySQL 8.0
- MySQL Workbench or another MySQL client

## Project structure

```text
Indexing_and_Hashing_MySQL_GitHub/
├── README.md
└── sql/
    ├── 01_create_table_without_index.sql
    ├── 02_create_index_and_inspect_plan.sql
    ├── 03_index_filtering_column.sql
    ├── 04_composite_index_leftmost_prefix.sql
    ├── 05_hash_index_using_memory.sql
    ├── 06_hash_index_equality_vs_range.sql
    ├── 07_inspect_innodb_index.sql
    ├── 08_drop_index_and_compare.sql
    └── all_experiments.sql
```

## How to run

1. Open MySQL Workbench and connect to your MySQL 8.0 server.
2. Open the SQL files in the `sql` folder.
3. Run the numbered files in order (`01` through `08`) using the same MySQL connection.
4. Alternatively, run `sql/all_experiments.sql` once from start to finish.

The scripts create and use a separate database named `IndexHashLab`.

## Experiments
1. Create a table without an index and inspect its query plan.
2. Create an index and inspect the plan.
3. Index a filtering column.
4. Create a composite index and observe the leftmost-prefix rule.
5. Create a HASH index using the MEMORY storage engine.
6. Compare equality and range searches on the HASH index.
7. Inspect an InnoDB index.
8. Drop an index and compare the query plan.

## Important notes
- Use `EXPLAIN` to inspect `type`, `possible_keys`, `key`, and `rows`.
- MySQL's optimizer may choose a table scan for tiny tables even when an index exists.
- The explicit HASH index example uses the `MEMORY` engine.
- Ordinary InnoDB indexes are B-tree indexes. Do not uncomment or execute the commented-out InnoDB `USING HASH` statement.
- HASH indexes are suited to equality lookups, not ordered range searches or sorted output.
- MEMORY table data does not survive a MySQL server restart. Use InnoDB for ordinary persistent application data.
