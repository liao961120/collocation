#%%
import pathlib
from random import sample, seed
from bs4 import BeautifulSoup

p = pathlib.Path("./")

def parse_vrt(fp):
    with open(fp) as f:
        vrt = f.read()

    soup = BeautifulSoup(vrt, 'html')
    post = soup.find('post')
    content = post.find(type='body')

    for row in content.text.strip().split('\n'):
        tk = row.split('\t')[0]
        if tk == "NEWLINE":
            yield '\n'
        else:
            yield tk

# %%
seed(100)
post_pool = list(p.rglob("./*/*.vrt"))
post_pool = sample(post_pool, 500)

with open("../sampled_PTTposts.txt", "w") as f:
    for fp in post_pool:
        post = '\u3000'.join(parse_vrt(fp))
        f.write(post)
        f.write('\n')
# %%
