import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

prod_imgs = ['product-1.png', 'product-2.png', 'product-3.png', 'product-4.png']
def cat_replacer(match):
    cat_replacer.i = getattr(cat_replacer, 'i', 0)
    res = f'src="{prod_imgs[cat_replacer.i % len(prod_imgs)]}"'
    cat_replacer.i += 1
    return res

content = re.sub(r'src="https://images.unsplash.com[^"]*?w=200[^"]*"', cat_replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
