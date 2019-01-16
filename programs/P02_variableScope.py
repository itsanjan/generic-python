"""
Variable scopes can be defined as LEGB
L : Local
E : Enclosed
G : Global
B : Builtin
"""

x = 'Global x'

def test():
    #global x
    y="local y"
    x="local x"
    print(x+ ',' +y)

if __name__ == '__main__':
    test()
    print(x)