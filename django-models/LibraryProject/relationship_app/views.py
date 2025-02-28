from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Librarian, UserProfile
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, permission_required

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the context
        context = super().get_context_data(**kwargs)
        # Add the list of books for this library
        context['books'] = self.object.books.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
UserCreationForm()

@user_passes_test
def check_role(role):
    def role_check(user):
        if not user.is_authenticated:
            return False
        try:
            user_profile = user.userprofile
            return user_profile.role == role
        except UserProfile.DoesNotExist:
            return False
    return user_passes_test(role_check)

@check_role('Admin')
@permission_required('relationship_app.can_add_book', raise_exception=True)
def admin_view(request):
    if request.method == 'POST':
        # Example: Add a new book (simplified)
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        author, created = Author.objects.get_or_create(name=author_name)
        Book.objects.create(title=title, author=author)
        return redirect('booklist')
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin! Add a Book:'})

@check_role('Librarian')
@permission_required('relationship_app.can_change_book', raise_exception=True)
def librarian_view(request):
    if request.method == 'POST':
        # Example: Edit a book (simplified)
        book_id = request.POST.get('book_id')
        new_title = request.POST.get('new_title')
        book = get_object_or_404(Book, pk=book_id)
        book.title = new_title
        book.save()
        return redirect('booklist')
    books = Book.objects.all()
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian! Edit a Book:', 'books': books})

@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})