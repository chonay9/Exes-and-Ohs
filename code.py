def xo(s):
    s = s.lower() #pasamos a minusculas
    print(s)
    print("s.count('x'): ",s.count('x'))
    print("s.count('o')",s.count('o'))
    print("s.count('x') == s.count('o')",s.count('x') == s.count('o'))
    return s.count('x') == s.count('o') #busca un substring en un string
    
#TDD code
#Test.expect(xo('xo'), 'True expected')
#Test.expect(xo('xo0'), 'True expected')
#Test.expect(not xo('xxxoo'), 'False expected')
#
