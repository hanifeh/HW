# import shutil
# # cv2
# # PIL
# my_image = r'C:\Users\lvlrw\PycharmProjects\test\python.png'
# new_image = r'C:\Users\lvlrw\PycharmProjects\test\python2.png'
# shutil.copy(my_image, new_image)
my_image = open('python.png', 'rb')
new_image = open('python2.png', 'wb')
new_image.write(my_image.read())
new_image.close()
my_image.close()
