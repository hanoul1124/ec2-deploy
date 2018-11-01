from django.shortcuts import render

# Create your views here.

def index(request):
    # templates/index.html 파일을 보여주도록 함
    # Root URL ('/')에서 이 views로 이동
    return render(request, 'index.html')
