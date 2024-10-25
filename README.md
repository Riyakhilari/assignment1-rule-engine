# assignment1-rule-engine
This repository contains the implementation of a Rule Engine using Abstract Syntax Trees (AST). The engine allows users to create and evaluate rules based on specified conditions.
The project supports rules with AND, OR operators, and comparison expressions like >, <, and =.

To run the project, clone the repository using git clone <repository-url> and navigate into the project directory using cd rule_engine_with_ast. Ensure you have Python 3.x installed. No external dependencies are required. You can run the main code with python main.py and test the functionality using python -m pytest tests/.

The code structure includes:

ast_node.py: Contains the ASTNode class for building the tree structure.
main.py: Main logic for parsing rules and evaluating them.
tests/test_ast_engine.py: Test cases for parsing and evaluation.
README.md: Documentation of the project (this file).
An example rule is "salary > 50000 AND experience > 5", and with data like {"salary": 60000, "experience": 6}, the AST looks like:Node(type=operator, value=AND)
  Node(type=operand, value=salary > 50000)
  Node(type=operand, value=experience > 5)
  The evaluation result for this rule and data will be True.
 Non-Functional Considerations  
1. Security Layer:
   - Sanitization of input data and rules to prevent injection attacks.  
   - Type-checking of AST nodes to ensure valid operations only.  

2. Performance Optimization:
   - Short-circuiting logic for `AND` and `OR` operators.  
   - Optimized recursion to minimize function calls.

3. Scalability:
   - Modular design allows for easy extensions, such as adding new operators or conditions.


Authored By,
Riya Khilari
