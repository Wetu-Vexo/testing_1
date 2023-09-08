import os
import time
import cv2 as cv

videopath = 0
duration = 15 * 60  # 15 minutes in seconds

cap = cv.VideoCapture(videopath)
save_video = "video.avi"

# If save_video exists, create a file with a new name+1
if os.path.exists(save_video):
    i = 1
    while os.path.exists(save_video):
        save_video = f"video{i}.avi"
        i += 1

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter(save_video, fourcc, 20, (width, height))

start_time = time.time()

while True:
    ret, frame = cap.read()
    if ret:
        writer.write(frame)

    # Check for the duration and exit the loop
    if int(time.time() - start_time) >= duration:
        break

    # Check for the 'q' key to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv.destroyAllWindows()
