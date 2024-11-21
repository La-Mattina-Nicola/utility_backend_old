from .models import User, Groups, Note, Appointments
from rest_framework import serializers

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'subject', 'subtopic']

class UserSerializers(serializers.ModelSerializer):
    notes = NotesSerializers(many = True)
    class Meta:
        model = User
        fields = ['id', 'username', 'notes']

class GroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'

class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'