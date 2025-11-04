# 🖱️ Mouse Tracker - Project Information

## 📊 Project Overview

**Name**: Mouse Tracker  
**Version**: 1.2.0  
**Type**: Desktop Application  
**Platform**: Windows 10/11  
**Language**: Python 3.11/3.12  
**License**: MIT  

## 🎯 Purpose

Track mouse movements across the entire screen and generate beautiful heatmaps with progressive animation for UX research, presentations, and workflow analysis.

## 📁 Project Structure

```
Eye tracker/
│
├── 🚀 START.bat              ← DOUBLE-CLICK TO RUN
├── 📦 INSTALL.bat            ← DOUBLE-CLICK TO INSTALL
├── 📖 HOW_TO_USE.txt         ← Quick guide
├── 📄 README.md              ← Full documentation
├── 🔧 PROJECT_INFO.md        ← This file
│
├── 🐍 mouse_tracker.py       ← Main application
├── 📋 requirements.txt       ← Python dependencies
├── 🚫 .gitignore             ← Git configuration
│
├── 📁 docs/                  ← All documentation
│   ├── README.md             ← Docs index
│   ├── CHANGELOG.md          ← Version history
│   ├── TROUBLESHOOTING.md    ← Problem solving  
│   ├── QUICK_START.txt       ← Quick reference
│   ├── SUCCESS_INSTALLATION.txt
│   ├── README_DESKTOP.md     ← Desktop version docs
│   ├── VIDEO_FORMATS_INFO.txt
│   └── HEATMAP_COLORS_INFO.txt
│
└── 📁 scripts/               ← Utility scripts
    ├── README.md             ← Scripts index
    ├── install_fix.bat       ← Advanced installer
    ├── install_dependencies.bat
    └── run_tracker.bat       ← Alternative launcher
```

## 🎯 User-Friendly Features

### One-Click Installation
- `INSTALL.bat` - Checks existing dependencies, installs only what's missing
- Automatic verification
- Clear error messages
- No technical knowledge required

### One-Click Launch
- `START.bat` - Verifies setup and launches app
- Auto-checks dependencies
- User-friendly error messages

### Organized Documentation
- All docs in `/docs` folder
- Quick reference: `HOW_TO_USE.txt`
- Advanced: `README.md`
- Problems: `docs/TROUBLESHOOTING.md`

### Smart Installers
- Detect already installed packages
- Skip unnecessary downloads
- Show installation progress
- Verify after installation

## 🔧 Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Core** | Python 3.11/3.12 | Main language |
| **GUI** | Tkinter | User interface |
| **Tracking** | pynput | Mouse events |
| **Graphics** | Pillow (PIL) | Image processing |
| **Video** | OpenCV | Video recording |
| **Screen** | MSS | Screenshots |
| **Math** | NumPy | Calculations |

## 📈 Key Features

### ✅ Implemented (v1.2.0)
- Global mouse tracking
- Real-time point counter
- Heatmap generation
- Progressive video animation
- Bright color palette
- Multiple video formats (AVI/MP4)
- Adjustable settings
- Image export (PNG/JPG)

### 🔄 In Progress
- Documentation consolidation
- Smart dependency checking
- User-friendly installers

### 🔮 Planned (Future Versions)
- Click heatmap (separate from movement)
- Multi-monitor support
- GIF export
- CSV/JSON data export
- Web interface
- Real-time preview

## 📊 Version History

### v1.2.0 (Current)
- Brighter heatmap colors
- AVI format support
- Smart installers
- Organized file structure

### v1.1.0
- Progressive heatmap animation
- Animated cursor in videos

### v1.0.0
- Initial release
- Basic tracking and heatmap

## 🎨 Design Philosophy

### Simplicity First
- One-click installation
- One-click launch
- Clear instructions
- Minimal user interaction required

### Progressive Disclosure
- `HOW_TO_USE.txt` - Quick start
- `README.md` - Complete guide
- `docs/` - Advanced topics

### Smart Defaults
- Optimized settings out of the box
- Auto-detection of environment
- Graceful error handling

## 👥 Target Users

### Primary
- UX Researchers
- UI/UX Designers
- Product Managers
- Accessibility Testers

### Secondary
- Presenters/Educators
- Workflow Analysts
- Student Researchers

## 💻 Development

### Prerequisites
- Python 3.11 or 3.12
- Windows 10/11
- 500MB free space

### Setup for Development
```bash
git clone <repo>
cd "Eye tracker"
INSTALL.bat
```

### Running Tests
```bash
python mouse_tracker.py
```

### Building Distribution
```bash
# Option 1: PyInstaller
pyinstaller --onefile --windowed mouse_tracker.py

# Option 2: Distribute as-is with installers
```

## 📝 Contributing

See `README.md` for contribution guidelines.

## 🐛 Reporting Issues

1. Check `docs/TROUBLESHOOTING.md` first
2. Search existing issues
3. Create detailed bug report
4. Include:
   - Python version
   - Error messages
   - Steps to reproduce

## 📄 License

MIT License - Free for personal and commercial use.

## 🙏 Credits

### Libraries
- pynput by Moses Palmer
- Pillow Python Imaging Library
- OpenCV Computer Vision
- MSS Screen Capture
- NumPy Scientific Computing

### Inspiration
Built to make UX research easier and more visual.

## 📞 Contact & Support

- **Documentation**: See `README.md`
- **Quick Help**: See `HOW_TO_USE.txt`
- **Troubleshooting**: See `docs/TROUBLESHOOTING.md`

---

**Last Updated**: November 4, 2025  
**Maintained**: Active  
**Status**: Production Ready ✅

---

*Making mouse tracking simple and beautiful* 🖱️✨

