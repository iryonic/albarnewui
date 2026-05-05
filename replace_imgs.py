import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero banners first
hero_imgs = ['hero-1.png', 'hero-2.png', 'hero-3.png']
def hero_replacer(match):
    hero_replacer.i = getattr(hero_replacer, 'i', 0)
    res = f'src="{hero_imgs[hero_replacer.i % len(hero_imgs)]}"'
    hero_replacer.i += 1
    return res

content = re.sub(r'src="https://images.unsplash.com[^"]*?w=800[^"]*"', hero_replacer, content)

# Replace product images
prod_imgs = ['product-1.png', 'product-2.png', 'product-3.png', 'product-4.png']
def prod_replacer(match):
    prod_replacer.i = getattr(prod_replacer, 'i', 0)
    res = f'src="{prod_imgs[prod_replacer.i % len(prod_imgs)]}"'
    prod_replacer.i += 1
    return res

content = re.sub(r'src="https://images.unsplash.com[^"]*?w=400[^"]*"', prod_replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
