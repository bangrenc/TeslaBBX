from django.db import models
import sys,os

#collect current directory
def cur_file_dir():
    path=sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

class UploadFile(models.Model):
    FileDir=cur_file_dir()
    File=models.FileField(upload_to=FileDir)

    def __str__(self):
        return self.File

'''
class Data(models.Model):
    PN=models.CharField(max_length = 30)
    SN=models.CharField(max_length = 30)
    ECC=models.CharField(max_length = 30)
'''     
