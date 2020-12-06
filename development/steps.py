"""Steps in developing a Django application
"""

# Setup

"""
Open a Django project in PyCharm:
    specify one app in Application name
    check Enable Django admin
Add another app (optionally) using:
    manage.py@<project_site>  > startapp <app_label>
Run:
    manage.py@<project_site>  > runserver
    (Tools / Run manage.py Task...)
        click http://127.0.0.1:8000/ 
        open http://127.0.0.1:8000/admin 
Verify / Add the following line in INSTALLED_APPS in settings.py:
    '<app>.apps.<App>Config' (e.g., 'music.apps.MusicConfig')
Specify the database in DATABASES in settings.py (default: sqlite3)
Run:
    manage.py@<project_site>  > makemigrations
    (although it is probably not absolutely necessary at this stage)
Run:
    manage.py@<project_site>  > migrate
    (in order to create some initial database tables)
Create admin superuser:
    manage.py@<project_site>  > createsuperuser
    open http://127.0.0.1:8000/admin
Create the <project_site>/templates/<app> folder for the first <app>
"""

# Development 1

"""
In <app>/views.py, write the simplest index view (returning just HttpResponse("<h1>Hello, world<>/h1")):
    from django.http import HttpResponse
    def index(request):
        return HttpResponse('<h1>Hello, world</h1>')
Add the corresponding URL pattern to <project_site>/urls.py:
    import views.py:
        from <app> import views
    create/update the urlpatterns list:
        urlpatterns += [
	        path('', views.index, name='index')
        ]
Verify that the index view works:
    run:
        manage.py@<project_site>  > runserver 
    again if it was closed after running it for the first time
    open http://localhost:8000/<app>/ (e.g., http://localhost:8000/music/) 
    (you should see "Hello, World!" printed in the browser)
Create the corresponding <app>/urls.py file:
    import views.py:
        from . import views
    create/update the urlpatterns list and 
    move the corresponding URL pattern from <project_site>/urls.py to <app>/urls.py:
        urlpatterns = (+=) [
	        path('', views.index, name='index')
        ]
Include <app>/urls.py in the urlpatterns list of the <project_site>/urls.py:
    path('<app>/', include('<app>.urls'))
Verify again that the index view works.
Redirect (optionally) the root URL of your site (i.e. 127.0.0.1:8000) to 127.0.0.1:8000/<app>/, 
    i.e. make '<app>/' the landing page:
        in <project_site>/urls.py extend the urlpatterns list like this:
            urlpatterns += [
	            path('', RedirectView.as_view(url='music/'))
            ]
Create also (optionally) a class-based index view in <app>/views.py: 
    from django.views import View	
    # alternatively: from django.views.generic import TemplateView
    class IndexView(View):
    # alternatively: class IndexView(TemplateView):
	    def get(self, request, *args, **kwargs):	# override (Template)View.get()
		    return HttpResponse('<h1>Hello, world</h1>')
Modify/Update the corresponding path statement in the urlpatterns list in <urls>.py :
    urlpatterns += [
	    path('', views.IndexView.as_view(), name='index')
    ]
Verify again that the index view works.
Create also (optionally) a modified/improved version of the class-based index view in <app>/views.py, 
    suitable for testing with index0.html, see below:
    from django.views import View	
    # alternatively: from django.views.generic import TemplateView
    class IndexView(View):
    # alternatively: class IndexView(TemplateView):
		# a better option for testing with index0.html, see below:
	    def get(self, request, *args, **kwargs):	# override (Template)View.get()
	        context = {
	            'john': 'John Lennon'
	        }
		    return render(request, 'index0.html', context=context)
Create also (optionally) the simplest index0.html in templates.
Verify again that the index view works.
Create (optionally) the static, static/css, static/images and other directories in the <app> directory 
    to store static files that the <app> might need
Include (really optionally, since it is unnecessary) the call to the static() function in <project_site>/urls.py, 
    in order to enable the serving of static files (CSS, JavaScript, images) during development:
        in <project_site>/urls.py extend the urlpatterns list like this:
            from django.conf import settings
            from django.conf.urls.static import static
            ...
            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
Commit 1
"""

# Development 2

"""
Create the first (simple) model(s) in the <app>/models.py file
    typical fields:
        models.CharField(max_length=<n>)
        models.BooleanField(verbose_name=<verbose name>, 
		    		        choices=<choices_list>, 
		    		        default=<choice from choices_list>,
		    		        ...)
        models.DateField(null=True, blank=True)
        models.TimeField(null=True, blank=True,
		    		     default=datetime.time(hour=<int>, minute=<int>, second=<int>))
        models.ForeignKey(<AnotherModel>,
		                  on_delete=models.SET_NULL,	# CASCADE, SET_DEFAULT,…
		                  null=True, 
		                  blank=True)
        ...
	typical methods:
	    __str__()
        get_absolute_url()		# return reverse('<Model-detail>', args=[str(self.id)])
        ...
Run:
    manage.py@<project_site>  > makemigrations <app>
Run:
    manage.py@<project_site>  > migrate
in order to create those model tables in your database
Run another cycle of change models - makemigrations - migrate whenever you make changes to your model(s) / database
Run (optionally):
    manage.py@<project_site>  > sqlmigrate <app> <migration number> 
    (e.g., manage.py@polls_site  > sqlmigrate polls 0001) 
to see the SQL equivalent of a specific migration
Try some of the frequently used operations on the database:
    in the Python Console, run runfile('console.py')
        copy console.py from https://docs.google.com/document/d/13sU3UgaorntPFxIcOwQsjnZCe9Jp5EVyIebWJDlB7uk/edit
        to the project at the topmost level (where manage.py is);
        after it is run, it enables experimenting with the database of a Django app manually, from the console, 
        by instantiating models and running commands like:
            - <Model>.objects.all() - display all the items of a certain type
            - m = <Model>(<p1>, <p2>,...) - create a new object/item m by instantiating a model class <Model>
                                            (<p1>, <p2>,... - the model field values passed to the <Model> constructor);
                                            for using classmethod instead of __init__() for creating objects, see:
                                            https://docs.djangoproject.com/en/dev/ref/models/instances/#creating-objects
            - save it in the database by calling <object>.save() explicitly
              (you can actually instantiate a model class with an empty constructor (no parameters)
              and then populate its fields with <object>.<field> = <new value>;
              don't forget to <object>.save() everything in the end if you need it saved)
            - <Model>.objects.create() - create a new object/item; no need to <object>.save() afterwords
            - <object>.id or <object>.pk - show the id field of an object
            - <object>.<field> - show the value of another field of the object
            - <object/item>.<field> = <new value> - change the value of an object's field
Register your first model(s) in the /<project_site>/<app>/admin.py file, thus making the <app> modifiable in the admin
    in the <app>/admin.py file enter:
        from django.contrib import admin
        from .models import <Model class 1> [, <Model class 2>, <Model class 3>,...]
        admin.site.register(<Model class 1>)
        [admin.site.register(<Model class 2>)
         admin.site.register(<Model class 3>)
        ...]
    then runserver again, or just refresh the admin site
    repeat these actions for other model classes if needed
Add some database objects in the admin
Add other, custom methods to models as needed and experiment with them in the Python Console to verify that they work
Include the corresponding URL patterns (one path() function per pattern, best using the urlpatterns += [...] syntax) 
in the <app>/urls.py, for the first model(s) created in the previous steps
    note that there can be more than one URL pattern related to a single model 
    (e.g., path('songs/', views.SongListView.as_view(), name='songs'), 
           path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'), etc.)
Develop the corresponding view(s) in the <app>/views.py for the first model(s) created in the previous steps
    the first versions of these views can be rather "low-level", returning HttpResponse(...) or render(...); 
    however, consider using generic display views (such as ListView, DetailView) and 
    generic editing views (such as CreateView, UpdateView, DeleteView,...) right away; 
    in practice, use generic views from the very beginning whenever the corresponding views match them; 
    note that there can be more than one URL pattern and, consequently, more than one view related to a single model 
    (represented by the appropriate subclasses of ListView, DetailView, CreateView, UpdateView, DeleteView,...)
Develop the corresponding template(s) in the <project_site>/templates folder 
for the first model(s) and view(s) created in the previous steps
    create the <project_site>/templates/<app> folder for each <app>
    put the corresponding <app> template(s) in the <project_site>/templates/<app> folder
    accumulate over time and use your own collection of typical, generic templates ("template templates")
Play with the admin site by adding more models and more data items
Customize (optionally) the admin site by including the stuff discussed in 
    https://docs.djangoproject.com/en/dev/intro/tutorial07/#customize-the-admin-form
Commit 2
"""

# Development 3

