from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
from TeslaApp.models import UploadFile
import sys,os

#collect current directory
def cur_file_dir():
    path=sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

class UserForm(forms.Form):
    file=forms.FileField()

def BBXData(request):
    if request.method=="POST":
        uf=UserForm(request.POST,request.FILES)
        if uf.is_valid():
            f=uf.cleaned_data['file']
            UF=UploadFile()
            UF.File=f
            filename=str(UF.File)
            UF.save()
            
            file0=cur_file_dir()
            file1=os.path.join(file0,filename)
            file2=os.path.join(file0,'result.log')
            f0=open(file2,'a+')
            f1=open(file1,'r')
            f2=open(file1,'r')
            f3=open(file1,'r')
            
            #PN
            for Line0 in f1:
                if ': 900' in Line0:
                    loc=Line0.index(': 900')
                    f0.write('PN:')
                    f0.write(Line0[(loc+2):(loc+20)]) #collect the current PN location between 'loc+2' and 'loc+20'
                    f0.write('<br>')
                    break
            
            #SN
            for Line1 in f2:
                if ': 032' in Line1:
                    #the location of *032*
                    loc=Line1.index(': 032')
                    f0.write('SN:')
                    f0.write(Line1[(loc+2):(loc+15)]) #collect the current SN location between 'loc+2' and 'loc+15'
                    f0.write('<br>')
                    break
            
            #ECC
            for Line2 in f3:
                if 'ECC    ' in Line2 and 'Disable' in Line2:
                    f0.write('ECC Mode: Disable\n')
                elif 'ECC    ' in Line2:
                    f0.write('ECC Mode: Enable\n')
                    f0.write('<br>')
            
            f0.close()
            f1.close()
            f2.close()
            f3.close()
            
            R=open(file2,'r')
            ReadResult=R.read()
            R.close()
            
            os.remove(file1)
            os.remove(file2)
            
            return HttpResponse(ReadResult)
        
    else:
        uf=UserForm()
    return render_to_response('show.html',{'uf':uf})



# Create your views here.
