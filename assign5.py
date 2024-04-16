from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_normalized_cmy(image_path):
    # Read the image using PIL
    image = Image.open(image_path)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Calculate the mean and standard deviation of the RGB image
    # mean = np.mean(image_array)
    # std = np.std(image_array)

    # Normalize the RGB image
    # normalized_image_array = (image_array - mean) / std

    # Convert the normalized RGB image to CMY
    cmy_image_array = 1 - (image_array/255.0)

    # Clip values to be in the range [0, 1]
    cmy_image_array = np.clip(cmy_image_array, 0, 1)

    # Create a new image from the normalized CMY array
    cmy_image = Image.fromarray((cmy_image_array * 255).astype(np.uint8))

    return image, cmy_image

# Path to the input RGB image
image_path = "F:\TY Sem 2\IPPR\Practicals\clg.jpg"

# Convert RGB to normalized CMY
rgb_image, cmy_image = rgb_to_normalized_cmy(image_path)

# Display the RGB and CMY images
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(rgb_image)
axs[0].set_title('RGB Image')
axs[0].axis('off')
axs[1].imshow(cmy_image)
axs[1].set_title('Normalized CMY Image')
axs[1].axis('off')
plt.show()
