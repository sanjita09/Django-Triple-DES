from django.shortcuts import render,redirect
from .forms import EncryptForm,DecryptForm
from Crypto.Cipher import DES3
import os
import string
from django.core.files import File
from django.core.files.base import ContentFile
import base64
from PIL import Image
from .models import Image



#Encrypt file method
def Encrypt_file(key,in_file,chunk_size=16*1024):
    key=bytes(str(key),'utf-8')

    #Creating a random intialization vector
    iv=os.urandom(8)
    print(f'Intialization vector is {iv}')
    print()
    encryptor=DES3.new(key,DES3.MODE_CBC,iv)

    #Writing the intialization vector into the output file
    with in_file.open() as image:
        with open("encoded\image.inc",'wb')as outfile:
            outfile.write(iv)
            while True:
                chunk=image.read(chunk_size)
                if len(chunk)==0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
                chunkd=encryptor.encrypt(chunk)
                chunkd=base64.b64encode(chunkd).decode()              
                
def home(request):
    return render(request,'home.html')

def encrypt(request):
    if request.method=="POST":
        form=EncryptForm(request.POST,request.FILES)
        if form.is_valid():
            key=form.cleaned_data.get("key")
            image=request.FILES['image']
            title=form.cleaned_data.get('title')
            Encrypt_file(key,image,chunk_size=16*1024)
            return redirect('/encrypt_complete')
    else:
        form=EncryptForm()   
    return render(request,'encrypt.html',{'form':form})


def encrypt_complete(request):
    return render(request,'encrypt_complete.html',{
    })


def decrypt(request):
    if request.method=="POST":
        form=DecryptForm(request.POST,request.FILES)
        if form.is_valid():
            key=form.cleaned_data.get("key")
            encfile=request.FILES['Encoded_file']
            title=form.cleaned_data.get('title')
        
        chunk_size=16*1024    
        with encfile.open() as infile:
            iv=infile.read(8)

            decryptor=DES3.new(key,DES3.MODE_CBC,iv)

            with open("uploads\image.jpg",'wb') as outfile:
                while True:
                    chunk=infile.read(chunk_size)
                    if len(chunk)==0:
                        break
                    plaintext=decryptor.decrypt(chunk)
                    outfile.write(plaintext)
            obj=Image.objects.create(image=os.path.abspath(outfile.name))      
            return render(request,'decrypt_complete.html',{
        'object':obj,
        'title':title,
        'path':os.path.abspath(outfile.name)
    })
    else:
        form=DecryptForm()   
    return render(request,'encrypt.html',{'form':form})
