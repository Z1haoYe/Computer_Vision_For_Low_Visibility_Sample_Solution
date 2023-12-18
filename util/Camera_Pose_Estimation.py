import cv2
import numpy as np

# List of image filenames in your dataset
image_files = []  # Add all your image filenames here

# Initialize the feature detector and descriptor extractor
orb = cv2.ORB_create()

# Initialize variables to store camera poses
camera_poses = []

# Iterate through pairs of images
for i in range(len(image_files) - 1):
    img1 = cv2.imread(image_files[i], cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_files[i + 1], cv2.IMREAD_GRAYSCALE)

    # Detect keypoints and compute descriptors for both images
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Create a feature matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match features between the images
    matches = bf.match(des1, des2)

    # Extract matched keypoints
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Use the RANSAC algorithm to estimate the fundamental matrix and remove outliers
    F, mask = cv2.findFundamentalMat(src_pts, dst_pts, cv2.FM_RANSAC)

    # Recover the essential matrix from the fundamental matrix (for calibrated cameras)
    E = np.dot(camera_matrix.T, np.dot(F, camera_matrix))

    # Decompose the essential matrix into rotation and translation (camera pose)
    _, R, t, _ = cv2.recoverPose(E, src_pts, dst_pts, camera_matrix)

    # Store the camera pose for the second image in the pair
    camera_poses.append((R, t))

# 'camera_poses' now contains the relative camera poses for each pair of consecutive images
# You can further refine these poses and perform global optimization if needed.