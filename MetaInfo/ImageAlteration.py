import imagehash
from PIL import Image

def compute_image_hash(image_path):
    try:
        with Image.open(image_path) as img:
            return imagehash.average_hash(img)
    except Exception as e:
        print("Error computing hash:", e)
        return None

def verify_image_alteration(original_path, saved_path):
    original_hash = compute_image_hash(original_path)
    saved_hash = compute_image_hash(saved_path)
    
    if original_hash is None or saved_hash is None:
        print("Error: Unable to compute image hashes.")
        return False
    
    if original_hash == saved_hash:
        print("Image is unaltered.")
        return True
    else:
        print("Image has been altered.")
        return False

# Example usage:
original_image_path = "img.jpg"
saved_image_path = "imgCopy.jpg"
verify_image_alteration(original_image_path, saved_image_path)
