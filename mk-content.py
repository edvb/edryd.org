#!/usr/bin/env python3

import yaml
import urllib.request
import requests
import shutil
import os

# TODO flag -v for verbose printing
# TODO flag -d for destination

# TODO write in tisp
with open('data/projects.yaml') as d:
    data = yaml.load(d, Loader=yaml.FullLoader)
    if not os.path.exists('content/projects'):
        os.mkdir('content/projects')
    print(f'creating script pages')
    for gist in data['scripts']:
        gid = gist['id']
        r = requests.get('https://api.github.com/gists/' + gid)
        desc = r.json()['description']
        title = list(r.json()['files'])[0].split('.')[0].lower()
        with open(f'content/projects/{title}.md', 'w') as f:
            f.write(f'---\ntitle: {title}\ndescription: {desc}\n---\n')
            for file in iter(r.json()['files'].values()):
                name = file['filename']
                lang = file['language'].lower()
                content = file['content']
                f.write(f'##### {name}:\n')
                f.write(f'```{lang}\n{content}\n```\n')
                # write button
                # TODO view raw file
                # with open(f'content/projects/{name}', 'w') as fp:
                #     fp.write(content)
    print(f'creating project pages')
    for code in data['code']:
        if 'link' in code:
            continue
        name = code['name']
        desc = code['desc']
        with open(f'content/projects/{name}.md', 'w') as f:
            f.write(f'---\ntitle: {name}\ndescription: {desc}\n---\n')
        url = f'https://raw.githubusercontent.com/edvb/{name}/master/README.md'
        if name == 'tisp':
            url = 'https://raw.githubusercontent.com/edvb/tisp/master/doc/tisp.7.md'
        with urllib.request.urlopen(url) as response, open(f'content/projects/{name}.md', 'ab') as f:
            for chunk in iter(lambda: response.read(1), ''):
                if chunk == b'':
                    break
                    response.seek(0)
                    url  = f'https://raw.githubusercontent.com/edvb/{name}/master/' + response.read()
                    with urllib.request.urlopen(url) as response:
                        shutil.copyfileobj(response, f)
                if chunk == b'\n':
                    break
            shutil.copyfileobj(response, f)

# TODO replace with parital in layout page
# https://gohugo.io/templates/lookup-order/
print(f'creating photo pages')
with open('data/photos.yaml') as d:
    data = yaml.load(d, Loader=yaml.FullLoader)
    if not os.path.exists('content/photos'):
        os.mkdir('content/photos')
    with open('content/photos/_index.md', 'w') as f:
        f.write('---\ntitle: photos\n---\n')
        f.write(f'{{{{< photos limit="999" dir="best">}}}}\n')
        for album in data['photos']:
            f.write(f'{{{{< photos limit="5" dir="{album["name"]}">}}}}\n')
    for album in data['photos']:
        title = album['name']
        name = title.replace(' ', '-')
        with open(f'content/photos/{name}.md', 'w') as f:
            f.write(f'---\ntitle: {title}\n---\n')
            f.write(f'{{{{< photos limit="999" dir="{title}">}}}}\n')
