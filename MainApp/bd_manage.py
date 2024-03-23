from .models import *


def getAllMovies() -> list:
    res = []
    for obj in Movie.objects.all():
        res.append({"id": obj.id, "title": obj.title,
                    "year": obj.year, "director": obj.director.fio,
                    "length": str(obj.length), "rating": obj.rating})
    return res


def getMovie(movieID) -> dict:
    res = {}
    try:
        obj = Movie.objects.get(id=movieID)

        res = {"id": obj.id, "title": obj.title,
                    "year": obj.year, "director": obj.director.fio,
                    "length": str(obj.length), "rating": obj.rating}
    except Movie.DoesNotExist:
        pass

    return res


def addMovie(movie):
    try:
        Movie.objects.create(id=movie["id"], title=movie["title"],
                             year=movie["year"], director=Director.objects.get(id=movie["director"]),
                             length=movie["length"], rating=movie["rating"])
        movie["director"] = Director.objects.get(id=movie["director"]).fio

        return movie, ""
    except Exception as exc:
        return None, str(exc)


def changeMovie(movieID, movie):
    try:
        Movie.objects.get(id=movieID)
    except Movie.DoesNotExist:
        return None, "Not found"
    try:
        Movie.objects.filter(id=movieID).update(id=movieID, title=movie["title"],
                                                year=movie["year"], director=Director.objects.get(id=movie["director"]),
                                                length=movie["length"], rating=movie["rating"])
        movie["director"] = Director.objects.get(id=movie["director"]).fio

        return movie, ""
    except Exception as exc:
        return None, str(exc)


def deleteMovie(movieID):
    try:
        Movie.objects.get(id=movieID)
    except Movie.DoesNotExist:
        return "Not found"
    try:
        Movie.objects.filter(id=movieID).delete()
        return ""
    except Exception as exc:
        return str(exc)


def getAllDirectors() -> list:
    res = []
    for obj in Director.objects.all():
        res.append({"id": obj.id, "fio": obj.fio})
    return res


def getDirector(directorID) -> dict:
    res = {}
    try:
        obj = Movie.objects.get(id=directorID)

        res = {"id": obj.id, "fio": obj.fio}
    except Director.DoesNotExist:
        pass

    return res


def addDirector(director):
    try:
        Director.objects.create(id=director["id"], title=director["fio"])

        return director, ""
    except Exception as exc:
        return None, str(exc)


def changeDirector(directorID, director):
    try:
        Director.objects.get(id=directorID)
    except Director.DoesNotExist:
        return None, "Not found"
    try:
        Director.objects.filter(id=directorID).update(id=directorID, fio=director["fio"])
        return director, ""
    except Exception as exc:
        return None, str(exc)


def deleteDirector(directorID):
    try:
        Director.objects.get(id=directorID)
    except Director.DoesNotExist:
        return "Not found"
    try:
        Director.objects.filter(id=directorID).delete()
        return ""
    except Exception as exc:
        return str(exc)

