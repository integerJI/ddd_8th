from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
import string, random
import json

def index(request):
    return render(request, 'index.html')

def list(request):
    response = {}
    
    body = request.body.decode('utf8')
    data = json.loads(body)

    list_data = [1,2,3,4]

    response["result"] = "true"
    response["status_code"] = "200"
    response["message"] = "성공!"
    response["return_url"] = "/"
    response["data"] = list_data

    return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})

# class CreateInvitationView(View):
#     def get(self, request):
#         return render(request, 'create.html')

#     def post(self, request):
#         response = {}
        
#         body = request.body.decode('utf8')
#         data = json.loads(body)

#         invitation = Invitation()

#         invitation.invi_key = create_key()
#         invitation.invi_title = data['invi_title']
#         invitation.invi_input_date = timezone.datetime.now()
#         invitation.invi_content = data['invi_content']

#         invitation.save()

#         response["result"] = "true"
#         response["status_code"] = "200"
#         response["message"] = "성공!"
#         response["return_url"] = "/"

#         return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})

# def create_key():
#     chars = ''.join([string.ascii_letters, string.digits])

#     invitation_key = ''.join([random.SystemRandom().choice(chars) for i in range(10)])

#     return invitation_key

# def detail(request, invi_key):
#     invi_detail = get_object_or_404(Invitation, invi_key=invi_key)
#     return render(request, 'detail.html', {'invi': invi_detail})
