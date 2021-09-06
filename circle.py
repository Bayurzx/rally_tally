import cv2
import numpy as np

# Read image.
img = cv2.imread('images.jfif', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
gray_blurred = cv2.blur(gray, (4, 4))

detected_circles = cv2.HoughCircles(gray,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=28, minRadius=1, maxRadius=20)

print(f'The number of pipes are: {len(detected_circles[0])}')

# Draw circles that are detected.
if detected_circles is not None:

    # Detect the parameters a, b and r.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Add a dot to circle.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)
