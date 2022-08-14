from itertools import permutations # 순열, 중복x
from itertools import combinations # 조합, 중복x
from itertools import product      # 순열, 중복o
from itertools import combinations_with_replacement # 조합, 중복o

data = ['A', 'B', 'C']
print( list(permutations(data, 3)), end='\n\n')
print( list(combinations(data, 2)), end='\n\n')
print( list(product(data, repeat=2)), end='\n\n')
print( list(combinations_with_replacement(data, 2)), end='\n\n')