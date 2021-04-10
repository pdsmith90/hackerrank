from itertools import permutations
hack=list(input().split())
hackPermu=sorted(list(permutations(list(hack[0]),int(hack[1]))))
print('\n'.join([''.join(x) for x in hackPermu]))
