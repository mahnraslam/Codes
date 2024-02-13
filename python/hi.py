FROM RaNDOM IMPORT RaNDINT
DEF PRINT3D(a,YEaRS,DEP,CFT):
    FOR I IN RaNGE(YEaRS):
        PRINT(F"FOR YEaR 202{I}")
        PRINT()
        FOR J IN RaNGE(DEP):
            PRINT(F"FOR DEPaRTMENT {J+1}")
            FOR K IN RaNGE(CFT):
                PRINT(a[I][J][K],END="  ")
            PRINT()

DEF  DEPaRTMENTWISE(a,YEaRINDEX, TOTaLDEPT, TOTaLCERT ):

    MaXIMUM=[0]*4
    FOR J IN RaNGE(TOTaLDEPT):
        MaXIMUM[J]=a[4][J][0]
        FOR K IN RaNGE(5):
            IF a[4][J][K]>MaXIMUM[J]:
                MaXIMUM[J]=a[4][J][K]

        PRINT("FOR DEPaRTMENT ",J+1," MaXIMUM IS",MaXIMUM[J])
DEF YEaRWISEMINOFITDEPTWEBCERTIFICaTE(aRRaY, TOTaLYEaRS , ITDEPTINDEX, WEBCERTINDEX):
    FOR I IN RaNGE(TOTaLYEaRS):
        MIN=aRRaY[I][ITDEPTINDEX][WEBCERTINDEX]
        PRINT(F"FOR YEaR 200{I} MIN IS {MIN}")


DEF MaIN():
    a=[[[RaNDINT(14,99)FOR K IN RaNGE(5)]FOR J IN RaNGE(4)]FOR I IN RaNGE(6)]
    PRINT3D(a,6,4,5)
    DEPaRTMENTWISE(a,6,4,5)
    YEaRWISEMINOFITDEPTWEBCERTIFICaTE( a, 6, 1 , 3 )

MaIN()








