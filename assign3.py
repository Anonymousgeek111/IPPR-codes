from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_path = 'F:\TY Sem 2\IPPR\Practicals\clg.jpg' 
image = Image.open(image_path)
image = image.rotate(angle=-90,expand=True)


image_array = np.array(image)
print("Original Image Array",image_array)


negative_image_array = 255 - image_array
print("Negative image array : ",negative_image_array)


negative_image = Image.fromarray(negative_image_array.astype(np.uint8))


fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(negative_image)
axes[1].set_title('Negative')
axes[1].axis('off')
fig.set_facecolor("grey")

plt.show()

