# Two-Phase Locking (2PL) Schedule Practice

## Basic 2PL rules
- **Growing phase:** a transaction may acquire locks but cannot release any lock.
- **Shrinking phase:** a transaction may release locks but cannot acquire new locks.
- Basic 2PL ensures conflict serializability but does not itself prevent deadlocks.
- Strict 2PL holds exclusive locks until commit or rollback.

## Experiment 6 schedule

| Step | Transaction T1 | Transaction T2 | 2PL note |
|---|---|---|---|
| 1 | LOCK-S(A) | — | T1 growing phase |
| 2 | READ(A) | LOCK-S(B) | T1 still growing; T2 growing |
| 3 | LOCK-X(B) request | READ(B) | T1 may wait if T2 holds S(B) |
| 4 | — | UNLOCK(B) | T2 starts shrinking; cannot acquire new locks afterward |
| 5 | LOCK-X(B) granted if available | COMMIT | T1 may proceed |
| 6 | WRITE(B); COMMIT | — | Release locks at end for strict 2PL |

Mark the growing and shrinking phases for each transaction.

## Experiment 7: Schedule that violates 2PL

| Step | Operation by T1 |
|---|---|
| 1 | LOCK-S(A) |
| 2 | READ(A) |
| 3 | UNLOCK(A) |
| 4 | LOCK-X(B) |
| 5 | WRITE(B) |

**Question:** Is this schedule permitted by basic 2PL? Explain why or why not.

**Answer from the lab sheet:** No. T1 acquires X(B) after releasing A, which means it acquires a new lock during the shrinking phase.
