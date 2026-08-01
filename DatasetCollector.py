import cv2
import os
import time

# ---- Config ----
label = 'J'  # Change this to the letter/phrase you’re collecting
samples = 1000
save_path = f'dataset/{label}'
os.makedirs(save_path, exist_ok=True)

# ---- Init ----
cap = cv2.VideoCapture(0)
count = 0
auto_capture = False
capture_delay = 0.005  # seconds between auto captures
last_capture_time = time.time()

print(f"[INFO] Collecting label: {label}")
print("Press 'c' to toggle auto-capture ON/OFF")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # ROI box
    x1, y1, x2, y2 = 100, 100, 500, 500
    roi = frame[y1:y2, x1:x2]
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display info
    status_text = "Auto-Capture: ON" if auto_capture else "Auto-Capture: OFF"
    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255), 2)
    cv2.putText(frame, f"Samples: {count}/{samples}", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2)

    cv2.imshow("Dataset Collector", frame)
    key = cv2.waitKey(1)

    # Toggle auto-capture
    if key == ord('c'):
        auto_capture = not auto_capture
        print(f"[INFO] Auto-capture {'ENABLED' if auto_capture else 'DISABLED'}")

    # Quit
    elif key == ord('q') or count >= samples:
        break

    # Auto capture logic
    if auto_capture and (time.time() - last_capture_time) > capture_delay:
        img_name = f"{save_path}/{count}.jpg"
        cv2.imwrite(img_name, roi)
        count += 1
        last_capture_time = time.time()
        print(f"Saved: {img_name}")

cap.release()
cv2.destroyAllWindows()
print(f"[INFO] Finished collecting {count} samples for label: {label}")