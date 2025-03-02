from src.chars import Character, SyntaxType, get_syntax_type
from src.errors import ReaderError, StreamEOF
from src.object import LispObject

from typing import Optional

class Reader:
    def __init__(self):
        ...

    # as in https://www.lispworks.com/documentation/HyperSpec/Body/02_b.htm
    def read(self, charStream) -> str:
        # step 1
        if charStream.eof:
            raise StreamEOF
        x = charStream.get_next()
        x_type = get_syntax_type(x)
        print(x, x_type)
        next_step = -1
        # step 2 3 4 5 6 7
        match x_type:
            case SyntaxType.INVALID: # step 2
                raise ReaderError("Invalid character")
            case SyntaxType.WHITESPACE: # step 3
                return self.read(charStream)
            case SyntaxType.NON_TERMINATING_MACRO_CHAR| SyntaxType.TERMINATING_MACRO_CHAR: # step 4
                obj = reader_macro(self.charStream, char)
                if obj is not None: # we got an obj back ! we just return it and thats all
                    return obj
            case SyntaxType.SINGLE_ESCAPE: # step 5
                if charStream.eof:
                    raise StreamEOF
                y = charStream.get_next()
                token = ""
                token += y
                # GOTO STEP 8
                next_step = 8
            case SyntaxType.MULTIPLE_ESCAPE: # step 6
                token = ""
                # GOTO STEP 9
                next_step = 9
            case SyntaxType.CONSTITUENT: # step 7
                # TODO : maybe change case in case of readtable
                token = ""
                token += x
                # GOTO STEP 8
                next_step = 8
        while next_step != -1:
            match next_step:
                case 8: # step 8
                    if charStream.eof:
                        next_step = 10
                        continue
                    y = charStream.get_next()
                    y_type = get_syntax_type(y)
                    match y_type:
                        case SyntaxType.CONSTITUENT | SyntaxType.NON_TERMINATING_MACRO_CHAR:
                            # TODO : maybe change case in case of readtable
                            token += y
                            next_step = 8
                            continue
                        case SyntaxType.SINGLE_ESCAPE:
                            if charStream.eof:
                                raise StreamEOF
                            z = charStream.get_next()
                            token += z
                            next_step = 8
                            continue
                        case SyntaxType.MULTIPLE_ESCAPE:
                            next_step = 9
                            continue
                        case SyntaxType.INVALID:
                            raise ReaderError("Invalid Character")
                        case SyntaxType.TERMINATING_MACRO_CHAR:
                            charStream.unread()
                            next_step = 10
                            continue
                        case SyntaxType.WHITESPACE:
                            # TODO : only unread if appropriate
                            charStream.unread()
                            next_step = 10
                            continue
                case 9: # step 9
                    if charStream.eof:
                        raise StreamEOF
                    y = charStream.get_next()
                    y_type = get_syntax_type(y)
                    match y_type:
                        case SyntaxType.CONSTITUENT | SyntaxType.WHITESPACE:
                            token += y
                            next_step = 9
                            continue
                        case SyntaxType.SINGLE_ESCAPE:
                            if charStream.eof:
                                raise StreamEOF
                            z = charStream.get_next()
                            token += z
                            next_step = 9
                            continue
                        case SyntaxType.MULTIPLE_ESCAPE:
                            next_step = 8
                            continue
                        case SyntaxType.INVALID:
                            raise ReaderError("Invalid character")
                case 10: # step 10 (THE END !!!!)
                    # TODO : return the object and not the raw token
                    return token 

    def reader_macro(self, stream, char) -> Optional[LispObject]:
        ...
