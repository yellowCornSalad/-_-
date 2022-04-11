from django.shortcuts import get_object_or_404, redirect, render
from community.forms import Form
from .models import Article 
# Create your views here.
def write(request):
    # form 데이터를 입력하고 확인, 데이터 저장 요청
    if request.method == 'POST':      #POST 는 대문자로 
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/community/list/')
    #빈 form 페이지 요청 
    else :
        form= Form()
    
    return render(request, 'community/write.html', {'form': form})

# 글작성 목록 보여주기 
def articleList(request) :
    article_list =  Article.objects.all()    
    return render(request, 'community/list.html', {'article_list':article_list})
    
    
def viewDetail(request, num=1):
    # article_detail = Article.objects.get(pk=num)  #id 대신 pk
    article_detail = get_object_or_404(Article, pk=num)
    return render(request, 'community/view_detail.html', {'article_detail' : article_detail} )


def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate') [:3]
    return render(request, 'index.html', {'latest_article_list':
    latest_article_list})