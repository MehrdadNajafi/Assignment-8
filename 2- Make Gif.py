import imageio
import os
images = []
print('Making...')
for file_name in os.listdir('images'):
    image = imageio.imread(f"images/{file_name}")
    images.append(image)
imageio.mimsave('Noooo!.gif', images)
print('Done!')