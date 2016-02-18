from django.shortcuts import render
import datetime

# Create your views here.
def main(request):
    now = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    return render(request, 'main/main.html', {'now':now})

def about(request):
    return render(request, 'main/about.html')