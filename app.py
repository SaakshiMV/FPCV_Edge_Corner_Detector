import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

st.set_page_config(layout="wide")
st.title("Edge & Corner Detector - Original | Detection | Heatmap")
st.write("View original, corner/edge detection, and heatmap side-by-side.")

# --- Upload Image ---
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    img = np.array(image.convert("RGB"))

    # --- Sidebar Parameters ---
    st.sidebar.header("Canny Parameters")
    canny_low = st.sidebar.slider("Canny Low Threshold", 0, 500, 100)
    canny_high = st.sidebar.slider("Canny High Threshold", 0, 500, 200)

    st.sidebar.header("Harris Parameters (odd)")
    harris_block = st.sidebar.slider("Block Size", 1, 31, 3, step=2)
    harris_ksize = st.sidebar.slider("Aperture (ksize)", 1, 31, 3, step=2)
    harris_k = st.sidebar.slider("Harris k", 0.01, 0.10, 0.04)

    st.sidebar.header("Shi-Tomasi Parameters")
    shi_max_corners = st.sidebar.slider("Max Corners", 1, 200, 50)
    shi_quality = st.sidebar.slider("Quality Level", 0.01, 0.20, 0.01)
    shi_min_distance = st.sidebar.slider("Min Distance", 1, 50, 10)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # --- Sobel ---
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = cv2.magnitude(sobelx, sobely).astype(np.uint8)
    sobel_heatmap = cv2.applyColorMap(cv2.normalize(sobel_mag, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8), cv2.COLORMAP_JET)

    # --- Canny ---
    edges = cv2.Canny(gray, canny_low, canny_high)
    canny_heatmap = cv2.applyColorMap(cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8), cv2.COLORMAP_JET)

    # --- Harris Corners ---
    gray_float = np.float32(gray)
    dst = cv2.cornerHarris(gray_float, harris_block, harris_ksize, harris_k)
    dst = cv2.dilate(dst, None)
    harris_img = img.copy()
    harris_img[dst > 0.01 * dst.max()] = [255, 0, 0]

    # --- Shi-Tomasi Corners ---
    shi_img = img.copy()
    corners = cv2.goodFeaturesToTrack(gray, shi_max_corners, shi_quality, shi_min_distance)
    if corners is not None:
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(shi_img, (int(x), int(y)), 4, (0, 255, 0), -1)

    # --- Tabs ---
    tabs = st.tabs(["Sobel", "Canny", "Harris", "Shi-Tomasi"])

    # --- Helper function to display 1x3 images ---
    def display_1x3(orig, detection, heatmap, save_name_prefix):
        col1, col2, col3 = st.columns(3)
        col1.image(orig, caption="Original", use_column_width=True)
        col2.image(detection, caption="Detection", use_column_width=True)
        col3.image(heatmap, caption="Heatmap", use_column_width=True)

        if st.button(f"Save {save_name_prefix} Results"):
            os.makedirs("processed_results", exist_ok=True)
            Image.fromarray(orig).save(f"processed_results/{save_name_prefix}_original.png")
            Image.fromarray(detection).save(f"processed_results/{save_name_prefix}_detection.png")
            Image.fromarray(heatmap).save(f"processed_results/{save_name_prefix}_heatmap.png")
            st.success(f"✅ {save_name_prefix} images saved!")

    # --- Sobel Tab ---
    with tabs[0]:
        display_1x3(img, sobel_mag, sobel_heatmap, "Sobel")

    # --- Canny Tab ---
    with tabs[1]:
        display_1x3(img, edges, canny_heatmap, "Canny")

    # --- Harris Tab ---
    with tabs[2]:
        # Heatmap for Harris is just red corners over black background
        harris_heatmap = np.zeros_like(img)
        harris_heatmap[harris_img[:, :, 0] == 255] = [255, 0, 0]
        display_1x3(img, harris_img, harris_heatmap, "Harris")

    # --- Shi-Tomasi Tab ---
    with tabs[3]:
        # Heatmap for Shi-Tomasi is green corners over black background
        shi_heatmap = np.zeros_like(img)
        shi_heatmap[shi_img[:, :, 1] == 255] = [0, 255, 0]
        display_1x3(img, shi_img, shi_heatmap, "ShiTomasi")
