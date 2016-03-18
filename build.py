#!/usr/bin/env python3

from glob import glob
import subprocess

if __name__ == '__main__':
    header = open('header.html').read()

    for filename in glob('*.md'):
        markdown = open(filename).read()
        title = markdown.split('\n')[0][1:].strip()
        html = subprocess.check_output(['marked', filename]).decode()

        output = header.format(title=title, body=html)

        newpath = filename.split('.')[:-1]
        newpath.append('html')
        newpath = '.'.join(newpath)

        open(newpath, 'w+').write(output)
