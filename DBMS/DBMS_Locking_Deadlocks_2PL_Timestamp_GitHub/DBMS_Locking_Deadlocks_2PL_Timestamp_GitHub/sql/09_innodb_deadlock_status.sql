-- Experiment 9: Run after a deadlock, where permitted by MySQL version.
SHOW ENGINE INNODB STATUS;
-- Look for the latest detected deadlock section.
-- Access to detailed performance_schema lock tables varies by version and privileges.
