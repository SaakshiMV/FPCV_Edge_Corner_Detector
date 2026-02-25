# Ultimate Edge & Corner Detector 🧭

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-app-red)
![License](https://img.shields.io/badge/license-MIT-green)

An interactive computer vision tool for **visualizing and comparing classical edge and corner detection algorithms**.  
Experiment with **Sobel, Canny, Harris, and Shi-Tomasi** detectors and observe their behavior in real time.

Built with **Streamlit** for an intuitive UI and instant feedback.

---

## ✨ Overview

**Ultimate Edge & Corner Detector** allows users to upload an image and explore how different detection algorithms respond to parameter changes.

Instead of static outputs, the application provides **live visual experimentation**, making it useful for:

- Learning computer vision fundamentals  
- Understanding algorithm behavior  
- Rapid prototyping & testing  

---

## 🚀 Features

✔ Upload any image for analysis  
✔ Compare multiple algorithms side by side  
✔ Interactive parameter tuning with sliders  
✔ Real-time visual updates  
✔ Save / download processed results  

---

## 🔍 Supported Algorithms

| Category | Algorithm          | Description |
|----------|-------------------|-------------|
| **Edge Detection** | **Sobel** | Computes image gradients to highlight edges |
| | **Canny** | Multi-stage edge detection with noise filtering |
| **Corner Detection** | **Harris** | Detects corners via local intensity variations |
| | **Shi-Tomasi** | Improved corner detection for tracking & features |

---

## 🧠 Edge vs Corner Detection

**Edge Detection** identifies regions of sharp intensity change useful for:

- Boundary detection  
- Shape analysis  
- Segmentation  

**Corner Detection** identifies interest points where edges intersect useful for:

- Feature tracking  
- Image matching  
- Object recognition  
- 3D reconstruction  

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SaakshiMV/FPCV_Edge_Corner_Detector.git
cd FPCV_Edge_Corner_Detector
````

---

### 2️⃣ Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Streamlit will automatically open the app in your browser.

---

## 🧭 Usage

1. Launch the Streamlit app
2. Upload an image
3. Adjust detector parameters (thresholds, block size, etc.)
4. Observe live changes
5. Save or download outputs

---

## 📂 Project Structure

```
FPCV_Edge_Corner_Detector/
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── README.md
├── .gitignore
```

---

## 🔮 Future Enhancements

* Add modern detectors (FAST, ORB, SIFT)
* Batch image processing
* Parameter presets for quick testing
* Visual overlays & annotations
* Performance optimizations

---

## 🤝 Contributing

Contributions are welcome!

Possible improvements:

* New detection algorithms
* UI/UX enhancements
* Example datasets
* Performance improvements

---

## 📜 License

This project is open-source.
