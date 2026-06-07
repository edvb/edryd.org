#!/usr/bin/env python3

import yaml
import urllib.request
import requests
import shutil
import os
import chevron
from pathlib import Path

# TODO flag -v for verbose printing
# TODO flag -d for destination

# TODO write in eevo
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

def gen_galleries(input_file):
    # Read the input YAML file
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    galleries = []

    # Process each gallery
    for gallery in data['galleries']:
        title = gallery['title']
        date = gallery['date']
        folder = "photos/" + str(date) + "/" + title.lower().replace(' ', '-')

        # Get all image files from the folder with the same name as title
        folder_path = "content/" / Path(folder)
        images = [folder + "/" + f.name for f in folder_path.iterdir()
                    # Only include images, not index pages
                    if f.is_file() and f.suffix != '.md']

        # Create new YAML structure
        new_gallery = {
            'title': title,
            'date': date,
            'link': folder,
            # TODO cover or first image
            'cover': folder + "/" + gallery['cover'],
            'images': images
        }

        # Add to galleries index
        galleries.append(new_gallery)

    return galleries

def transform_galleries(input_file, templ_index, templ_gallery):
    galleries = gen_galleries(input_file)

    os.makedirs('content/photos', exist_ok=True)
    print(f'creating content/photos/_index.md')
    with open(templ_index, 'r') as templ, \
         open('content/photos/_index.md', 'w') as f:
        f.write(chevron.render(templ, { 'galleries': galleries }))

    for gallery in galleries:
        with open(templ_gallery, 'r') as templ:
            os.makedirs(f'content/photos/{gallery['date']}', exist_ok=True)
            # TODO make content/photos/{date}/_index.md for all photos that year,
            #      with list on galleries page for each year
            print(f'creating content/{gallery['link']}/_index.md')
            with open(f'content/{gallery['link']}/_index.md', 'w') as f:
                f.write(chevron.render(templ, gallery))

print(f'creating photo pages')
transform_galleries('data/galleries.yaml',
                    'templ/index.md', 'templ/gallery.md')
