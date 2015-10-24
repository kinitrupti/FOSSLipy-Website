from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    
class ServicesPage(generic.TemplateView):
    template_name = "services.html"
    
class ProjectsPage(generic.TemplateView):
    template_name = "projects.html"
    
class ClientsPage(generic.TemplateView):
    template_name = "clients.html"
    
class ContactsPage(generic.TemplateView):
    template_name = "contacts.html"            
    
class PythonPage(generic.TemplateView):
    template_name = "python.html"                

class PhpPage(generic.TemplateView):
    template_name = "php.html"              
    
class LatexPage(generic.TemplateView):
    template_name = "latex.html"                      
