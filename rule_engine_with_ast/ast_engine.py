class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # e.g., 'AND', 'age > 30'
        self.left = left  # Left child node
        self.right = right  # Right child node

def create_rule(rule_string):
    # Parse rule_string and create an AST
    if " AND " in rule_string:
        left_rule, right_rule = rule_string.split(" AND ")
        return Node(type='operator', value='AND',
                    left=create_rule(left_rule.strip()),
                    right=create_rule(right_rule.strip()))
    else:
        return Node(type='operand', value=rule_string.strip())

def evaluate_rule(ast, data):
    # Evaluate the AST against the data
    if ast.type == 'operator' and ast.value == 'AND':
        return (evaluate_rule(ast.left, data) and
                evaluate_rule(ast.right, data))
    return eval_operand(ast.value, data)

def eval_operand(condition, data):
    # Basic evaluation: check if a condition holds based on input data
    key, op, val = condition.split()
    val = int(val)
    if op == '>':
        return data[key] > val
    elif op == '<':
        return data[key] < val
    elif op == '==':
        return data[key] == val
    return False

def combine_rules(rules):
    # Combine multiple rules into a single AST using an 'AND' operator at the root
    if not rules:
        return None  # Return None if there are no rules

    # Create the root node for the 'AND' operation
    root = Node(type='operator', value='AND')
    
    # The left child is the first rule as a Node
    root.left = create_rule(rules[0])
    current = root  # Start from the root
    
    # Loop through the remaining rules to create the right side
    for rule in rules[1:]:
        # Create a new Node for the next rule
        new_node = create_rule(rule)
        current.right = new_node  # Link it as the right child
        current = new_node  # Move current to the newly added node
    
    return root
