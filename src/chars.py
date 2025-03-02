from enum import IntEnum, auto

class Character(IntEnum):
    # Firsts chars
    NEWLINE = ord("\n")
    SPACE = ord(" ")
    
    # Latin Characters
    LA01 = ord('a')
    LA02 = ord('A')
    LB01 = ord('b')
    LB02 = ord('B')
    LC01 = ord('c')
    LC02 = ord('C')
    LD01 = ord('d')
    LD02 = ord('D')
    LE01 = ord('e')
    LE02 = ord('E')
    LF01 = ord('f')
    LF02 = ord('F')
    LG01 = ord('g')
    LG02 = ord('G')
    LH01 = ord('h')
    LH02 = ord('H')
    LI01 = ord('i')
    LI02 = ord('I')
    LJ01 = ord('j')
    LJ02 = ord('J')
    LK01 = ord('k')
    LK02 = ord('K')
    LL01 = ord('l')
    LL02 = ord('L')
    LM01 = ord('m')
    LM02 = ord('M')
    LN01 = ord('n')
    LN02 = ord('N')
    LO01 = ord('o')
    LO02 = ord('O')
    LP01 = ord('p')
    LP02 = ord('P')
    LQ01 = ord('q')
    LQ02 = ord('Q')
    LR01 = ord('r')
    LR02 = ord('R')
    LS01 = ord('s')
    LS02 = ord('S')
    LT01 = ord('t')
    LT02 = ord('T')
    LU01 = ord('u')
    LU02 = ord('U')
    LV01 = ord('v')
    LV02 = ord('V')
    LW01 = ord('w')
    LW02 = ord('W')
    LX01 = ord('x')
    LX02 = ord('X')
    LY01 = ord('y')
    LY02 = ord('Y')
    LZ01 = ord('z')
    LZ02 = ord('Z')
    
    # Numeric Characters
    ND01 = ord('1')
    ND02 = ord('2')
    ND03 = ord('3')
    ND04 = ord('4')
    ND05 = ord('5')
    ND06 = ord('6')
    ND07 = ord('7')
    ND08 = ord('8')
    ND09 = ord('9')
    ND10 = ord('0')
    
    # Special Characters
    SP02 = ord('!')
    SC03 = ord('$')
    SP04 = ord('"')
    SP05 = ord('\'')
    SP06 = ord('(')
    SP07 = ord(')')
    SP08 = ord(',')
    SP09 = ord('_')
    SP10 = ord('-')
    SP11 = ord('.')
    SP12 = ord('/')
    SP13 = ord(':')
    SP14 = ord(';')
    SP15 = ord('?')
    SA01 = ord('+')
    SA03 = ord('<')
    SA04 = ord('=')
    SA05 = ord('>')
    SM01 = ord('#')
    SM02 = ord('%')
    SM03 = ord('&')
    SM04 = ord('*')
    SM05 = ord('@')
    SM06 = ord('[')
    SM07 = ord('\\')
    SM08 = ord(']')
    SM11 = ord('{')
    SM13 = ord('|')
    SM14 = ord('}')
    SD13 = ord('`')
    SD15 = ord('^')
    SD19 = ord('~')

    def __repr__(self):
        return f"Character.{self.name}"

    def __str__(self):
        return f"Character.{self.name}"

class SyntaxType(IntEnum):
    CONSTITUENT = auto()
    TERMINATING_MACRO_CHAR = auto()
    NON_TERMINATING_MACRO_CHAR = auto()
    SINGLE_ESCAPE = auto()
    MULTIPLE_ESCAPE = auto()
    WHITESPACE = auto()
    INVALID = auto()

    def __repr__(self):
        return f"SyntaxType.{self.name}"

    def __str__(self):
        return f"SyntaxType.{self.name}"

def get_syntax_type(character: Character) -> SyntaxType:
    whitespace_chars = {Character.NEWLINE, Character.SPACE}
    terminating_macro_chars = {ord('"'), ord('\''), ord('('), ord(')'), ord(','), ord(';'), ord('`')}
    non_terminating_macro_chars = {ord('#')}
    single_escape_chars = {ord('\\')}
    multiple_escape_chars = {ord('|')}
    valid_chars = set(Character)

    if ord(character) not in valid_chars:
        return SyntaxType.INVALID
    if character in whitespace_chars:
        return SyntaxType.WHITESPACE
    if character in terminating_macro_chars:
        return SyntaxType.TERMINATING_MACRO_CHAR
    if character in non_terminating_macro_chars:
        return SyntaxType.NON_TERMINATING_MACRO_CHAR
    if character in single_escape_chars:
        return SyntaxType.SINGLE_ESCAPE
    if character in multiple_escape_chars:
        return SyntaxType.MULTIPLE_ESCAPE
    
    return SyntaxType.CONSTITUENT