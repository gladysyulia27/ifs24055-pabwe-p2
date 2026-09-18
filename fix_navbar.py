import glob, re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = re.compile(
        r'<li\s+class="nav-item">\s*<a\s+href="index\.html#cta"\s+class="nav-link">CONTACT\s+US</a>\s*</li>\s*</ul>\s*</nav>(?:\s*<!--[^>]*-->)?\s*<div\s+class="header-action">\s*<a\s+href="index\.html#cta"\s+class="btn\s+btn-pill\s+btn-primary">GET\s+STARTED</a>\s*</div>',
        re.DOTALL
    )
    
    new_content = pattern.sub(
        r'<li class="nav-item"><a href="index.html#cta" class="btn btn-pill btn-primary">GET STARTED</a></li>\n                </ul>\n            </nav>',
        content
    )
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
