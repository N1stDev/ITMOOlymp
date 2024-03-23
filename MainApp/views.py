from django.http import HttpResponse, HttpRequest, JsonResponse
from .bd_manage import *
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse(content="OK", status=200)

@csrf_exempt
def movies(request: HttpRequest):
    if request.method == "GET":
        moviesList = getAllMovies()
        return JsonResponse(status=200, data={"list": moviesList})
    elif request.method == "POST":
        data = json.loads(request.body.decode())["movie"]
        movieObj, err = addMovie(data)
        if not err:
            return JsonResponse(status=200, data={"movie": movieObj})
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})

@csrf_exempt
def movie(request: HttpRequest, id):
    if request.method == "GET":
        movieObj = getMovie(int(id))
        if movieObj:
            return JsonResponse(status=200, data={"movie": movieObj})
        else:
            return HttpResponse(status=404, content="Not found")
    elif request.method == "PATCH":
        data = json.loads(request.body.decode())["movie"]
        movieObj, err = changeMovie(int(id), data)
        if not err:
            return JsonResponse(status=200, data={"movie": movieObj})
        elif err == "Not found":
            return HttpResponse(status=404, content="Not Found")
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})

    elif request.method == "DELETE":
        err = deleteMovie(int(id))
        if not err:
            return HttpResponse(status=202, content="Accepted")
        elif err == "Not found":
            return HttpResponse(status=404, content="Not Found")
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})


@csrf_exempt
def directors(request: HttpRequest):
    if request.method == "GET":
        directorsList = getAllDirectors()
        return JsonResponse(status=200, data={"list": directorsList})
    elif request.method == "POST":
        data = json.loads(request.body.decode())["director"]
        directorObj, err = addDirector(data)
        if not err:
            return JsonResponse(status=200, data={"director": directorObj})
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})

@csrf_exempt
def director(request: HttpRequest, id):
    if request.method == "GET":
        directorObj = getDirector(int(id))
        if directorObj:
            return JsonResponse(status=200, data={"director": directorObj})
        else:
            return HttpResponse(status=404, content="Not found")
    elif request.method == "PATCH":
        data = json.loads(request.body.decode())["director"]
        directorObj, err = changeDirector(int(id), data)
        if not err:
            return JsonResponse(status=200, data={"director": directorObj})
        elif err == "Not found":
            return HttpResponse(status=404, content="Not Found")
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})

    elif request.method == "DELETE":
        err = deleteDirector(int(id))
        if not err:
            return HttpResponse(status=202, content="Accepted")
        elif err == "Not found":
            return HttpResponse(status=404, content="Not Found")
        else:
            return JsonResponse(status=500, data={"status": 500, "reason": err})





