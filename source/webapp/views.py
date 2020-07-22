from django.shortcuts import render

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        context = {
            'number_1': int(request.POST.get('number_1', 0)),
            'number_2': int(request.POST.get('number_2', 0)),
        }
        if request.POST.get('operation') == 'plus':
            result = context['number_1'] + context['number_2']
            text = {
                'operation': '+',
                'result': result
            }
            context.update(text)
        elif request.POST.get('operation') == 'minus':
            result = context['number_1'] - context['number_2']
            text = {
                'operation': '-',
                'result': result
            }
        elif request.POST.get('operation') == 'multiply':
            result = context['number_1'] * context['number_2']
            text = {
                'operation': '*',
                'result': result
            }
        else:
            result = context['number_1'] / context['number_2']
            text = {
                'operation': '/',
                'result': result
            }
        context.update(text)
        return render(request, 'index.html', context)
