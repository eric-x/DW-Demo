#from django.core import serializers
from django.http import HttpResponse#, Http404
#from django.shortcuts import render
import simplejson

from p.models import Store, AccessPoint


def json_resp(func):
    def func_wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        print resp
        #data = serializers.serialize('json', resp)
        data = simplejson.dumps(resp)
        return HttpResponse(data, content_type='application/json')
    return func_wrapper


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

@json_resp
def all_aps(request, store_id):
    data = []
    try:
        s = Store.objects.get(id=store_id)
        if s:
            aps = s.accesspoint_set.all()
            return [{'nick':x.nick, 'status':x.status} for x in aps]
    except Store.DoesNotExist:
        return data

@json_resp
def ap_status(request, store_id, ap_nick):
    try:
        s = Store.objects.get(id=store_id)
        if s:
            aps = s.accesspoint_set.get(nick=ap_nick)
            if aps:
                return {'status': aps.status}
    except Store.DoesNotExist:
        return {'status': 0}
    except AccessPoint.DoesNotExist:
        return {'status': 0}
    return {'status': 0}

@json_resp
def update_ap_status(request, store_id, ap_nick, status):
    try:
        s = Store.objects.get(id=store_id)
        if s:
            aps = s.accesspoint_set.get(nick=ap_nick)
            if aps:
                aps.status = status
                s.save()
                return {'status': aps.status}
    except Store.DoesNotExist:
        return {'status': 0}
    except AccessPoint.DoesNotExist:
        return {'status': 0}
    return {'status': 0}
