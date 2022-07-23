import ply.lex as lex

class PythonLexer(object) :
    reserved = {
        'False' : 'FALSE',      #reserved words
        'None' : 'NONE',
        'True' : 'TRUE',
        'and' : 'AND',
        'as' : 'AS',
        'assert' : 'ASSERT',
        'async' : 'ASYNC',
        'await' : 'AWAIT',
        'break' : 'BREAK',
        'class' : 'CLASS',
        'continue' : 'CONTINUE',
        'def' : 'DEF',
        'del' : 'DEL',
        'elif' : 'ELIF',
        'else' : 'ELSE',
        'except' : 'EXCEPT',
        'finally' : 'FINALLY',
        'for' : 'FOR',
        'from' : 'FROM',
        'global' : 'GLOBAL',
        'if' : 'IF',
        'import' : 'IMPORT',
        'in' : 'IN',
        'is' : 'IS',
        'lambda' : 'LAMBDA',
        'nonlocal' : 'NONLOCAL',
        'not' : 'NOT',
        'or' : 'OR',
        'pass' : 'PASS',
        'raise' : 'RAISE',
        'return' : 'RETURN',
        'try' : 'TRY',
        'while' : 'WHILE',
        'with' : 'WITH',
        'yield' : 'YIELD',
        'abs' : 'ABS',          #built in functions
        'aiter' : 'AITER',
        'all' : 'ALL',
        'any' : 'ANY',
        'anext' : 'ANEXT',
        'ascii' : 'ASCII',
        'bin' : 'BIN',
        'bool' : 'BOOL',
        'breakpoint' : 'BREAKPOINT',
        'bytearray' : 'BYTEARRAY',
        'bytes' : 'BYTES',
        'callable' : 'CALLABLE',
        'chr' : 'CHR',
        'classmethod' : 'CLASSMETHOD',
        'complie' : 'COMPLIE',
        'complex' : 'COMPLEX',
        'delattr' : 'DELATTR',
        'dict' : 'DICT',
        'dir' : 'DIR',
        'divmod' : 'DIVMOD',
        'enumerate' : 'ENUMERATE',
        'eval' : 'EVAL',
        'exec' : 'EXEC',
        'filter' : 'FILTER',
        'float' : 'FLOAT',
        'format' : 'FORMAT',
        'frozenset' : 'FROZENSET',
        'getattr' : 'GETATTR',
        'globals' : 'GLOBALS',
        'hasattr' : 'HASATTR',
        'hash' : 'HASH',
        'help' : 'HELP',
        'hex' : 'HEX',
        'id' : 'ID',
        'input' : 'INPUT',
        'int' : 'INT',
        'isinstance' : 'ISINSTANCE',
        'issubclass' : 'ISSUBCLASS',
        'iter' : 'ITER',
        'len' : 'LEN',
        'list' : 'LIST',
        'locals' : 'LOCALS',
        'map' : 'MAP',
        'max' : 'MAX',
        'memoryview' : 'MEMORYVIEW',
        'min' : 'MIN',
        'next' : 'NEXT',
        'object' : 'OBJECT',
        'oct' : 'OCT',
        'open' : 'OPEN',
        'ord' : 'ORD',
        'pow' : 'POW',
        'print' : 'PRINT',
        'property' : 'PROPERTY',
        'range' : 'RANGE',
        'repr' : 'REPR',
        'reversed' : 'REVERSED',
        'round' : 'ROUND',
        'set' : 'SET',
        'setattr' : 'SETATTR',
        'slice' : 'SLICE',
        'sorted' : 'SORTED',
        'staticmethod' : 'STATICMETHOD',
        'str' : 'STR',
        'sum' : 'SUM',
        'super' : 'SUPER',
        'tuple' : 'TUPLE',
        'type' : 'TYPE',
        'vars' : 'VARS',
        'zip' : 'ZIP',
        '__import__' : '__IMPORT__',
    }
    
    tokens = [
        'VARIABLE',
        'INTEGER',
        'STRING',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MODULUS',
        'FLOORDIVISION',
        'EXPONENT',
        'GREATER',
        'LESS',
        'GREATEREQUAL',
        'LESSEQUAL',
        'EQUAL',
        'NOTEQUAL',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'LBRACKET',
        'RBRACKET',
        'COMMA',
        'DOT',
        'COLON',
        'ASSIGNMENT',
        'UNDERBAR',
        'TRIPLEDOT',
        'BLANK',
        'NEWLINE',
    ] + list(reserved.values())

    t_INTEGER = r'[+-]?(0|[1-9]\d*)'
    t_STRING = r'(\'\'\'(.|\n)*\'\'\'|\"\"\"(.|\n)*\"\"\"|\'[^\']*\'|\"[^\"]*\")'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULUS = r'%'
    t_FLOORDIVISION = r'//'
    t_EXPONENT = r'\*\*'
    t_GREATER = r'>'
    t_LESS = r'<'
    t_GREATEREQUAL = r'>='
    t_LESSEQUAL = r'<='
    t_EQUAL = r'=='
    t_NOTEQUAL = r'!='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_COMMA = r','
    t_DOT = r'\.'
    t_COLON = r':'
    t_ASSIGNMENT = r'='
    t_UNDERBAR = r'_'
    t_TRIPLEDOT = r'\.{3}'
    t_BLANK = r'[ \t]'

    t_ignore_COMMENT = r'\#.*'

    def t_VARIABLE(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'VARIABLE')
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while(True):
            tok = self.lexer.token()
            if(not tok):
                break
            print(tok)

    def test_blank(self, data):
        self.lexer.input(data)

        newline_flag = False
        
        while(True):
            tok = self.lexer.token()
            if(not tok):
                break
            if(tok.type == 'NEWLINE'):
                newline_flag = True
            if(tok.type == 'BLANK' and newline_flag == False):
                continue
            if(tok.type != 'NEWLINE' and tok.type != 'BLANK' and newline_flag == True):
                newline_flag = False
            print(tok)
            
