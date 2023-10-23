from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib import messages


color_codes = {
    1: "#FF5733",
    2: "#00FF00",
    3: "#0000FF",
    4: "#FFFF00",
    5: "#FFA500",
    6: "#800080",
    7: "#FFC0CB",
    8: "#40E0D0",
    9: "#A52A2A",
    10: "#808080",
    11: "#E6E6FA",
    12: "#00FFFF",
    13: "#4B0082",
    14: "#FFD700",
    15: "#008080"
}



def index(request):
    return render(request, "generate/index.html")


def avatar_input(request, seed):
    user_input = seed
    ascii_sum = sum(ord(char) for char in user_input)
    color = ascii_sum % 15 + 1
    eye = ascii_sum % 10 + 1
    mouth = ascii_sum % 11
    final_svg = avatar(color, eye, mouth)
    return render(request, "generate/random.html", {'avatar_svg': final_svg})


# Generate random hexadecimal color value
def generate_random_hex_color():  
        color = "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color


# function to generate the svg given eyes and mouth
def avatar(color, eye , mouth):
    
    eye_path = f"generate/eyes/{eye}.svg"
    with open(eye_path, "r") as eye_file:
            eye_svg = eye_file.read()

    mouth_path = f"generate/mouth/{mouth}.svg"
    with open(mouth_path, "r") as mouth_file:
            mouth_svg = mouth_file.read()
    
    color_svg = color_codes[color]
    
    final_svg = f"""
    <svg width="256" height="256" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="256" height="256" fill="{color_svg}"/>
        {eye_svg}
        {mouth_svg}
    </svg>
    """  
    return final_svg
    

# generate random avatar
def random_avatar(request):
    # Generate a random number between 1 and 10 (inclusive)
    random_color = random.randint(1,15)
    random_eye = random.randint(1, 10)
    random_mouth = random.randint(1,10)
    final_svg = avatar(random_color,random_eye , random_mouth)
    return render(request, "generate/random.html", {'avatar_svg': final_svg})



# signup
def signup(request):
      if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  login(request,user)
                  return redirect("login")
      else :
            form = UserCreationForm()
      return render(request, "generate/signup.html", {"form" : form})

# login
def login_view(request):
    if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request,username = username, password=password)
          if user is not None:
                login(request,user)
                return redirect("index")
          else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'generate/login.html')      