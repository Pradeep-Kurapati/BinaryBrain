from django.shortcuts import redirect, render
from blog.models import Blog, Contact

# Create your views here.
def home(request):
    return render(request, "index.html")

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, "bloghome.html", context)

def search(request):
    return render(request, "search.html")

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request, 'blogpost.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        instance = Contact(name=name,email=email,desc=desc)
        instance.save()
        return redirect("home")
    return render(request, "contact.html")
