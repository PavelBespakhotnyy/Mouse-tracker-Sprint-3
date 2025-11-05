# 🖱️ Mouse Tracker - Mouse Movement Heatmap

Windows application: records mouse movements and creates heatmaps with videos.

---

## 🚀 QUICK START

### 1. Install Python
👉 https://www.python.org/downloads/

💡 **Recommended:** Python 3.11 or 3.12 (but newer versions may work too)

⚠️ **Must check:** `Add Python to PATH`

### 2. Install dependencies
Double-click: **`INSTALL.bat`**

### 3. Launch app
Double-click: **`START.bat`**

---

## 📖 HOW TO USE

1. **▶️ Start Recording** → move mouse → **⏹️ Stop**
2. **🔥 Show Heatmap** → see heatmap
3. **📹 Record Video** → save video (AVI format)

**Heatmap colors:**
- 🔵 Blue = low activity
- 🟢 Green = medium activity
- 🟡 Yellow = high activity
- 🔴 Red = very high activity (hot zones)

**Settings (sliders):**
- Radius (60) - point size
- Intensity (0.9) - brightness
- Blur (25) - smoothness

---

## ❗ COMMON PROBLEMS

**Python not found:**
- Install Python with "Add Python to PATH" checked
- Restart computer

**Can't install dependencies:**
- Right-click on `INSTALL.bat` → "Run as administrator"
- Or try: `pip install pynput Pillow numpy mss opencv-python`

**Installation fails on newer Python:**
- Some libraries may not support very new Python versions yet
- Try Python 3.11 or 3.12: https://www.python.org/downloads/
- Or wait for library updates

**Video won't play:**
- Install VLC Player: https://www.videolan.org/
- Or save as AVI format

**App won't start:**
- Open command prompt
- Type: `pip install pynput Pillow numpy mss opencv-python`

---

## ⚙️ REQUIREMENTS

- Windows 10/11
- Python 3.7+ (recommended: 3.11 or 3.12)
- 4 GB RAM
- 500 MB disk space

---

## 📍 INSTALLATION PATHS

**Python:**
```
C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\
```

**Libraries:**
```
C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Lib\site-packages\
```

---

## 💡 TIPS

- Record at least **1000 points** for good heatmaps
- Use **AVI format** for videos
- Default settings work great for most cases
- Move mouse naturally

---

## 🔒 PRIVACY

✅ Everything works locally  
✅ Nothing sent to internet  
✅ Open source code
