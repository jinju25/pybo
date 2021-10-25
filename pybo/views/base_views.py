
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import render, get_object_or_404, redirect, reverse
from ..models import Question, Answer, Comment
from django.core.paginator import Paginator


@login_required(login_url='common:login')
@permission_required('pybo.can_view_list', login_url='pybo:permission_guide')
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)



def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') #페이지

    #조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def permission_guide(request):
    """
    pybo 직원 권한
    """
    return render(request, 'pybo/permission_guide.html')