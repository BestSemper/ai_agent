from langchain_core.tools import tool
import cv2
import time

@tool
def capture_image() -> str:
    """Capture an image from the webcam and save it to a file."""
    # Create a video capture object and specify camera ID (0 for default webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
    else:
        time.sleep(0.5)
        # Capture a single frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if ret:
            # Save the captured image to a file
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured and saved as 'captured_image.jpg'")
        else:
            print("Error: Failed to capture frame.")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()
    return "Image captured and saved as 'captured_image.jpg'"

capture_image.func()