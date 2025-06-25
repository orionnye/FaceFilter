from camera import Camera

def main():
    """Main entry point for the camera application."""
    camera = Camera()
    
    # Open camera
    if not camera.open():
        print("Error: Could not open camera")
        return
    
    print("Camera opened successfully!")
    print("Press 'q' or ESC to quit")
    
    try:
        while True:
            # Update camera frame
            if not camera.update_frame():
                print("Error: Failed to capture frame")
                break
            
            # Display the current frame
            camera.display_current_frame()
            
            # Check for quit key
            if camera.check_for_quit_key():
                break
                
    finally:
        camera.close()
        camera.cleanup_display()
        print("Camera closed")

if __name__ == "__main__":
    main() 