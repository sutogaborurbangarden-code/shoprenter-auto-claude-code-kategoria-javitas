import json,glob,sys,re
D=sys.argv[1]
kw={}
def add(k,v,c):
    k=k.strip()
    if v is None: return
    if k not in kw or v>kw[k][0]: kw[k]=(v,c)
for f in glob.glob(D+'/mcp-*.txt')+glob.glob(D+'/extra*.json'):
    _d = json.load(open(f))
    for r in (_d.get('result') or _d.get('data') or []):
        add(r['keyword'],r['avg_monthly_searches'],r.get('keyword_competition'))
for line in open(D+'/inline.tsv',encoding='utf8'):
    p=line.rstrip('\n').split('\t')
    if len(p)>=2 and p[1]: add(p[0],int(p[1]),p[2] if len(p)>2 and p[2] else None)
json.dump(kw,open(D+'/all.json','w'),ensure_ascii=False)
print(len(kw))
