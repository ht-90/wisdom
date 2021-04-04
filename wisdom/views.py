from django.shortcuts import render


def handle_403(request, exception):
    return render(request, "error_403.html", context={}, status=403)


def handle_404(request, exception):
    return render(request, "error_404.html", context={}, status=404)


def handle_500(request):
    return render(request, "error_500.html", context={}, status=500)
