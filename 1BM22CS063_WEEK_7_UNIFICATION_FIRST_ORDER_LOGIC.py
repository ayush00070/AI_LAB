from typing import Union, Dict, List, Tuple

# Define types for terms
Term = Union[str, Tuple[str, List['Term']]]

# Check if a term is a variable
def is_variable(term: Term) -> bool:
    return isinstance(term, str) and term.islower()

# Check if a term is a constant
def is_constant(term: Term) -> bool:
    return isinstance(term, str) and term.isupper()

# Check if a term is a compound term
def is_compound(term: Term) -> bool:
    return isinstance(term, tuple) and len(term) == 2 and isinstance(term[1], list)

# Unification algorithm
def unify(term1: Term, term2: Term, substitutions: Dict[str, Term] = None) -> Union[Dict[str, Term], str]:
    if substitutions is None:
        substitutions = {}

    if term1 == term2:
        return substitutions

    if is_variable(term1):
        return unify_variable(term1, term2, substitutions)

    if is_variable(term2):
        return unify_variable(term2, term1, substitutions)

    if is_compound(term1) and is_compound(term2):
        if term1[0] != term2[0] or len(term1[1]) != len(term2[1]):
            return "Failure"
        for arg1, arg2 in zip(term1[1], term2[1]):
            substitutions = unify(arg1, arg2, substitutions)
            if substitutions == "Failure":
                return "Failure"
        return substitutions

    if is_constant(term1) and is_constant(term2):
        return "Failure" if term1 != term2 else substitutions

    return "Failure"

def unify_variable(var: str, term: Term, substitutions: Dict[str, Term]) -> Union[Dict[str, Term], str]:
    if var in substitutions:
        return unify(substitutions[var], term, substitutions)
    if occurs_check(var, term, substitutions):
        return "Failure"
    substitutions[var] = term
    return substitutions

def occurs_check(var: str, term: Term, substitutions: Dict[str, Term]) -> bool:
    if var == term:
        return True
    if is_compound(term):
        return any(occurs_check(var, arg, substitutions) for arg in term[1])
    if is_variable(term) and term in substitutions:
        return occurs_check(var, substitutions[term], substitutions)
    return False

# Apply substitutions to a term
def apply_substitutions(term: Term, substitutions: Dict[str, Term]) -> Term:
    if is_variable(term):
        if term in substitutions:
            return apply_substitutions(substitutions[term], substitutions)
        return term
    if is_compound(term):
        return (term[0], [apply_substitutions(arg, substitutions) for arg in term[1]])
    return term  # Return constant as is

# Resolve final substitutions
def resolve_final_substitutions(substitutions: Dict[str, Term]) -> Dict[str, Term]:
    final_substitutions = {}
    for var, value in substitutions.items():
        final_substitutions[var] = apply_substitutions(value, substitutions)
    return final_substitutions

# Parse user input into a term
def parse_term(term_str: str) -> Term:
    if "(" not in term_str:
        return term_str  # Variable or constant
    functor, args = term_str.split("(", 1)
    args = args.rstrip(")").split(",")
    return (functor, [parse_term(arg.strip()) for arg in args])

# Convert term back to string for output
def term_to_string(term: Term) -> str:
    if is_variable(term) or is_constant(term):
        return term
    if is_compound(term):
        return f"{term[0]}({', '.join(term_to_string(arg) for arg in term[1])})"

# Main function for user input
def main():
    print("Enter two expressions to unify (e.g., Eats(x, Apple) or Eats(Riya, y)):")
    term1_str = input("Expression A: ")
    term2_str = input("Expression B: ")

    term1 = parse_term(term1_str)
    term2 = parse_term(term2_str)

    result = unify(term1, term2)
    if result == "Failure":
        print("Unification failed.")
    else:
        print("Unification successful.")
        
        # Resolve final substitutions
        final_substitutions = resolve_final_substitutions(result)
        
        print("\nFinal Substitutions:")
        for var, value in final_substitutions.items():
            print(f"  {var} = {term_to_string(value)}")
        
        # Apply substitutions to expressions
        unified_term1 = apply_substitutions(term1, final_substitutions)
        unified_term2 = apply_substitutions(term2, final_substitutions)
        
        print("\nExpressions after substitution:")
        print(f"  Expression A: {term_to_string(unified_term1)}")
        print(f"  Expression B: {term_to_string(unified_term2)}")

if __name__ == "__main__":
    main()
