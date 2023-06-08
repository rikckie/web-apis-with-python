from flask import Flask
from flask import request
from flask import send_file
from flask import jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL document to find out which filters are available out-of the box
filters_available = [
        "blur",
        "contour",
        "detail",
        "edge-enchance",
        "edge-enchance_more",
        "emboss",
        "sharpen",
        "smooth",
        "smooth_more" ]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    TODO:
    1. Return the usage instructions that specifies which filters are available, and the method format
    """
    response = {
            "filters_available": filters_available,
            "usage": {"http_method":"POST", "URL":"/<filter_available>/"},
            }
    return jsonify(response)

    


@app.post("/<filter>")
def image_filter(filter):
    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error
    2. Check if a file has been provided in the POST request, if not return an error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    if filter not in filters_available:
        return jsonify({"error":"incorrect filter"})
    # GETS THE IMAGE FILE
    file = request.files["image"]
    if not file:
        return jsonify({"error":"no file provided"})
    # APPLY THE IMAGE FILTER
    filtered_image = apply_filter(file, filter)
    return send_file(filtered_image, mimetype="image/JPEG")


if __name__ == "__main__":
    app.run()
    
