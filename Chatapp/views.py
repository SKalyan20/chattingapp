from django.shortcuts import render,redirect
from Chatapp.models import Room,Message

# Create your views here.
#create room views
def createroom(request):
    if request.method=='POST':
        username=request.POST['username']
        room=request.POST['room']
        try:
            get_room=Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room=Room(room_name=room)
            new_room.save()
        return redirect('room',room_name=room,username=username)
    return render(request,'index.html')

#message view
def messageview(request,room_name,username):
    get_room=Room.objects.get(room_name=room_name)
    get_messages=Message.objects.filter(room=get_room)
    
    context={
        'messages':get_messages,
        'user':username,
        'room_name':room_name,
        
        
    }
    
    return render(request,'_message.html',context)