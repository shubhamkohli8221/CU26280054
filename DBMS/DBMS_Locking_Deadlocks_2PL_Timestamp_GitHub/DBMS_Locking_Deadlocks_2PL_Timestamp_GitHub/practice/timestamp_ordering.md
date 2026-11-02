# Timestamp-Ordering Simulation Practice

This is a manual schedule simulation, not an implementation of MySQL's storage engine.

## Rules
Each transaction receives a unique timestamp `TS(T)`. For each data item X, track:
- `read_TS(X)`: largest timestamp of a successful read of X.
- `write_TS(X)`: largest timestamp of a successful write of X.

**Read rule:** T may read X if `TS(T) >= write_TS(X)`; otherwise T is rolled back.

**Basic write rule:** reject a write if `TS(T) < read_TS(X)` or `TS(T) < write_TS(X)`.

## Given simulation

Initial values: `read_TS(X) = 0`, `write_TS(X) = 0`.

| Action | TS(T) | read_TS(X) after action | write_TS(X) after action | Result |
|---|---:|---:|---:|---|
| T1 reads X | 5 | 5 | 0 | Allowed because 5 >= write_TS(X) |
| T2 writes X | 10 | 5 | 10 | Allowed because 10 is not less than read_TS(X) or write_TS(X) |
| T1 tries to write X | 5 | 5 | 10 | Rejected; TS(T1) < write_TS(X), so abort/restart T1 |

## Practice questions
1. Explain why T1 must not overwrite a value written by a transaction with a later timestamp.
2. Repeat the final write attempt with `TS(T1) = 15`. Would it pass the basic write rule if the timestamp metadata remains unchanged? Explain.
3. Apply the timestamp read and write rules to a new schedule of your choice.
