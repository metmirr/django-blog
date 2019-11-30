from django.shortcuts import render


posts = [
    {
        "author": "Metin Demir",
        "content": "First post content",
        "title": "Blog Post 1",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Suleyman Akan",
        "content": "Second post content",
        "title": "Blog Post 2",
        "date_posted": "August 28, 2018",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context=context)


def about(request):
    return render(request, "blog/about.html")
