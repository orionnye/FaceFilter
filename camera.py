import cv2

class Camera:
    def __init__(self, camera_index=0, window_name="Live Camera Feed"):
        """Initialize camera with given index and window name"""
        self.camera_index = camera_index
        self.window_name = window_name
        self.cap = None
        self.is_opened = False
        self.current_frame = None
    
    def open(self):
        """Open the camera and return success status"""
        self.cap = cv2.VideoCapture(self.camera_index)
        self.is_opened = self.cap.isOpened()
        return self.is_opened
    
    def update_frame(self):
        """Update the current frame. Returns success status"""
        if not self.is_opened or self.cap is None:
            return False
        
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
        return ret
    
    def get_current_frame(self):
        """Get the current stored frame"""
        return self.current_frame
    
    def display_current_frame(self):
        """Display the current frame in the window"""
        if self.current_frame is not None:
            cv2.imshow(self.window_name, self.current_frame)
    
    def check_for_quit_key(self):
        """Check for quit key presses. Returns True if should quit"""
        key = cv2.waitKey(1) & 0xFF
        return key == ord('q') or key == 27  # 'q' or ESC key
    
    def cleanup_display(self):
        """Clean up display windows"""
        cv2.destroyAllWindows()
    
    def close(self):
        """Close the camera and clean up resources"""
        if self.cap is not None:
            self.cap.release()
            self.is_opened = False
        self.current_frame = None
    
    def __enter__(self):
        """Context manager entry"""
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close() 