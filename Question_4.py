import re

def is_generic_image(image_url):
    generic_patterns = [
        r".*height=[2-4][0-9][0-9]&width=17[0-9][0-9]"
    ]
    return any(re.search(pattern, image_url) for pattern in generic_patterns)

image_url = "https://cdn.mathpix.com/cropped/2025_04_01_7b93083882288e619e6bg-01.jpg?height=332&width=1787&top"

if is_generic_image(image_url):
    x = 1
else:
    x = 0

print(x)
