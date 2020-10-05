from django.http import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tareas.models import Tareas, TipoTarea, Asignatura, Usuario
from .serializer import TareaSerialize, TipoTareaSerialize, AsignaturaSerialize, Usuario

# Create your views here.
class TareaList(APIView):
    """
       List all surveys, or create a new survey
    """
    def get(self, request, format=None):
        _tareas = Tareas.objects.all()

        serializer = TareaSerialize(_tareas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TareaSerialize(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TareaDetalle(APIView):
    """
      get object tarea by
    """
    def get_object(self, pk):
        try:
            return Tareas.objects.get(pk=pk)
        except Tareas.DoesNotExist:
            raise Http404

    #
    def get(self, request, pk, format=None):
        tarea = self.get_object(pk)

        serializer = TareaSerialize(tarea)
        return Response(serializer.data)

        #

    def put(self, request, pk, format=None):
        _tarea = self.get_object(pk)

        serializer = TareaSerialize(_tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #

    def delete(self, request, pk, format=None):
        _tarea = self.get_object(pk)

        _tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
    TipoTarea 
"""
class TipoTareaLista(APIView):
    def get(self, request, format=None):
        _tipo_tareas = TipoTarea.objects.all()

        serializer = TipoTareaSerialize(_tipo_tareas, many=True)
        return Response(serializer.data)


class TipoTareaDetalle(APIView):
    """
      get  tipotarea by ID
    """
    def get_object(self, pk):
        try:
            return TipoTarea.objects.get(pk=pk)
        except TipoTarea.DoesNotExist:
            raise Http404

    #
    def get(self, request, pk, format=None):
        _tp_tarea = self.get_object(pk)

        serializer = TipoTareaSerialize(_tp_tarea)
        return Response(serializer.data)

"""
    Asignatura 
"""
class AsignaturaLista(APIView):
    def get(self, request, format=None):
        _asignatura = Asignatura.objects.all()

        serializer = AsignaturaSerialize(_asignatura, many=True)
        return Response(serializer.data)


class AsignaturaDetalle(APIView):
    """
      get  Asignatura by ID
    """
    def get_object(self, pk):
        try:
            return Asignatura.objects.get(pk=pk)
        except Asignatura.DoesNotExist:
            raise Http404

    #
    def get(self, request, pk, format=None):
        _asignatura = self.get_object(pk)

        serializer = AsignaturaSerialize(_asignatura)
        return Response(serializer.data)

