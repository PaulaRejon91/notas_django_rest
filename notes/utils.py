#Funciones para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) 

from rest_framework.response import Response 
from .models import Note 
from .serializers import NoteSerializer #

# This function will return the notes list
def getNotesList(request): 
    #toma como objeto request(solicitud http)
    notes = Note.objects.all().order_by('-update')
    #consulta a la base de datos utilizando el modelo Note. 
    #Note.objects.all() obtiene todas las instancias del modelo Note 
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# This function will return the note detail
def getNoteDetail(request,pk):
    notes=Note.objects.get(id=pk) #?
    serializer=NoteSerializer(notes, many=False)
    return Response(serializer.data)

# This function will update a note
def updateNote(request,pk):
    data=request.data #?
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# This function will delete a note
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')



