import exif

orig_im = exif.Image('img.jpg')

def check_exif(img):
    if img.has_exif:
        print("The image contains EXIF information")
    else:
        print("EXIF info not found")    
        
check_exif(orig_im)   
print(dir(orig_im))   

print(orig_im.get('datetime_original'))  