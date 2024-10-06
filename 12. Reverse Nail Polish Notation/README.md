# Reverse Nail Polish Notation

- Here, Operands are pushed onto a stack, and when an operator is encountered, it is applied to the required number of operands popped from the stack. The result is then pushed back onto the stack.
- Also called postfix notation
- No Parentheses Needed: RPN avoids ambiguity and removes the need for parentheses, as the order of operations is determined by the position of the operators.
- Efficient for Computers: It is easier for computers and compilers to evaluate expressions using RPN as it simplifies the parsing process.

### Examples:
- In standard infix notation, you would write: ``` (3 + 4) * 5 ```
- In RPN, the same expression would be written as: ``` 3 4 + 5 * ```

![rpn-evaluation-animation](https://github.com/user-attachments/assets/a3fa855e-2222-4e86-bb33-f9eb8f27415a)
