from django.shortcuts import render
from Students_app import models as studentModels


# Create your views here.
def main_view(request):
    user_info = studentModels.User.objects.get(id=request.user.id)

    return render(request, 'chat_app/chat.html', context={'user_info': user_info})
