
import glob

main_name = 'portalet'


with open('./summer/portalet.md','w') as file:
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

	for image in glob.glob(f'./assets/images/summer/{main_name}/*'):
		text = f"""

<center> </center>

![](.{image})


"""
		file.write(text)


