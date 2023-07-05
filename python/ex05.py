def fetuccine(n, pri, seg):
	if(n == 1): return pri
	if(n == 2): return seg
	i = 4
	prox = pri + seg
	while(i <= n):
		pri = seg
		seg = prox
		prox = (seg - pri) if (i%2 == 0) else (pri + seg)
		i += 1
	return prox

def principal():
	termos = int(input())
	n1, n2 = map(int, input().split())
	i = 1
	while(i<termos):
		print(fetuccine(i, n1, n2), end = ' ')
		i += 1
	print(fetuccine(termos, n1, n2))
principal()