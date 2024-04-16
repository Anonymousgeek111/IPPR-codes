from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image_array, title):
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title(title)

def histogram_equalization(image_array):
    # Calculate the histogram
    histogram, _ = np.histogram(image_array, bins=256, range=(0, 256))

    # Calculate the cumulative distribution function
    cdf = histogram.cumsum()
    cdf_normalized = cdf / cdf.max()

    # Perform histogram equalization
    equalized_image_array = np.interp(image_array.flatten(), range(256), cdf_normalized * 255).reshape(image_array.shape)

    return equalized_image_array

# Path to the input image
image_path = "F:\TY Sem 2\IPPR\Practicals\clg.jpg"

# Read the image using PIL
image = Image.open(image_path)

# Convert the image to grayscale
image_gray = image.convert('L')
image_array = np.array(image_gray)

# Calculate and plot the original image histogram
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plot_histogram(image_array, 'Original Image Histogram')
plt.xlim([0, 256])

# Perform histogram equalization
equalized_image_array = histogram_equalization(image_array)

# Calculate and plot the equalized image histogram
plt.subplot(2, 2, 2)
plot_histogram(equalized_image_array, 'Equalized Image Histogram')
plt.xlim([0, 256])

# Display the original and equalized images
plt.subplot(2, 2, 3)
plt.imshow(image_gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(equalized_image_array, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()
