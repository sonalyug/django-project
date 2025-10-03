from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

# Display all blog entries
def blog_list(request):
    blogs = Blog.objects.all()  # Fetch all Blog records from the database
    return render(request, 'blog/blog_list.html', {'blogs': blogs})  # Pass blogs to the template

# Create a new blog entry
def blog_create(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()           # Get title from form data
        description = request.POST.get('description', '').strip()  # Get description from form
        if title and description:
            Blog.objects.create(title=title, description=description)  # Save new Blog to DB
            return redirect('blog_list')  # Redirect to blog list page after creation
        # Optional: Add error handling when form data is missing
    return render(request, 'blog/blog_create.html')  # Show the create form on GET request

# View details of a single blog entry by primary key
def blog_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  # Get Blog or 404 if not found
    return render(request, 'blog/blog_view.html', {'blog': blog})  # Display blog details

# Edit an existing blog entry by primary key
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  # Get Blog or 404
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title and description:
            blog.title = title         # Update title
            blog.description = description  # Update description
            blog.save()                # Save changes to database
            return redirect('blog_list')  # Redirect after saving
        # Optional: Add error handling for missing data
    return render(request, 'blog/blog_edit.html', {'blog': blog})  # Show edit form on GET request

# Confirm and delete a blog entry by primary key
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  # Get Blog or 404
    if request.method == "POST":
        blog.delete()           # Delete blog record
        return redirect('blog_list')  # Redirect to blog list after delete
    return render(request, 'blog/blog_delete.html', {'blog': blog})  # Show confirmation form on GET
