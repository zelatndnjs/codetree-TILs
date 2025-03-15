a,b,c = map(int,input().split())
starttime = 11*1440+11*60+11
endtime = a*1440+b*60+c
print(endtime-starttime)