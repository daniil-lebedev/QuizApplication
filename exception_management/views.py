from django.shortcuts import render


# Create your views here.

# handle 404 error
def error_404(request, exception):
    context = {
        'error': '404',
        'message': 'Page not found'
    }
    return render(request, 'exceptions/exception_template.html', status=404, context=context)


def error_500(request):
    context = {
        'error': '500',
        'message': 'Internal server error'
    }
    return render(request, 'exceptions/exception_template.html', status=500, context=context)


def error_403(request, exception):
    context = {
        'error': '403',
        'message': 'Forbidden'
    }
    return render(request, 'exceptions/exception_template.html', status=403, context=context)


def error_400(request, exception):
    context = {
        'error': '400',
        'message': 'Bad request'
    }
    return render(request, 'exceptions/exception_template.html', status=400, context=context)
