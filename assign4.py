from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def normalize_image(image_path):
    # Read the image using PIL
    image = Image.open(image_path)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Calculate the mean and standard deviation of the pixel values
    mean = np.mean(image_array)
    std = np.std(image_array)

    # Normalize the pixel values
    normalized_image_array = (image_array - mean) / std

    # Clip values to be in the range [0, 1]
    normalized_image_array = np.clip(normalized_image_array, 0, 1)

    # Convert the normalized array back to an image
    normalized_image = Image.fromarray((normalized_image_array * 255).astype(np.uint8))

    return image, normalized_image, image_array, normalized_image_array

def plot_histograms(image_array1, image_array2, title1, title2):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    freq1, bins1, _ = plt.hist(image_array1.ravel(), bins=256, range=(0.0, 1.0), color='blue', alpha=0.7)
    plt.yscale('log')
    plt.yticks(np.power(10, np.arange(0, 5)), ['1', '10', '100', '1000', '10000'])
    plt.title(title1)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency (log scale)')
    plt.subplot(1, 2, 2)
    freq2, bins2, _ = plt.hist(image_array2.ravel(), bins=256, range=(0.0, 1.0), color='red', alpha=0.7)
    plt.yscale('log')
    plt.yticks(np.power(10, np.arange(0, 5)), ['1', '10', '100', '1000', '10000'])
    plt.title(title2)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency (log scale)')
    plt.show()

# Example usage:


# Path to the input image
image_path = "F:\TY Sem 2\IPPR\Practicals\clg.jpg"

# Normalize the image
original_image, normalized_image, original_image_array, normalized_image_array = normalize_image(image_path)

# Display the original and normalized images
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(original_image)
axs[0].set_title('Original Image')
axs[0].axis('off')
axs[1].imshow(normalized_image)
axs[1].set_title('Normalized Image')
axs[1].axis('off')
plt.show()

# Display histograms
plot_histograms(original_image_array / 255.0, normalized_image_array, 'Histogram Before Normalization', 'Histogram After Normalization')






# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# def normalize_image(image):
#     # Convert image to floating point
#     image = image.astype(np.float32)

#     # Normalize each channel separately
#     for i in range(image.shape[2]):
#         min_val = np.min(image[:,:,i])
#         max_val = np.max(image[:,:,i])
#         image[:,:,i] = 255 * (image[:,:,i] - min_val) / (max_val - min_val)
    
#     # Convert back to uint8 and clip values to [0, 255]
#     image = np.clip(image, 0, 255).astype(np.uint8)
#     return image

# # Read the input image
# input_image = cv2.imread('input_image.jpeg')

# # Check if the image exists
# if input_image is None:
#     print("Error: Could not read the image.")
# else:
#     # Normalize the image
#     normalized_image = normalize_image(input_image)
    
#     # Plot original and normalized images
#     fig, axes = plt.subplots(1, 2, figsize=(10, 5))
#     axes[0].imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
#     axes[0].set_title('Original Image')
#     axes[0].axis('on')
#     axes[1].imshow(cv2.cvtColor(normalized_image, cv2.COLOR_BGR2RGB))
#     axes[1].set_title('Normalized Image')
#     axes[1].axis('on')
#     plt.show()
#     print("Normalized image saved successfully.")