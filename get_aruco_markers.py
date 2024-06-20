import cv2
print(cv2.__version__)
import cv2.aruco as aruco

def process_camera(cap, outfile):
    # Define Charuco dictionary
    arucoDict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
    arucoParams = aruco.DetectorParameters()
    arucodetector = aruco.ArucoDetector(detectorParams=arucoParams, dictionary=arucoDict)
    # charuco_board = aruco.CharucoBoard_create(5, 7, 1, .8, aruco_dict)

    # Create Charuco board
    # charuco_board = aruco.CharucoBoard( 5, 7, 1, .8, aruco_dict)



    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        corners_rgb, ids_rgb, rejected_rgb = arucodetector.detectMarkers(image=frame)
        print(f"{ids_rgb = }")
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect markers
        corners_gry, ids_gry, rejected_gry = arucodetector.detectMarkers(image=gray)
        print(f"{ids_gry = }")
    

        if ids_rgb is not None:
            # Draw detected markers on the frame
            aruco.drawDetectedMarkers(frame, corners_rgb, ids_rgb)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        outfile.write(frame)

        # Break the loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    outfile.release()
    cv2.destroyAllWindows()


video_filename = 'any_video_name.mp4'
stream = cv2.VideoCapture(video_filename)
# stream = cv2.VideoCapture(1)
if stream.isOpened():
    print('Video is loaded')

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
# if index is 1, invert width and height
width, height = (480, 640)
file_to_save = video_filename.replace('.mp4', '_pose_qr.mp4')
outfile = cv2.VideoWriter(file_to_save, fourcc, 24.0, (width, height))

# Load a model
process_camera(stream, outfile)