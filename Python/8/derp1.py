"""
241 Lab 8 - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates preorder expressions 
containing basic arithmetic operators (*,//,-+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Sean Strout (sps@cs.rit.edu)
Author: Zeyar Win
"""

##############################################################################
# structure definitions for parse tree
##############################################################################

class MultiplyNode:
    """Represents an multiply operator, *"""
    
    __slots__ = ('left', 'right')
    
class DivideNode:
    """Represents an integer divide operator, //"""

    __slots__ = ('left', 'right')
    
class AddNode:
    """Represents an addition operator, +"""

    __slots__ = ('left', 'right')
    
class SubtractNode:
    """Represents an addition operator, -"""

    __slots__ = ('left', 'right')
    
class LiteralNode:
    """Represents an operand node"""
    
    __slots__ = ('val')
    
class VariableNode:
    """Represents a variable node"""
    
    __slots__ = ('name')
class Empty:
    ''' empty node'''
    __slots__=()

    
##############################################################################
# structure creation routines for parse tree
##############################################################################
        
def mkMultiplyNode(left, right):
    """mkMultiplyNode(): Node * Node -> MultiplyNode
    Creates and returns an multiply node."""
    
    node = MultiplyNode()
    node.left = left
    node.right = right
    return node
    
def mkDivideNode(left, right):
    """mkDivideNode(): Node * Node -> DivideNode
    Creates and returns an divide node."""

    node = DivideNode()
    node.left = left
    node.right = right
    return node

def mkAddNode(left, right):
    """mkAddNode(): Node * Node -> AddNode
    Creates and returns an add node."""

    node = AddNode()
    node.left = left
    node.right = right
    return node

def mkSubtractNode(left, right):
    """mkSubtractNode(): Node * Node -> SubtractNode
    Creates and returns a subtract node."""

    node = SubtractNode()
    node.left = left
    node.right = right
    return node    
    
def mkLiteralNode(val):
    """mkOperatorNode(): int -> LiteralNode
    Creates and returns a literal node."""
    
    node = LiteralNode()
    node.val = val
    return node
    
def mkVariableNode(name):
    """mkVariableNode(): String -> VariableNode
    Creates and returns an variable node."""

    node = VariableNode()
    node.name = name
    return node

   
        
##############################################################################
# parse
############################################################################## 
    
def parse(token):
    """parse: list(String) -> Node
    From an inorder stream of tokens, and a symbol table, construct and
    return the tree, as a collection of Nodes, that represent the
    expression.
    """
    if token==[]:
        return
    
    t=token.pop(0)
    print(t)
    if t=="*":
        return mkMultiplyNode(parse(token),parse(token))
    elif t=='//':
        return mkDivideNode(parse(token),parse(token))
    elif t=='-':
        return mkSubtractNode(parse(token),parse(token))
    elif t=='+':
        return mkAddNode(parse(token),parse(token))
    elif t.isdigit() :
        return mkLiteralNode(t)
    elif not t.isdigit() :
        return mkVariableNode(t)


        
    
    


 
            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if isinstance(node,Empty):
        return ''
    elif isinstance(node,MultiplyNode):
        #node =mkMultilplyNode()
        return '('+infix(node.left)+'*'+infix(node.right)+')'
    elif isinstance(node,DivideNode):
        #node=mkDivideNode()
        return '('+infix(node.left)+'//'+infix(node.right)+')'
    elif isinstance(node,SubtractNode):
        #node=mkSubtractNode()
        return '('+infix(node.left)+'-'+infix(node.right)+')'
    elif isinstance(node,AddNode):
        #node=AddNode()
        return '('+infix(node.left)+'+'+infix(node.right)+')'
    elif isinstance(node,LiteralNode):
        return str(node.val)
    elif isinstance(node,VariableNode):
        return str(node.name)
    else:
        return ''
 
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if isinstance(node,Empty):
        return
 
    if isinstance(node,MultiplyNode):
        return evaluate(node.left,symTbl)*evaluate(node.right,symTbl)
    elif isinstance(node,DivideNode):
        return evaluate(node.left,symTbl)//evaluate(node.right,symTbl)
    elif isinstance(node,SubtractNode):
        return evaluate(node.left,symTbl)-evaluate(node.right,symTbl)
    elif isinstance(node,AddNode):
        return evaluate(node.left,symTbl)+evaluate(node.right,symTbl)
    elif isinstance(node,LiteralNode):
        
        return int(node.val)
    elif isinstance(node,VariableNode):
        print(node.name)
        return int(symTbl[node.name])
         
        
        
    
    pass
    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symTbl=dict()
    for line in open(inFile):
        line.strip()
        line=line.split()    
        symTbl[line[0]]=int(line[1])
        for var in symTbl:
            print('variable :'+var +'integer'+str(symTbl[var]))
        
            
    
    
    print("Herp, enter prefix expressions, e.g.: + 10 20 (RETURN to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens=prefixExp.split()
       
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE
        # print(parse(tokens))
        print("\n")
        to=parse(tokens)
        
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING    
        b=infix(to)
        print( b )
        print("Derping the infix expression: "+str(b))
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT
        c=evaluate(to,symTbl)
        print("Derping the evaluation: "+str(c))
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
