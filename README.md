# 🖱️ Mouse Tracker - Desktop Heatmap & Screen Recording

A desktop application for Windows that tracks mouse movements across the entire screen and creates stunning heatmaps with progressive animation.

![Version](https://img.shields.io/badge/version-1.2.0-blue)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- ✅ **Global Mouse Tracking** - Records movements across the entire screen
- 🔥 **Heatmap Generation** - Beautiful color-coded visualization
- 📹 **Progressive Animation** - Heatmap builds gradually with cursor movement
- 💾 **Image Export** - Save heatmaps as PNG/JPG
- 🎬 **Video Export** - Record in AVI/MP4 formats
- ⚙️ **Real-time Settings** - Adjust radius, intensity, and blur on the fly
- 🎨 **Bright Colors** - Enhanced visibility with vibrant gradients

### 🆕 What's New in v1.2

- **Brighter Heatmap Colors** - Increased base opacity from 0% to 50%
- **Enhanced Color Palette** - More vibrant and saturated colors
- **AVI Format Support** - Better compatibility with all video players
- **Automatic Codec Selection** - Chooses best codec based on file format

## 📋 Table of Contents

- [Quick Start (3 Steps)](#-quick-start)
- [How to Use](#-how-to-use)
- [System Requirements](#-system-requirements)
- [Installation Details](#-installation)
- [Settings & Configuration](#-settings--configuration)
- [Video Formats](#-video-formats)
- [Troubleshooting](#-troubleshooting)
- [Technical Details](#-technical-details)
- [FAQ](#-faq)

## 🎬 Video Demo

*Coming soon - watch how it works!*

---

## ⚡ Quick Start (3 Steps)

### For Absolute Beginners

1. **Install Python 3.11**
   - Download: https://www.python.org/downloads/release/python-3118/
   - ⚠️ Check "Add Python to PATH" during installation

2. **Double-click** `INSTALL.bat`
   - Wait for "Installation completed successfully"

3. **Double-click** `START.bat`
   - App will launch automatically!

### Already Have Python?

1. Double-click `INSTALL.bat`
2. Double-click `START.bat`

That's it! 🎉

---

## 🔧 System Requirements

- **OS**: Windows 10/11
- **Python**: 3.11 or 3.12 ⚠️ **DO NOT use Python 3.14** (compatibility issues)
- **RAM**: Minimum 4 GB
- **Disk Space**: ~500 MB (for Python and libraries)
- **Screen**: Any resolution supported

## 📦 Installation

### Step 1: Install Python

⚠️ **IMPORTANT**: Use Python 3.11 or 3.12 (NOT 3.14!)

1. Download **Python 3.11** or **3.12**:
   - Python 3.11: https://www.python.org/downloads/release/python-3118/
   - Python 3.12: https://www.python.org/downloads/release/python-3129/

2. During installation **check** "Add Python to PATH"

3. Install and restart your computer

### Step 2: Install Dependencies

**Easiest Way:**

Just run `INSTALL.bat` - it will:
- ✅ Check Python version
- ✅ Detect already installed packages
- ✅ Install only missing dependencies
- ✅ Verify installation
- ✅ Show clear status

**Alternative Methods:**

- Advanced: `scripts\install_fix.bat`
- Manual: `pip install pynput Pillow numpy mss opencv-python`

**If errors occur**, see [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

### Installation (One-Click)

1. **Download** or clone this repository
2. **Double-click** `INSTALL.bat`
3. Wait for installation to complete

### Run the Application

**Double-click** `START.bat`

That's it! The app will launch automatically.

### Alternative Methods

- Command line: `python mouse_tracker.py`
- Advanced install: `scripts\install_fix.bat`

## 📖 How to Use

### 1️⃣ Start Recording

1. Launch the app (double-click `START.bat`)
2. Click **"▶️ Start Recording"**
3. Confirm the notification (click OK)
4. Move your mouse across the screen
5. Watch the point counter increase

### 2️⃣ Stop Recording

1. Click **"⏹️ Stop"**
2. Review the recording summary

### 3️⃣ View Heatmap

1. Click **"🔥 Show Heatmap"**
2. Heatmap opens in a new window
3. Option to save as image

**Color Scheme:**
- 🔵 **Bright Blue** - Low activity
- 🟢 **Bright Green** - Medium activity
- 🟡 **Bright Yellow** - High activity
- 🔴 **Orange-Red** - Maximum activity (hot zones!)

### 4️⃣ Adjust Heatmap Settings

Use sliders to customize visualization:

- **Point Radius** (20-150 px) - Area of influence (default: 60px)
- **Intensity** (0.1-1.0) - Color brightness (default: 0.9)
- **Blur** (0-50 px) - Smoothness of transitions (default: 25px)

💡 **New**: Points are now significantly brighter and more visible!

### 5️⃣ Record Video

1. Click **"📹 Record Video with Heatmap"**
2. Choose save location and filename
3. Wait for processing (progress shown in status)
4. Video saves automatically

**✨ Special Feature**: Heatmap appears **progressively** with cursor movement!

**Video Settings:**
- Format: AVI (recommended) or MP4
- Duration: 10 seconds
- FPS: 30 frames/second
- Resolution: Matches your screen

⚠️ **Recommendation**: Save as **AVI** for maximum compatibility!

### 6️⃣ Reset

Click **"🔄 Reset"** to clear all data and start a new session

## ⚙️ Settings & Configuration

### Default Settings

```python
Radius: 60 pixels
Intensity: 0.9
Blur: 25 pixels
```

### Customizing in Code

Edit `mouse_tracker.py` to change defaults:

```python
# Line ~34-36
self.heatmap_radius = tk.IntVar(value=60)
self.heatmap_intensity = tk.DoubleVar(value=0.9)
self.heatmap_blur = tk.IntVar(value=25)
```

### Video Settings

```python
# Line ~499-501
fps = 30          # Frames per second (can change to 60)
duration = 10     # Duration in seconds
```

### Color Palette

Current colors (RGB):
- Blue: (0, 100, 255) - Enhanced from (0, 0, 255)
- Green: (0, 255, 100) - Enhanced from (0, 255, 0)
- Yellow: (255, 220, 0) - Enhanced from (255, 255, 0)
- Red: (255, 50, 0) - Enhanced from (255, 0, 0)

## 📹 Video Formats

### AVI (Recommended) ⭐

- **Codec**: XVID
- **Compatibility**: Excellent
- **Quality**: High
- **File Size**: Medium
- **Players**: All

### MP4

- **Codec**: H.264 (avc1) or MP4V
- **Compatibility**: Good
- **Quality**: High
- **File Size**: Smaller
- **Players**: Most (VLC recommended)

### If Video Doesn't Play

**Solution 1** - Install VLC Media Player:
```
https://www.videolan.org/
```

**Solution 2** - Save as AVI format instead

**Solution 3** - Install K-Lite Codec Pack:
```
https://codecguide.com/download_kl.htm
```

## 🐛 Troubleshooting

### Python 3.14 Installation Errors

**Problem**: `KeyError: '__version__'` or `ModuleNotFoundError: No module named 'pynput'`

**Solution**:
1. Uninstall Python 3.14
2. Install Python 3.11: https://www.python.org/downloads/release/python-3118/
3. Run `install_fix.bat`

### "No module named 'pynput'"

```bash
pip install --no-cache-dir pynput
```

### "DLL load failed"

1. Install Visual C++ Redistributable: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Reinstall libraries:
```bash
pip install --force-reinstall opencv-python
```

### Mouse Not Tracking

1. Run as Administrator
2. Add to Windows Defender exclusions
3. Check antivirus settings (might block pynput)

### Video Not Opening

**Cause**: Video player doesn't support the codec

**Solutions**:
1. Use VLC Media Player (opens everything)
2. Save in AVI format instead of MP4
3. Install K-Lite Codec Pack

### Video Not Saving

1. Check folder permissions
2. Ensure enough disk space
3. Try AVI format instead of MP4
4. Use opencv-python-headless:
```bash
pip uninstall opencv-python
pip install opencv-python-headless
```

### Low Heatmap Quality

1. Increase "Point Radius" (50-100)
2. Increase "Intensity" (0.7-1.0)
3. Add "Blur" (15-30)
4. Record more points (move mouse longer)

### Performance Issues

1. Record fewer points (shorter sessions)
2. Decrease radius (30-50px)
3. Close other programs
4. Use SSD for video saving

## 🛠️ Technical Details

### Technology Stack

- **Python 3.11/3.12** - Core language
- **Tkinter** - GUI framework
- **pynput** - Global mouse tracking
- **Pillow (PIL)** - Image processing
- **OpenCV** - Video recording
- **MSS** - Screen capture
- **NumPy** - Data processing

### Algorithm

**Density Map Creation:**
```python
1. Group mouse points into grid cells (20x20px)
2. Count points per cell
3. Normalize density (0-1 scale)
4. Apply color gradient based on density
5. Add Gaussian blur for smoothness
```

**Progressive Animation:**
```python
1. Sort points by timestamp
2. For each frame:
   - Show only points up to current time
   - Generate heatmap for visible points
   - Draw cursor at current position
3. Combine frames into video
```

**Brightness Enhancement:**
```python
alpha = 255 * (0.5 + normalized_density * 0.5) * intensity
# Ensures minimum 50% opacity instead of 0%
```

### File Structure

```
Eye tracker/
├── 📄 README.md              # Main documentation (you are here)
├── 🚀 START.bat              # ONE-CLICK: Launch app
├── 📦 INSTALL.bat            # ONE-CLICK: Install dependencies
├── 🐍 mouse_tracker.py       # Main application
├── 📋 requirements.txt       # Python packages
├── 🚫 .gitignore             # Git exclusions
│
├── 📁 docs/                  # Documentation
│   ├── CHANGELOG.md          # Version history
│   ├── TROUBLESHOOTING.md    # Problem solving
│   ├── QUICK_START.txt       # Quick reference
│   ├── VIDEO_FORMATS_INFO.txt # Video format guide
│   └── HEATMAP_COLORS_INFO.txt # Color guide
│
└── 📁 scripts/               # Installation & utility scripts
    ├── install_fix.bat       # Advanced installer
    ├── install_dependencies.bat # Basic installer
    └── run_tracker.bat       # Alternative launcher
```

### Performance Metrics

| Points | Processing Time | Video Quality |
|--------|----------------|---------------|
| < 1,000 | < 5 sec | Excellent |
| 1,000 - 10,000 | 5-30 sec | Excellent |
| 10,000 - 50,000 | 30-120 sec | Good |
| > 50,000 | 120+ sec | Variable |

## ❓ FAQ

### Q: Can I track mouse clicks separately?

Currently, the app tracks movement only. Click tracking is planned for v2.0.

### Q: Does it work on multiple monitors?

Yes, it tracks the primary monitor. Multi-monitor support is in development.

### Q: Can I change video duration?

Yes, edit line ~501 in `mouse_tracker.py`:
```python
duration = 10  # Change to desired seconds
```

### Q: Is my data sent anywhere?

No! Everything processes locally on your computer. No internet connection needed.

### Q: Can I export data to CSV?

Not yet, but planned for future releases. Currently exports to image and video only.

### Q: What's the maximum recording time?

No limit, but very long recordings (>1 hour) may impact performance.

### Q: Can I use this for commercial projects?

Yes! The project is open-source and free to use commercially.

### Q: Why Python 3.14 doesn't work?

Python 3.14 is very new and some libraries haven't updated yet. Use 3.11 or 3.12.

## 💡 Use Cases

### 1. UX/UI Research
Track how users interact with applications and websites

### 2. Presentations
Create stunning visualizations for demonstrations

### 3. Workflow Analysis
Understand which areas of the screen are used most

### 4. Training & Education
Demonstrate work patterns and processes

### 5. Accessibility Testing
Analyze cursor movement patterns for accessibility improvements

## 🎯 Tips for Best Results

### For Stunning Heatmaps:
- Record minimum 1,000 points
- Use blur: 20-30px
- Set intensity: 0.8-1.0
- Move mouse naturally

### For Detailed Analysis:
- Record 5,000+ points
- Decrease radius: 30-40px
- Lower intensity: 0.6-0.7
- Avoid blur or use minimal

### For Presentations:
- Use default settings (60/0.9/25)
- Record 2,000-5,000 points
- Save as AVI for compatibility
- Add smooth, deliberate movements

### For Quick Tests:
- Record 500-1,000 points
- Increase radius: 70-80px
- High intensity: 1.0
- More blur: 30-40px

## 📊 Version History

### v1.2.0 (2025-11-04)
- ✨ Brighter heatmap colors
- ✨ AVI format support
- 🔧 Auto codec selection
- 📖 Unified documentation

### v1.1.0 (2025-11-04)
- ✨ Progressive heatmap animation
- 🎬 Animated cursor in videos
- 🐛 Bug fixes

### v1.0.0 (2025-11-04)
- 🎉 Initial release
- ✅ Mouse tracking
- ✅ Heatmap generation
- ✅ Video recording

See [CHANGELOG.md](CHANGELOG.md) for detailed history.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgments

Built with:
- [pynput](https://github.com/moses-palmer/pynput) - Mouse event tracking
- [Pillow](https://python-pillow.org/) - Image processing
- [OpenCV](https://opencv.org/) - Video recording
- [MSS](https://python-mss.readthedocs.io/) - Screen capture
- [NumPy](https://numpy.org/) - Numerical operations

## 📞 Support

- **Issues**: Create an issue on GitHub
- **Documentation**: See this README
- **Troubleshooting**: See troubleshooting section above

## 🔮 Roadmap

### v1.3 (Planned)
- [ ] Click heatmap (separate from movement)
- [ ] Export to GIF animation
- [ ] Adjustable video speed
- [ ] Custom duration via GUI

### v2.0 (Future)
- [ ] Multi-monitor support
- [ ] Real-time heatmap display
- [ ] CSV/JSON data export
- [ ] Session comparison
- [ ] Web interface

---

**Made with ❤️ for UX research and user behavior analysis**

**All data is processed locally on your computer - nothing is sent to external servers!**

---

## 🆘 Quick Help

**Can't Install?** → Run `INSTALL.bat` as Administrator

**Installation Issues?** → Try `scripts\install_fix.bat`

**Video Won't Play?** → Use VLC Media Player or save as AVI

**Python 3.14 Problems?** → Downgrade to Python 3.11

**Still Need Help?** → See `docs\TROUBLESHOOTING.md`

---

**Star ⭐ this project if you find it useful!**
