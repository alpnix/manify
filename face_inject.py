import cv2
import numpy as np
import sys

def detect_face(image):
    """
    Detects a face in an image using Haar cascades.
    
    Returns:
        A tuple (x, y, w, h) of the detected face bounding box,
        or None if no face is detected.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Load the pre-trained Haar cascade for frontal face detection.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        return None
    # You can choose the largest face or simply the first one detected.
    return faces[0]  # (x, y, w, h)

def main():
    face_img_path = "WhatsApp Image 2025-02-08 at 01.25.24.jpeg"
    target_img_path = "1727795420400.jpeg"

    # Load the images
    target_img = cv2.imread(face_img_path)
    face_img = cv2.imread(target_img_path)

    if face_img is None:
        print("Error: Could not load face image from", face_img_path)
        sys.exit(1)
    if target_img is None:
        print("Error: Could not load target image from", target_img_path)
        sys.exit(1)

    # Detect a face in the source (face) image.
    face_box = detect_face(face_img)
    if face_box is None:
        print("Error: No face detected in face image.")
        sys.exit(1)
    (fx, fy, fw, fh) = face_box
    # Crop the face region from the face image.
    face_region = face_img[fy:fy+fh, fx:fx+fw]

    # Detect a face in the target image.
    target_face_box = detect_face(target_img)
    if target_face_box is None:
        print("Error: No face detected in target image.")
        sys.exit(1)
    (tx, ty, tw, th) = target_face_box

    # Resize the face region to match the dimensions of the target face region.
    resized_face = cv2.resize(face_region, (tw, th))

    # Create a mask for the resized face (all white, same size as resized_face).
    mask = 255 * np.ones(resized_face.shape, resized_face.dtype)

    # Determine the center of the target face region for cloning.
    center = (tx + tw // 2, ty + th // 2)

    # Seamlessly clone the resized face into the target image.
    output = cv2.seamlessClone(resized_face, target_img, mask, center, cv2.NORMAL_CLONE)

    # Save the output image.
    output_path = "output_face_injected.jpg"
    cv2.imwrite(output_path, output)
    print("Output saved to", output_path)

    # Optionally display the result.
    cv2.imshow("Face Injection", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
