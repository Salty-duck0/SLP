from PIL import Image

def image_info(file_path):
    try:
        with Image.open(file_path) as img:
            print("Image Format:", img.format)
            print("Image Mode:", img.mode)
            print("Image Size:", img.size)
            print("Image Palette:", img.palette)
            print("Image Info:", img.info)
    except Exception as e:
        print("Error:", e)

image_path = "img_notDocFormat.jpg"
image_info(image_path)

image_path = "img.jpg"
image_info(image_path)
