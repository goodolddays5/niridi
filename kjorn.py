def func2(arg8, arg9):
    var10 = func5()
    var14 = func6(arg9, arg8)
    var27 = var17(arg9, var10)
    var28 = (arg9 & arg8 & 765) ^ 753 & -125493483 - arg9
    var29 = ((var28 | ((var10 & var14 + arg8 + var10) | var14 ^ var27 ^ var28)) ^ var27) - ((var10 - (arg8 ^ -1564729766) & arg8) | (arg9 | ((960409714 - arg9) - var10) + ((var28 - arg8 & (var28 - var14)) - var10)))
    if arg9 < var28:
        var30 = ((478 - ((-989 | var28 - (-393 + var10 ^ var27)) | (1646763781 | var29 | var27) | ((-664 - var14) + var28) & 250636459 & arg9 ^ arg9 - var14 + var29 | var27 - arg8) - var10) - var10) & -201
    else:
        var30 = arg9 | 59
    result = ((arg9 - (var10 ^ arg9 & var28 + arg8)) + (((-1313988542 & var29 - var28) + var27) & arg8 ^ var10)) & var28
    return result
def func10(arg18, arg19):
    var24 = func11(arg18, arg19)
    var25 = arg19 | var24
    var26 = (arg18 | arg19) ^ -229
    result = arg18 ^ -749 & var24 ^ arg18
    return result
def func11(arg20, arg21):
    var22 = 0
    for var23 in range(15):
        var22 += var22 | (arg20 - var23)
    return var22
def func9():
    closure = [-10]
    def func8(arg15, arg16):
        closure[0] += func10(arg15, arg16)
        return closure[0]
    func = func8
    return func
var17 = func9()
def func5():
    func3()
    result = len(((-10 ^ -10) ^ ((i ^ -5) | -8 | 0 & 8 ^ ((-10 ^ -8) ^ -4 + 5)) & i for i in range(43)))
    func4()
    return result
def func4():
    global len
    del len
def func3():
    global len
    len = lambda x : 0
def func1(arg1, arg2):
    if arg1 < arg1:
        var3 = (-1780089391 | 551573218) | arg2
    else:
        var3 = arg2 + 1253293210
    if arg1 < arg1:
        var4 = -550 - (arg1 | 1465225901)
    else:
        var4 = (-1 | (arg2 + arg1) - arg1 & arg2 & (arg2 - (-2049737141 | arg2))) - arg1 - 566129275 ^ arg2 - 1701167260 + arg2
    var5 = arg2 | (1192623573 | arg1)
    if var5 < arg1:
        var6 = -2130471668 + -645484925 | arg1 ^ ((-1683210500 & arg2) + (var5 + 442 ^ 953))
    else:
        var6 = (479267402 | var5) & -992101019
    var7 = (arg2 - 614487247 & 824406003 ^ -461 | arg1 | -338 | (-710 - (-1720956297 ^ (-60 ^ -511))) | arg2 + 1881720180 - ((arg1 - arg2) & arg2)) + (arg2 ^ arg1) + (arg1 + ((-1711379577 + arg1 - arg2) & -745))
    result = 1897068405 - var7 | (arg2 ^ ((-77368577 | (var7 + 879249832)) - arg2))
    return result
def func6(arg11, arg12):
    def func7(acc, rest):
        var13 = -3 | 8 - acc
        if acc == 0:
            return var13
        else:
            result = func7(acc - 1, var13)
            return result
    result = func7(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 0'
    print 'func_number: 2'
    print 'arg_number: 8'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 31'
    for i in xrange(25000):
        x = 5
        x = func2(x, i)
        print x,
