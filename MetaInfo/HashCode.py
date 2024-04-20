import hashlib

def compute_hash(file_path, algorithm="md5"):
    hash_algo = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()



file_path = "img.jpg"
print("MD5:", compute_hash(file_path, "md5"))
print("SHA-1:", compute_hash(file_path, "sha1"))
print("SHA-256:", compute_hash(file_path, "sha256"))



file_path = "imgCopy.jpg"
print("MD5:", compute_hash(file_path, "md5"))
print("SHA-1:", compute_hash(file_path, "sha1"))
print("SHA-256:", compute_hash(file_path, "sha256"))




# https://www.microsoft.com/en-us/PhotoDNA     
# In 2009, Microsoft in collaboration with Dartmouth College developed PhotoDNA. PhotoDNA uses hash technology but with the added ability that it 'recognises' when an image has been edited so still assigns it the same hash value.
# Thus for above two images, it must give same hash code