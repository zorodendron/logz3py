import logging
import time
from z3 import *

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Logging inferred claueses

inferred_clauses = []

def on_clause_callback(pr, deps, clause):
    inferred_clauses.append((pr, deps, clause))
    logger.info(f"Proof hint: {pr}, Dependencies: {deps}, Clause: {clause}")

# Logging solver statistics
def log_solver_statistics(solver):
    stats = solver.statistics()
    for key, value in stats:
        logger.info(f"Solver Statistic - {key}: {value}")

s = Solver()
s.set(unsat_core=True)

A, B = Bools('A B')
s.add(And(A, B))
s.add(Not(B))

onc = OnClause(s, on_clause_callback)

start_time = time.time()
result = s.check()
end_time = time.time()

logger.info(f"Solver result: {result}")
logger.info(f"Solver time: {end_time - start_time} seconds")

log_solver_statistics(s)

if result == sat:
    m = s.model()
    logger.info(f"Model: {m}")
else:
    logger.info("No model found")

# summary of inferred clauses
logger.info(f"Total inferred clauses: {len(inferred_clauses)}")
for pr, deps, clause in inferred_clauses:
    logger.info(f"Inferred Clause - Proof hint: {pr}, Dependencies: {deps}, Clause: {clause}")
