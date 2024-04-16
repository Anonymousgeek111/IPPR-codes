from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_path = 'F:\TY Sem 2\IPPR\Practicals\clg.jpg'
image = Image.open(image_path).rotate(angle=-90,expand=True)
print(image.size)


image_array = np.array(image)


r, g, b = np.split(image_array, 3, axis=2)
print(image_array)

r = np.clip(r, 0, 255)
g = np.clip(g, 0, 255)
b = np.clip(b, 0, 255)


fig,axes = plt.subplots(2, 2, figsize=(10, 7))


axes[0, 0].imshow(image)
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')


axes[0, 1].imshow(r, cmap='Reds' )
axes[0, 1].set_title('Red Channel')
axes[0, 1].axis('off')

axes[1, 0].imshow(g, cmap='Greens')
axes[1, 0].set_title('Green Channel')
axes[1, 0].axis('off')

axes[1, 1].imshow(b, cmap='Blues')
axes[1, 1].set_title('Blue Channel')
axes[1, 1].axis('off')



plt.show()
