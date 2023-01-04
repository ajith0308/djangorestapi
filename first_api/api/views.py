from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User 
from .serilazear import IteamSerilazear

@api_view(["GET"])
def getData(request):
   Users=User.objects.all()
   serilerzer=IteamSerilazear(Users,many=True)
   return Response(serilerzer.data)

@api_view(["POST"])
def putdata(request):
    serizerdata=IteamSerilazear(data=request.data)
    if serizerdata.is_valid():
        serizerdata.save()
    return Response(serizerdata.data)
