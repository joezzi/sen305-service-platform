from django.shortcuts import render

def ab(request):
    project_roles = [
        "Requester",
        "Coordinator",
        "Technician",
        "Administrator",
    ]
    return render(
        request,
        "core/about.html",
        {"project_roles": project_roles},
    )