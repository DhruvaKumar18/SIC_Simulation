DATA    START   5000

        LDA     NUM
        STA     RESULT
        RSUB

NUM     WORD    100
CHAR    BYTE    C'HELLO'
HEXVAL  BYTE    X'F1'
RESULT  RESW    1

        END     DATA