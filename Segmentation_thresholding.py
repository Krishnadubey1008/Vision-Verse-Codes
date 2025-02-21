# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OEjj7GaZpDkpgNJhLw-JCwyDMnldtIDj

Task 1
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 3))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/1.png"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 3))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/2.png"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 3))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/3.png"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 3))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/4.png"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 2))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/5.png"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def kmeans_segmentation(img_path, k_values):

    original_img = Image.open(img_path)

    img_array = np.array(original_img)

    # Reshaping image to a 2D array of pixels
    pixels = img_array.reshape((-1, 2))

    pixels = shuffle(pixels, random_state=42)

    # Creating subplots for each value of K
    fig, axs = plt.subplots(1, len(k_values) + 1, figsize=(15, 5))

    # Ploting original image
    axs[0].imshow(img_array)
    axs[0].set_title("Original Image")
    axs[0].axis("off")


    for i, k in enumerate(k_values):
        # Applying KMeans clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]

        # Reshaping segmented image back to original shape
        segmented_img = segmented_img.astype(np.uint8).reshape(img_array.shape)

        axs[i+1].imshow(segmented_img)
        axs[i+1].set_title(f"K = {k}")
        axs[i+1].axis("off")

    plt.show()

img_path = "/content/6.jpg"
k_values = [3, 5, 8]
kmeans_segmentation(img_path, k_values)

"""TASK 2"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_and_normal_thresholding(img_path, normal_threshold):

    original_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Otsu's thresholding
    _, otsu_thresholded = cv2.threshold(original_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Normal thresholding
    _, normal_thresholded = cv2.threshold(original_img, normal_threshold, 255, cv2.THRESH_BINARY)

    # Plotting
    plt.figure(figsize=(12, 4))

    plt.subplot(131)
    plt.imshow(original_img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(otsu_thresholded, cmap='gray')
    plt.title('Otsu\'s Thresholding')
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(normal_thresholded, cmap='gray')
    plt.title('Normal Thresholding')
    plt.axis('off')

    plt.show()

img_path = "/content/boat.jpg"
normal_threshold_value = 127

otsu_and_normal_thresholding(img_path, normal_threshold_value)
