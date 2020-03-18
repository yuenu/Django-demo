from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from blog.models import Post



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'api/task-list',
		'Detail View':'api/task-detail/<str:pk>',
		'Create':'api/task-create/',
		'Update':'api/task-update/<str:pk>',
		'Delete':'api/task-delete/<str:pk>',
	}
	return Response(api_urls)


# C . U .R .D .->
@api_view(['GET'])
def taskList(request):
	tasks = Post.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
	task = Post.objects.get(id=pk)
	serializer = TaskSerializer(task, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
	task = Post.objects.get(id=pk)
	serializer = TaskSerializer(instance=task,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
	task = Post.objects.get(id=pk)
	task.delete()
	return Response("Item succesfully delete")