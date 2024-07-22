import z3

def load_SMTLIB(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    solver = z3.Solver()
    solver.from_string(content)
    
    return solver

def add_constraints(solver, constraints):
    # Add constraints with this function
    for constraint in constraints:
        solver.add(constraint)