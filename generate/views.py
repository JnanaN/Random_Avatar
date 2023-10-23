from django.shortcuts import render
import random
from django.http import HttpResponse
import base64
# Create your views here.


def index(request):
    # Generate a random number between 1 and 10 (inclusive)
    random_eye = random.randint(1, 10)
    random_mouth = random.randint(1,6)

    def generate_random_hex_color():
        # Generate random hexadecimal color value
        color = "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color

    # Generate and print a random hex color
    random_color = generate_random_hex_color()

    eye_path = f"generate/eyes/{random_eye}.svg"
    with open(eye_path, "r") as eye_file:
            eye = eye_file.read()

    mouth_path = f"generate/mouth/{random_mouth}.svg"
    with open(mouth_path, "r") as mouth_file:
            mouth = mouth_file.read()
    final_svg = f"""
    <svg width="256" height="256" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="256" height="256" fill="{random_color}"/>
        {eye}
        {mouth}
    </svg>
    """
    # encoded_svg = base64.b64encode(final_svg.encode()).decode()

    # return render(request, "generate/index.html", {'avatar_svg': encoded_svg})

    return render(request, "generate/index.html", {'avatar_svg': final_svg})



        