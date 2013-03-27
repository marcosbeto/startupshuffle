# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404
from models import launch_users
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponsePermanentRedirect, Http404

def goToURL(request):
    return render_to_response('index.html',{} , context_instance=RequestContext(request))

def saveEmailLaunchPage(request):
    
    if not request.is_ajax():
        return HttpResponse("error") 

    email_str = request.GET["email"]
    startup_name_str = request.GET["startup"]
    
    try: 
        launch_user = launch_users(email=email_str,startup_name=startup_name_str)
        launch_user.save()
        return HttpResponse("sucess") 

    except:
        return HttpResponse("error") 
