"""
Mouse Tracker Desktop Application
Mouse tracking for Windows with screen recording and heatmap generation
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
from datetime import datetime
from pynput import mouse
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import mss
import cv2
import os
from collections import defaultdict

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Mouse Tracker - Desktop")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Tracking data
        self.is_tracking = False
        self.is_recording_video = False
        self.mouse_points = []
        self.start_time = None
        self.elapsed_time = 0
        
        # Heatmap settings (increased for brightness)
        self.heatmap_radius = tk.IntVar(value=60)
        self.heatmap_intensity = tk.DoubleVar(value=0.9)
        self.heatmap_blur = tk.IntVar(value=25)
        
        # Mouse listener
        self.mouse_listener = None
        
        # Screen resolution
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            self.screen_width = monitor["width"]
            self.screen_height = monitor["height"]
        
        # Video
        self.video_writer = None
        self.video_path = None
        
        # Screen frames storage during tracking
        self.screen_frames = []  # List of (timestamp, frame_image) tuples
        self.is_capturing_screen = False
        
        self.setup_ui()
        self.update_timer()
    
    def setup_ui(self):
        """Create user interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg="#667eea", height=100)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🖱️ Mouse Tracker",
            font=("Segoe UI", 24, "bold"),
            bg="#667eea",
            fg="white"
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Mouse tracking across the entire computer screen",
            font=("Segoe UI", 11),
            bg="#667eea",
            fg="white"
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status panel
        status_frame = tk.LabelFrame(main_frame, text="Status", font=("Segoe UI", 12, "bold"), padx=15, pady=15)
        status_frame.pack(fill=tk.X, pady=(0, 15))
        
        status_grid = tk.Frame(status_frame)
        status_grid.pack()
        
        # Status
        tk.Label(status_grid, text="Status:", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky=tk.W, padx=5)
        self.status_label = tk.Label(status_grid, text="Ready", font=("Segoe UI", 10), fg="#10b981")
        self.status_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        # Points
        tk.Label(status_grid, text="Points recorded:", font=("Segoe UI", 10, "bold")).grid(row=0, column=2, sticky=tk.W, padx=(20, 5))
        self.points_label = tk.Label(status_grid, text="0", font=("Segoe UI", 10, "bold"), fg="#667eea")
        self.points_label.grid(row=0, column=3, sticky=tk.W, padx=5)
        
        # Time
        tk.Label(status_grid, text="Recording time:", font=("Segoe UI", 10, "bold")).grid(row=0, column=4, sticky=tk.W, padx=(20, 5))
        self.time_label = tk.Label(status_grid, text="00:00", font=("Segoe UI", 10, "bold"), fg="#667eea")
        self.time_label.grid(row=0, column=5, sticky=tk.W, padx=5)
        
        # Resolution information
        resolution_frame = tk.Frame(main_frame, bg="#f3f4f6", padx=10, pady=10)
        resolution_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            resolution_frame,
            text=f"📺 Screen resolution: {self.screen_width} x {self.screen_height} pixels",
            font=("Segoe UI", 10),
            bg="#f3f4f6"
        ).pack()
        
        # Control buttons
        buttons_frame = tk.LabelFrame(main_frame, text="Control", font=("Segoe UI", 12, "bold"), padx=15, pady=15)
        buttons_frame.pack(fill=tk.X, pady=(0, 15))
        
        btn_grid = tk.Frame(buttons_frame)
        btn_grid.pack()
        
        self.start_btn = tk.Button(
            btn_grid,
            text="▶️ Start Recording",
            command=self.start_tracking,
            font=("Segoe UI", 11, "bold"),
            bg="#667eea",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.start_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.stop_btn = tk.Button(
            btn_grid,
            text="⏹️ Stop",
            command=self.stop_tracking,
            font=("Segoe UI", 11, "bold"),
            bg="#ef4444",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_btn.grid(row=0, column=1, padx=5, pady=5)
        
        self.show_heatmap_btn = tk.Button(
            btn_grid,
            text="🔥 Show Heatmap",
            command=self.show_heatmap,
            font=("Segoe UI", 11, "bold"),
            bg="#8b5cf6",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.show_heatmap_btn.grid(row=1, column=0, padx=5, pady=5)
        
        self.record_btn = tk.Button(
            btn_grid,
            text="📹 Record Video with Heatmap",
            command=self.record_video,
            font=("Segoe UI", 11, "bold"),
            bg="#10b981",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.record_btn.grid(row=1, column=1, padx=5, pady=5)
        
        self.reset_btn = tk.Button(
            btn_grid,
            text="🔄 Reset",
            command=self.reset,
            font=("Segoe UI", 11, "bold"),
            bg="#f59e0b",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.reset_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Heatmap Settings
        settings_frame = tk.LabelFrame(main_frame, text="Heatmap Settings", font=("Segoe UI", 12, "bold"), padx=15, pady=15)
        settings_frame.pack(fill=tk.BOTH, expand=True)
        
        # Radius
        radius_frame = tk.Frame(settings_frame)
        radius_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(radius_frame, text="Point radius:", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.radius_value_label = tk.Label(radius_frame, text=f"{self.heatmap_radius.get()} px", font=("Segoe UI", 10, "bold"), fg="#667eea")
        self.radius_value_label.pack(side=tk.RIGHT)
        
        radius_slider = tk.Scale(
            settings_frame,
            from_=20,
            to=150,
            orient=tk.HORIZONTAL,
            variable=self.heatmap_radius,
            command=lambda v: self.radius_value_label.config(text=f"{int(float(v))} px")
        )
        radius_slider.pack(fill=tk.X, pady=(0, 10))
        
        # Intensity
        intensity_frame = tk.Frame(settings_frame)
        intensity_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(intensity_frame, text="Intensity:", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.intensity_value_label = tk.Label(intensity_frame, text=f"{self.heatmap_intensity.get():.1f}", font=("Segoe UI", 10, "bold"), fg="#667eea")
        self.intensity_value_label.pack(side=tk.RIGHT)
        
        intensity_slider = tk.Scale(
            settings_frame,
            from_=0.1,
            to=1.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.heatmap_intensity,
            command=lambda v: self.intensity_value_label.config(text=f"{float(v):.1f}")
        )
        intensity_slider.pack(fill=tk.X, pady=(0, 10))
        
        # Blur
        blur_frame = tk.Frame(settings_frame)
        blur_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(blur_frame, text="Blur:", font=("Segoe UI", 10)).pack(side=tk.LEFT)
        self.blur_value_label = tk.Label(blur_frame, text=f"{self.heatmap_blur.get()} px", font=("Segoe UI", 10, "bold"), fg="#667eea")
        self.blur_value_label.pack(side=tk.RIGHT)
        
        blur_slider = tk.Scale(
            settings_frame,
            from_=0,
            to=50,
            orient=tk.HORIZONTAL,
            variable=self.heatmap_blur,
            command=lambda v: self.blur_value_label.config(text=f"{int(float(v))} px")
        )
        blur_slider.pack(fill=tk.X)
    
    def on_mouse_move(self, x, y):
        """Mouse movement handler"""
        if self.is_tracking:
            self.mouse_points.append({
                'x': x,
                'y': y,
                'timestamp': time.time()
            })
            self.points_label.config(text=str(len(self.mouse_points)))
    
    def start_tracking(self):
        """Start mouse tracking"""
        self.is_tracking = True
        self.mouse_points = []
        self.screen_frames = []  # Clear previous frames
        self.start_time = time.time()
        self.is_capturing_screen = True
        
        self.status_label.config(text="Recording...", fg="#f59e0b")
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.show_heatmap_btn.config(state=tk.DISABLED)
        self.record_btn.config(state=tk.DISABLED)
        
        # Start mouse listener
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.mouse_listener.start()
        
        # Start screen capture in separate thread
        screen_thread = threading.Thread(target=self._capture_screen_thread)
        screen_thread.daemon = True
        screen_thread.start()
        
        messagebox.showinfo(
            "Recording Started",
            "Mouse tracking is active!\n\n"
            "Move your mouse across the screen.\n"
            "Press 'Stop' when you're done."
        )
    
    def stop_tracking(self):
        """Stop tracking"""
        self.is_tracking = False
        self.is_capturing_screen = False  # Stop screen capture
        
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None
        
        self.status_label.config(text="Recording stopped", fg="#10b981")
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        
        if len(self.mouse_points) > 0:
            self.show_heatmap_btn.config(state=tk.NORMAL)
            self.record_btn.config(state=tk.NORMAL)
            messagebox.showinfo(
                "Recording Complete",
                f"Recorded {len(self.mouse_points)} points!\n\n"
                "Now you can:\n"
                "• Show Heatmap\n"
                "• Record Video with Heatmap"
            )
        else:
            messagebox.showwarning("No Data", "No points were recorded")
    
    def generate_heatmap(self, background_image=None):
        """Generate heatmap"""
        if len(self.mouse_points) == 0:
            return None
        
        # Create base image
        if background_image is None:
            # Take screenshot of current screen
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                screenshot = sct.grab(monitor)
                background_image = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        
        # Create heatmap layer
        heatmap_layer = Image.new('RGBA', (self.screen_width, self.screen_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(heatmap_layer)
        
        # Create density map
        cell_size = 20
        density_map = defaultdict(int)
        
        for point in self.mouse_points:
            cell_x = int(point['x'] / cell_size)
            cell_y = int(point['y'] / cell_size)
            density_map[(cell_x, cell_y)] += 1
        
        # Maximum density
        max_density = max(density_map.values()) if density_map else 1
        
        # Draw points with color gradient
        radius = self.heatmap_radius.get()
        intensity = self.heatmap_intensity.get()
        
        for (cell_x, cell_y), density in density_map.items():
            x = cell_x * cell_size + cell_size // 2
            y = cell_y * cell_size + cell_size // 2
            
            normalized_density = density / max_density
            # Increase brightness: minimum 50%, maximum 100%
            alpha = int(255 * (0.5 + normalized_density * 0.5) * intensity)
            
            # Color gradient: blue -> green -> yellow -> red (bright colors)
            if normalized_density < 0.25:
                color = (0, 100, 255, alpha)  # Bright blue
            elif normalized_density < 0.5:
                color = (0, 255, 100, alpha)  # Bright green
            elif normalized_density < 0.75:
                color = (255, 220, 0, alpha)  # Bright yellow
            else:
                color = (255, 50, 0, alpha)  # Bright red/orange
            
            # Draw circle
            bbox = [x - radius, y - radius, x + radius, y + radius]
            draw.ellipse(bbox, fill=color)
        
        # Apply blur
        blur_amount = self.heatmap_blur.get()
        if blur_amount > 0:
            heatmap_layer = heatmap_layer.filter(ImageFilter.GaussianBlur(blur_amount))
        
        # Overlay heatmap on background
        result = background_image.copy()
        result.paste(heatmap_layer, (0, 0), heatmap_layer)
        
        return result
    
    def show_heatmap(self):
        """Show heatmap in new window"""
        self.status_label.config(text="Generating Heatmap...", fg="#8b5cf6")
        self.root.update()
        
        heatmap_image = self.generate_heatmap()
        
        if heatmap_image:
            # Resize image for display
            display_width = 1200
            display_height = int(self.screen_height * (display_width / self.screen_width))
            heatmap_image_resized = heatmap_image.resize((display_width, display_height), Image.Resampling.LANCZOS)
            
            # Save temporary file
            temp_path = "temp_heatmap.png"
            heatmap_image_resized.save(temp_path)
            
            # Open image
            heatmap_image_resized.show()
            
            self.status_label.config(text="Heatmap shown", fg="#10b981")
            
            # Ask to save
            if messagebox.askyesno("Save Heatmap", "Would you like to save the heatmap as an image?"):
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")],
                    initialfile=f"heatmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                )
                if save_path:
                    heatmap_image.save(save_path)
                    messagebox.showinfo("Saved", f"Heatmap saved to:\n{save_path}")
    
    def record_video(self):
        """Record screen video with heatmap"""
        if len(self.mouse_points) == 0:
            messagebox.showwarning("No Data", "No data available for video recording")
            return
        
        # Choose save path
        save_path = filedialog.asksaveasfilename(
            defaultextension=".avi",
            filetypes=[
                ("AVI Video (recommended)", "*.avi"),
                ("MP4 Video", "*.mp4"),
                ("All Files", "*.*")
            ],
            initialfile=f"mouse_tracker_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
        )
        
        if not save_path:
            return
        
        self.video_path = save_path
        self.is_recording_video = True
        self.status_label.config(text="Recording video...", fg="#f59e0b")
        self.record_btn.config(state=tk.DISABLED)
        
        # Start recording in separate thread
        thread = threading.Thread(target=self._record_video_thread)
        thread.daemon = True
        thread.start()
    
    def generate_progressive_heatmap(self, background_image, points_subset):
        """Generate heatmap for subset of points (for animation)"""
        if len(points_subset) == 0:
            return background_image.copy()
        
        # Create heatmap layer
        heatmap_layer = Image.new('RGBA', (self.screen_width, self.screen_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(heatmap_layer)
        
        # Create density map
        cell_size = 20
        density_map = defaultdict(int)
        
        for point in points_subset:
            cell_x = int(point['x'] / cell_size)
            cell_y = int(point['y'] / cell_size)
            density_map[(cell_x, cell_y)] += 1
        
        # Maximum density
        max_density = max(density_map.values()) if density_map else 1
        
        # Draw points with color gradient
        radius = self.heatmap_radius.get()
        intensity = self.heatmap_intensity.get()
        
        for (cell_x, cell_y), density in density_map.items():
            x = cell_x * cell_size + cell_size // 2
            y = cell_y * cell_size + cell_size // 2
            
            normalized_density = density / max_density
            # Increase brightness: minimum 50%, maximum 100%
            alpha = int(255 * (0.5 + normalized_density * 0.5) * intensity)
            
            # Color gradient (bright colors)
            if normalized_density < 0.25:
                color = (0, 100, 255, alpha)  # Bright blue
            elif normalized_density < 0.5:
                color = (0, 255, 100, alpha)  # Bright green
            elif normalized_density < 0.75:
                color = (255, 220, 0, alpha)  # Bright yellow
            else:
                color = (255, 50, 0, alpha)  # Bright red/orange
            
            bbox = [x - radius, y - radius, x + radius, y + radius]
            draw.ellipse(bbox, fill=color)
        
        # Apply blur
        blur_amount = self.heatmap_blur.get()
        if blur_amount > 0:
            heatmap_layer = heatmap_layer.filter(ImageFilter.GaussianBlur(blur_amount))
        
        # Overlay heatmap on background
        result = background_image.copy()
        result.paste(heatmap_layer, (0, 0), heatmap_layer)
        
        return result
    
    def _capture_screen_thread(self):
        """Capture screen frames during tracking"""
        fps = 30
        frame_delay = 1.0 / fps
        
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            
            while self.is_capturing_screen:
                current_time = time.time()
                screenshot = sct.grab(monitor)
                frame_image = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
                
                # Store frame with timestamp
                self.screen_frames.append({
                    'timestamp': current_time,
                    'frame': frame_image
                })
                
                # Limit memory usage - keep only last 10 seconds worth of frames
                max_frames = fps * 10
                if len(self.screen_frames) > max_frames:
                    self.screen_frames = self.screen_frames[-max_frames:]
                
                time.sleep(frame_delay)
    
    def _get_frame_at_time(self, target_time):
        """Get the closest frame to target_time from recorded frames"""
        if len(self.screen_frames) == 0:
            # Fallback: capture current screen
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                screenshot = sct.grab(monitor)
                return Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        
        # Find closest frame by timestamp
        closest_frame = self.screen_frames[0]
        min_diff = abs(self.screen_frames[0]['timestamp'] - target_time)
        
        for frame_data in self.screen_frames:
            diff = abs(frame_data['timestamp'] - target_time)
            if diff < min_diff:
                min_diff = diff
                closest_frame = frame_data
        
        return closest_frame['frame'].copy()
    
    def _record_video_thread(self):
        """Thread for recording video with real-time screen and heatmap"""
        try:
            # Video settings
            fps = 30
            frame_delay = 1.0 / fps  # Time between frames
            
            # Sort points by time
            sorted_points = sorted(self.mouse_points, key=lambda p: p['timestamp'])
            
            if len(sorted_points) == 0:
                raise Exception("No points recorded")
            
            # Calculate time range - use actual tracking duration exactly
            start_time = sorted_points[0]['timestamp']
            end_time = sorted_points[-1]['timestamp']
            total_duration = end_time - start_time
            
            # Slow down video by 20% - increase duration by 20%
            # Video duration is 20% longer than tracking duration
            if total_duration < 0.1:
                duration = 1.0 * 1.2  # Minimum 1.2 seconds if duration is too short
            else:
                duration = total_duration * 1.2  # Slow down by 20% (multiply by 1.2)
            
            # Time scale is always 1.0 for perfect synchronization
            time_scale = 1.0
            
            total_frames = int(fps * duration)
            
            # Determine codec based on file extension
            file_ext = os.path.splitext(self.video_path)[1].lower()
            
            if file_ext == '.avi':
                # For AVI use XVID (good compatibility)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
            else:
                # For MP4 try different codecs
                # Try H.264 (avc1), if it doesn't work - use mp4v
                try:
                    fourcc = cv2.VideoWriter_fourcc(*'avc1')
                    # Test writer for verification
                    test_writer = cv2.VideoWriter(
                        'test_codec.mp4',
                        fourcc,
                        fps,
                        (self.screen_width, self.screen_height)
                    )
                    if test_writer.isOpened():
                        test_writer.release()
                        if os.path.exists('test_codec.mp4'):
                            os.remove('test_codec.mp4')
                    else:
                        # If avc1 doesn't work, use mp4v
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                except:
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            
            # Create VideoWriter
            video_writer = cv2.VideoWriter(
                self.video_path,
                fourcc,
                fps,
                (self.screen_width, self.screen_height)
            )
            
            # Check if creation was successful
            if not video_writer.isOpened():
                raise Exception("Failed to create video file. Try saving in AVI format.")
            
            # Record video with exact time mapping
            # Use recorded screen frames from during tracking, not current screen
            for frame_num in range(total_frames):
                # Calculate current time in video (seconds) - based on video duration
                current_video_time = (frame_num / fps) if fps > 0 else 0
                
                # Map video time to tracking time - slow down by 20%
                # Video is 20% longer, so we need to map video time to actual tracking time
                if duration > 0 and total_duration > 0:
                    # Calculate progress through video (0.0 to 1.0)
                    video_progress = min(1.0, current_video_time / duration)
                    # Map to tracking time - video is slower, so same progress = less tracking time
                    # Since duration = total_duration * 1.2, we need to scale back
                    tracking_time = start_time + (video_progress * total_duration)
                elif duration > 0:
                    # If total_duration is 0, use video time directly
                    tracking_time = start_time + current_video_time
                else:
                    tracking_time = start_time
                
                # Clamp to end time
                if tracking_time > end_time:
                    tracking_time = end_time
                
                # Find points up to this time
                points_so_far = [p for p in sorted_points if p['timestamp'] <= tracking_time]
                
                # Get screen frame from recorded frames at this time
                # This uses frames captured DURING tracking, not current screen
                current_screen = self._get_frame_at_time(tracking_time)
                
                # Generate heatmap for points up to current time
                if len(points_so_far) > 0:
                    frame = self.generate_progressive_heatmap(current_screen, points_so_far)
                else:
                    frame = current_screen.copy()
                
                draw = ImageDraw.Draw(frame)
                
                # Find cursor position at this time - use direct interpolation
                cursor_x = None
                cursor_y = None
                
                if len(sorted_points) > 0:
                    # Find the two points to interpolate between
                    point_before = None
                    point_after = None
                    
                    for i, p in enumerate(sorted_points):
                        if p['timestamp'] <= tracking_time:
                            point_before = p
                            if i + 1 < len(sorted_points):
                                point_after = sorted_points[i + 1]
                        else:
                            if i > 0:
                                point_before = sorted_points[i - 1]
                                point_after = p
                            break
                    
                    if point_before:
                        if point_after and point_after['timestamp'] > tracking_time:
                            # Interpolate between two points
                            time_diff = point_after['timestamp'] - point_before['timestamp']
                            if time_diff > 0:
                                t = (tracking_time - point_before['timestamp']) / time_diff
                                t = max(0, min(1, t))  # Clamp between 0 and 1
                                cursor_x = int(point_before['x'] + (point_after['x'] - point_before['x']) * t)
                                cursor_y = int(point_before['y'] + (point_after['y'] - point_before['y']) * t)
                            else:
                                cursor_x = int(point_before['x'])
                                cursor_y = int(point_before['y'])
                        else:
                            cursor_x = int(point_before['x'])
                            cursor_y = int(point_before['y'])
                    
                    # Draw cursor if we have position - make it very visible
                    if cursor_x is not None and cursor_y is not None:
                        # Large, visible cursor
                        cursor_size = 20
                        # Outer circle
                        draw.ellipse([cursor_x-cursor_size, cursor_y-cursor_size, cursor_x+cursor_size, cursor_y+cursor_size], 
                                   fill='red', outline='white', width=3)
                        # Inner circle
                        draw.ellipse([cursor_x-cursor_size//2, cursor_y-cursor_size//2, cursor_x+cursor_size//2, cursor_y+cursor_size//2], 
                                   fill='yellow', outline='black', width=2)
                        # Crosshair
                        crosshair_len = cursor_size * 2
                        draw.line([cursor_x-crosshair_len, cursor_y, cursor_x+crosshair_len, cursor_y], 
                                fill='white', width=3)
                        draw.line([cursor_x, cursor_y-crosshair_len, cursor_x, cursor_y+crosshair_len], 
                                fill='white', width=3)
                        
                        # Add time indicator near cursor
                        time_text = f"{current_video_time:.1f}s"
                        draw.text((cursor_x + 30, cursor_y - 30), time_text, fill='white', stroke_width=2, stroke_fill='black')
                
                # Convert to OpenCV format
                frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
                video_writer.write(frame_cv)
                
                # Update progress every 10 frames to avoid UI lag
                if frame_num % 10 == 0:
                    progress_pct = int((frame_num / total_frames) * 100) if total_frames > 0 else 0
                    self.root.after(0, lambda p=progress_pct: self.status_label.config(
                        text=f"Recording video... {p}%"
                    ))
            
            video_writer.release()
            
            # Completion
            self.root.after(0, self._video_recording_complete)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Recording Error",
                f"An error occurred while recording video:\n{str(e)}"
            ))
            self.root.after(0, lambda: self.status_label.config(text="Recording error", fg="#ef4444"))
            self.is_recording_video = False
    
    def _video_recording_complete(self):
        """Video recording completion"""
        self.is_recording_video = False
        self.status_label.config(text="Video recorded", fg="#10b981")
        self.record_btn.config(state=tk.NORMAL)
        
        messagebox.showinfo(
            "Video Ready",
            f"Video successfully saved!\n\n{self.video_path}"
        )
        
        # Offer to open folder
        if messagebox.askyesno("Open Folder", "Open folder with video?"):
            os.startfile(os.path.dirname(self.video_path))
    
    def reset(self):
        """Reset all data"""
        if self.is_tracking:
            self.stop_tracking()
        
        self.mouse_points = []
        self.start_time = None
        self.elapsed_time = 0
        
        self.status_label.config(text="Ready", fg="#10b981")
        self.points_label.config(text="0")
        self.time_label.config(text="00:00")
        
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.show_heatmap_btn.config(state=tk.DISABLED)
        self.record_btn.config(state=tk.DISABLED)
    
    def update_timer(self):
        """Update timer"""
        if self.is_tracking and self.start_time:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        
        self.root.after(1000, self.update_timer)
    
    def on_closing(self):
        """Handle window closing"""
        if self.is_tracking:
            if messagebox.askyesno("Exit", "Recording is still active. Stop and exit?"):
                self.stop_tracking()
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    root = tk.Tk()
    app = MouseTrackerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()

