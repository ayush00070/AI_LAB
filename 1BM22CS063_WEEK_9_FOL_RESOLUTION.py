from typing import List, Set, Dict, Union

def unify(literal1: str, literal2: str) -> Union[Dict[str, str], None]:
    """
    Unify two literals and return a substitution dictionary, or None if they cannot be unified.
    """
    if literal1 == literal2:
        return {}
    if literal1.startswith("~") and literal2.startswith("~"):
        return None
    if literal1.startswith("~"):
        neg, pos = literal1, literal2
    else:
        neg, pos = literal2, literal1

    if neg[1:] == pos:
        return {}
    return None

def apply_substitution(clause: Set[str], substitution: Dict[str, str]) -> Set[str]:
    """
    Apply a substitution to a clause.
    """
    new_clause = set()
    for literal in clause:
        for var, value in substitution.items():
            literal = literal.replace(var, value)
        new_clause.add(literal)
    return new_clause

def resolve(clause1: Set[str], clause2: Set[str]) -> Union[Set[str], None]:
    """
    Resolves two clauses. Returns the resolvent clause or None if resolution is not possible.
    """
    for lit1 in clause1:
        for lit2 in clause2:
            substitution = unify(lit1, lit2)
            if substitution is not None:
                # Create a new clause with unified literals removed
                new_clause = (clause1 - {lit1}) | (clause2 - {lit2})
                return apply_substitution(new_clause, substitution)
    return None

def resolution(knowledge_base: List[Set[str]], query: Set[str]) -> bool:
    """
    Implements the resolution algorithm.
    """
    # Negate the query and add it to the knowledge base
    negated_query = {f"~{literal}" if not literal.startswith("~") else literal[1:] for literal in query}
    clauses = knowledge_base + [negated_query]

    new_clauses = set()

    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i + 1, len(clauses))]
        for clause1, clause2 in pairs:
            resolvent = resolve(clause1, clause2)
            if resolvent is not None:
                if not resolvent:  # Empty clause found
                    return True
                new_clauses.add(frozenset(resolvent))

        if all(frozenset(c) in new_clauses for c in clauses):
            return False

        clauses.extend(map(set, new_clauses))

if __name__ == "__main__":
    print("Enter knowledge base (clauses) as sets of literals (comma-separated).")
    print("Example: Likes(John, Food), Food(Apple). Enter 'done' when finished.")

    knowledge_base = []
    while True:
        clause = input("Clause: ").strip()
        if clause.lower() == "done":
            break
        knowledge_base.append(set(lit.strip() for lit in clause.split(',')))

    print("Enter query as a set of literals (comma-separated).")
    query = set(lit.strip() for lit in input("Query: ").strip().split(','))

    result = resolution(knowledge_base, query)
    print("Result:", "Entailed (True)" if result else "Not Entailed (False)")
