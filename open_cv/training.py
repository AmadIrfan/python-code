import cv2

img=cv2.imread('img.png')

cv2.imshow('this is my image ',img)
k=cv2.waitKey(0)
if k== 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('Amad.png',img)
# def imgReader():
#     my_img = cv2.imread("img.png", 0)
#     cv2.imshow("image", my_img)
#     k = cv2.waitKey()
#     if k == 27:
#         cv2.destroyAllWindows()
#     elif k == ord("s"):
#         cv2.imwrite("my_bw_img.png", my_img)


# def videoRecorder():
#     video = cv2.VideoCapture(0)
#     if not video.isOpened():
#         print("error")

#     while True:
#         retValue, frame = video.read()
#         cFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow("my video", cFrame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     video.release()
#     cv2.destroyAllWindows()


# videoRecorder()
