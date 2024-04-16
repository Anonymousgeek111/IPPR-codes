import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


image_path = 'F:\TY Sem 2\IPPR\Practicals\clg.jpg'  
image = Image.open(image_path).rotate(angle=-90,expand=True)


image_array = np.array(image)


e = 1.3
enhanced_image_array = np.clip(image_array * e, 0, 255).astype(np.uint8)


enhanced_image = Image.fromarray(enhanced_image_array)


fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(enhanced_image)
axes[1].set_title('Enhanced')
axes[1].axis('off')

plt.show()
