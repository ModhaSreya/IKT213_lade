import cv2
import os

output_dir = os.path.expanduser("~/IKT213_lastname/assignment_1/solutions")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "camera_outputs.txt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Get camera properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    with open(output_file, "w") as f:
        f.write(f"fps: {int(fps)}\n")
        f.write(f"height: {int(height)}\n")
        f.write(f"width: {int(width)}\n")

    print(f"Camera information saved to {output_file}")
cap.release()
