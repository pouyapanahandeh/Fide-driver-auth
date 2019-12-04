

# # 从mysql读取图片到本地
# import pymysql
# import sys
#
# conn = pymysql.connect(host='localhost',user='root',passwd='ruirui123',db='image')
# cursor = conn.cursor()
# cursor.execute("SELECT image FROM user_info")
# fout = open('/Users/pingguo/Desktop/Software Tech/identification_recognization/outputs/result.png','wb')
# records = cursor.fetchone()
# fout.write(records[0])
# fout.close()
# cursor.close()
# conn.close()
# import pymysql
# from pymysql import MySQLError
# from configparser import ConfigParser
#
#
# def write_file(data, filename):
#     # Convert binary data to proper format and write it on Hard Disk
#     with open(filename, 'wb') as file:
#         file.write(data)
#
#
# def read_blob(filename):
#     # select photo column of a specific author
#     query = "SELECT image FROM user_info where id=11 "
#
#     try:
#         # query blob data form the authors table
#         conn = pymysql.connect(host='localhost', user='root', passwd='ruirui123', db='image')
#         cursor = conn.cursor()
#         cursor.execute(query)
#         photo = cursor.fetchone()[0]
#
#         # write blob data into a file
#         write_file(photo, filename)
#         print("Success!")
#
#     except MySQLError as e:
#         print(e)
#
#     finally:
#         cursor.close()
#         conn.close()
#
#
# if __name__ == '__main__':
#     read_blob('/Users/pingguo/Desktop/Software Tech/identification_recognization/immmmmmmmmmmmm.jpg')

#
import pymysql
import sys
from PIL import Image
import base64
from io import StringIO, BytesIO
import PIL.Image

conn = pymysql.connect(host='localhost',user='root',passwd='ruirui123',db='image')
filename = 'Selfie.jpg'
image = Image.open(filename)
print(image.size)
blob_value = open(filename, 'rb').read()
sql = 'INSERT INTO user_info(username, password,image) VALUES(1,2,%s)'
args = (blob_value, )
cursor = conn.cursor()
cursor.execute(sql,args)
sql1='select * from user_info where id = 64'
conn.commit()
cursor.execute(sql1)
data=cursor.fetchall()[0]
print (data[3])
file_like=BytesIO(data[3])
print(file_like)
img = Image.open(data[3],'r')
# img.save('testtewffad.png','PNG')
# img.show()
# img = img.convert("RGB")
# img.save("test.jpg")

conn.close()


import pymysql
import base64
import io

import PIL.Image
# from six import BytesIO
#
# with open('/Users/pingguo/Desktop/Software Tech/identification_recognization/data/Card_test.jpg','rb') as f:
#     photo = f.read()
#
# encodestring = base64.b64encode(photo)
# conn = pymysql.connect(host='localhost',user='root',passwd='ruirui123',db='image')
# mycursor=conn.cursor()
# sql = "insert into user_info(image) values(%s)"
# mycursor.execute(sql,(encodestring,))
# conn.commit()
# sql1="select image from user_info"
# mycursor.execute(sql1)
# data = mycursor.fetchone()
# data1=base64.b64decode(data[0])
# # image = PIL.Image.open(data1)
# image = PIL.Image.open(BytesIO(data1))
# image.show()
# image = image.convert("RGB")
# image.save("testtttttttttttttttt.jpg")
# conn.close()
#
# # This portion is part of my test code
# byteImgIO = io.BytesIO()
# byteImg = Image.open("some/location/to/a/file/in/my/directories.png")
# byteImg.save(byteImgIO, "PNG")
# byteImgIO.seek(0)
# byteImg = byteImgIO.read()


# Non test code
# dataBytesIO = io.BytesIO(byteImg)
# Image.open(dataBytesIO)
