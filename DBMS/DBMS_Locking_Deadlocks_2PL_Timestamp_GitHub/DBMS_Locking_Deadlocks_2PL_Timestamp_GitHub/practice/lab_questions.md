# Lab Questions and Observation Checklist

## Section C — Lab Questions
1. Explain shared locks and exclusive locks with an example.
2. Use two sessions to demonstrate a transaction waiting for a row lock.
3. Define deadlock and draw a wait-for graph for Experiment 3.
4. Explain how InnoDB responds when it detects a deadlock.
5. Demonstrate how consistent lock ordering can reduce deadlocks.
6. Explain growing and shrinking phases of 2PL.
7. Identify the exact step at which Experiment 7 violates 2PL.
8. Explain the difference between basic 2PL and strict 2PL.
9. Define transaction timestamps, `read_TS(X)`, and `write_TS(X)`.
10. Apply the timestamp read and write rules to a supplied schedule.
11. Compare lock-based protocols with timestamp ordering.
12. Explain why timestamp ordering is a schedule simulation in this lab rather than a MySQL mode.

## Observation table

| Experiment | Observation to record |
|---|---|
| Row lock | Which statement waited, and when did it continue? |
| Deadlock | Which transaction was selected as the victim? What error appeared? |
| Consistent ordering | Did the same lock order avoid the demonstrated circular wait? |
| 2PL schedule | Mark each transaction's growing and shrinking phases. |
| Timestamp ordering | State which read/write was accepted or rejected and why. |

## Expected learning outcome
Students should be able to explain and demonstrate locking with MySQL sessions, recognize and recover from deadlocks, analyze 2PL schedules, and apply basic timestamp-ordering rules to a transaction schedule.
