from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Vehicle, Tasks
from snippets.serializers import VehicleSerializer, TasksSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer


@api_view(['GET', 'POST'])
def getMachinesLocation(request):
    return JsonResponse({"coordinates": [55.7963846, 37.536643],
                         'markers': [
                             {
                                 'coordinates': [55.8072856, 37.536643],
                                 'machine_name': 'Car 1',
                                 'task_status_cd': 'FAIL',
                                 'machine_id': 1,
                                 'task_type_cd': 0,
                             },
                             {
                                 'coordinates': [55.8372856, 37.516643],
                                 'machine_name': 'Car 2',
                                 'task_status_cd': 'IN_PROGRESS',
                                 'machine_id': 2,
                                 'task_type_cd': 1,
                             },
                             {
                                 'coordinates': [55.8172856, 37.506643],
                                 'machine_name': 'Car 3',
                                 'task_status_cd': 'IN_PROGRESS',
                                 'machine_id': 3,
                                 'task_type_cd': 2,
                             },
                         ], })


@api_view(['GET', 'POST'])
def getMachineInformation(request):
    return JsonResponse({'cars': [
        {
            'machine_name': 'Car 1',
            'task_status_cd': 'FAIL',
            'machine_id': 1,
            'machine_type': 0,
            'machine_state': 'Поломка',
            'machine_number': 'EA789A 77',
            'machine_description': 'Машина уборочная вакуумного типа'
        },
        {
            'machine_name': 'Car 2',
            'task_status_cd': 'IN_PROGRESS',
            'machine_id': 2,
            'machine_type': 1,
            'machine_state': 'На задании',
            'machine_number': 'АУ779В 77',
            'machine_description': 'Машина уборочная вакуумного типа'
        },
        {
            'machine_name': 'Car 3',
            'task_status_cd': 'IN_PROGRESS',
            'machine_id': 3,
            'machine_type': 2,
            'machine_state': 'На задании',
            'machine_number': 'ВС659A 77',
            'machine_description': 'Машина уборочно-подметалельная'
        },
    ], })


@api_view(['GET', 'POST'])
def getMachinesDepo(request):
    return JsonResponse({'cars': [
        {

            'machine_id': 1,
            'machine_type': 0,
            'machine_number': 'EA789A 77',
            'machine_state': 'Поломка',
            'is_machine_ready': 'False',
        },
        {

            'machine_id': 2,
            'machine_type': 1,
            'machine_number': 'АУ779В 77',
            'machine_state': 'На задании',
            'is_machine_ready': 'False',
        },
        {

            'machine_id': 3,
            'machine_type': 2,
            'machine_number': 'ВС659A 77',
            'machine_state': 'На задании',
            'is_machine_ready': 'False',
        },
        {

            'machine_id': 4,
            'machine_type': 1,
            'machine_number': 'АС720Р 77',
            'machine_state': 'В парке',
            'is_machine_ready': 'True',
        },
        {

            'machine_id': 5,
            'machine_type': 1,
            'machine_number': 'ЕК121М 77',
            'machine_state': 'В парке',
            'is_machine_ready': 'True',
        },
    ], })


@csrf_exempt
def get_all_machines(request):
    if request.method == 'GET':
        machines = Vehicle.objects.all()
        serializer = VehicleSerializer(machines, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_all_tasks(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_root(request):
    return render(request, 'index.html')


@csrf_exempt
class ViewMachineLocations(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

# 4examples
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
