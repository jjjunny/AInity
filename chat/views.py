from django.shortcuts import render

def room(request, room_name):
    return render(request, 'chat/../templates/board_home/room.html', {
        'room_name': room_name
    })