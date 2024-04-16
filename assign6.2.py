from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image_array, title):
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title(title)

def histogram_equalization(image_array):
    equalized_image_array = np.empty_like(image_array)
    for i in range(3):  # Iterate over RGB channels
        channel = image_array[:,:,i]
        # Calculate the histogram
        histogram, _ = np.histogram(channel, bins=256, range=(0, 256))
        # Calculate the cumulative distribution function
        cdf = histogram.cumsum()
        cdf_normalized = cdf / cdf.max()
        # Perform histogram equalization
        equalized_channel = np.interp(channel.flatten(), range(256), cdf_normalized * 255).reshape(channel.shape)
        equalized_image_array[:,:,i] = equalized_channel

    return equalized_image_array

# Path to the input image
image_path = "F:\TY Sem 2\IPPR\Practicals\clg.jpg"

# Read the image using PIL
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Calculate and plot the original image histogram
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plot_histogram(image_array, 'Original Image Histogram')
plt.xlim([0, 256])

# Perform histogram equalization on RGB channels
equalized_image_array = histogram_equalization(image_array)

# Calculate and plot the equalized image histogram
plt.subplot(2, 2, 2)
plot_histogram(equalized_image_array, 'Equalized Image Histogram')
plt.xlim([0, 256])

# Display the original and equalized images
plt.subplot(2, 2, 3)
plt.imshow(image_array.astype(np.uint8))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(equalized_image_array.astype(np.uint8))
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
