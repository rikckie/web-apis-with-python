from PIL import Image
from PIL import ImageFilter
import io


def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """
    # Open the as an PIL Image object
    image = Image.open(file)
    # 3. Apply the filter
    image = image.filter(eval(f"ImageFilter.{filter.upper()}"))
    # 4. Convert the PIL Image object to file object
    # creates a new/empty bytes 'file' object
    file = io.BytesIO()
    # save the 'image' to the new 'file' object as 'JPEG'
    image.save(file, "JPEG")
    file.seek(0)
    # 5. Return the file object
    return file

