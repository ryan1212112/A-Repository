a,b,c = int(input()),int(input()),int(input())

def fun(a,b,c):
    '''
    
      Parameters
      ----------
      a : TYPE
          DESCRIPTION.
      b : TYPE
          DESCRIPTION.
      c : TYPE
          DESCRIPTION.
    
      Returns
      -------
      list
          DESCRIPTION.
    
      '''  
    return [(-b + (b**2 - 4*a*c)**0.5)/(2*a),(-b - (b**2 - 4*a*c)**0.5)/(2*a)]

print(fun(a,b,c))
