from django.shortcuts import render
from http import HTTPMethod
from .models import User, Groups, Note, Appointments
from .serializers import UserSerializers, GroupsSerializers, NotesSerializers, AppointmentSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    @action(detail=False, methods=['post'], url_path='login')
    def post_signin(self, request):
        username = request.headers["username"]
        password = request.headers["password"]
        
        user = User.objects.get(username = username)
        if (user is not None):
            if (user.password == password):
                serialize = UserSerializers(user)
                return Response(serialize.data)
            else:
                return Response({'error', ' Invalid Password'}, status=404)
        else:
            return Response({'error', ' User not found'}, status=404)

    @action(detail=False, methods=['post'], url_name='signin')
    def post_login(self, request):
        username = request.headers["username"]
        password = request.headers["password"]
        email = request.headers["email"]
        user = User(username=username, password=password, email=email)
        user.save()
        return Response(status=201)

    @action(detail=False, methods=['patch'], url_path='update')
    def user_update(self, request):
        id = request.headers["id"]
        user = User.objects.get(id = id)
        user.username = request.headers["username"]
        user.password = request.headers["password"]
        user.email = request.headers["email"]
        user.save()
        return Response(status=200)

    @action(detail=False, methods=['get'], url_path='notes')
    def get_notes(self, request):
        user_id = request.headers['user_id']
        notes = Note.objects.filter(user = user_id)
        serialize = NotesSerializers(notes, many=True)
        return Response(serialize.data)
    
class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers

    @action(detail=False, methods=['POST'], url_name='add')
    def group_add(self, request):
        name = request.headers['name']
        userid = request.headers['user-id']
        group = Groups(name = name)
        user = User.objects.get(id = userid)
        group.users.add(user)
        group.save()
        return Response(status=201)

    @action(detail=False, methods=['POST'], url_name='add_user')
    def group_add_user(self, request):
        id = request.headers['id']
        userid = request.headers['user-id']
        group = Groups.objects.get(id = id)
        user = User.objects.get(id = userid)
        group.users.add(user)
        return Response(status=200)
    
    @action(detail=False, methods=['patch'], url_path='update')
    def group_update(self, request):
        id = request.headers["id"]
        group = Groups.objects.get(id = id)
        group.name = request.headers["name"]
        group.save()
        return Response(status=200)
    
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializers

    @action(detail=False, methods=['POST'], url_name='add')
    def note_add(self, request):
        id = request.headers['user-id']
        subject = request.headers['subject']
        subtopic = request.headers['subtopic']
        user = User.objects.get(id = id)
        note = Note(subject = subject, subtopic = subtopic, user = user)
        note.save()
        return Response(status=201)
    
    @action(detail=False, methods=['DELETE'], url_name='delete')
    def note_delete(self, request):
        id = request.headers['id']
        note = Note.objects.get(id = id)
        note.delete()
        return Response(status=200)
    
    @action(detail=False, methods=['PATCH'], url_name='update')
    def note_update(self, request):
        id = request.headers['id']
        userid = request.headers['user-id']
        user = User.objects.get(id = userid)
        note = Note.objects.get(id = id, user = user)
        note.subject = request.headers['subject']
        note.subtopic = request.headers['subjtopic']
        note.save()

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializers
    