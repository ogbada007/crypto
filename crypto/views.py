from django.shortcuts import render

# Create your views here.
def home(request):
    """Renders the index page."""
    return render(request, 'crypto/index.html')

def news(request):
    """Renders the news html page."""
    return render(request, 'crypto/blog.html')

def about(request):
    """Renders the about html page."""
    return render(request, 'crypto/about.html')

def signin(request):
    """Renders the signin page."""
    return render(request, 'crypto/signin.html')

def signup(request):
    """Renders the signup page."""
    return render(request, 'crypto/signup.html')