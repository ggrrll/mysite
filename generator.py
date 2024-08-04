
import glob
from pathlib import Path

main_name = 'charmey'


with open(f'./vieferrate/{main_name}.md', 'w') as file:
    text = f"""
---
layout: post
title: {main_name}
description: multi pitch 
image:
show_tile: false 
---
"""
    file.write(text)

    for image in glob.glob(f'./assets/images/ferrate/{main_name}/*'):
        text = f"""

<center> </center>

![](.{image})


"""
        file.write(text)
