from django.shortcuts import render

from cv.models import Me


def index(request):



    user = Me.objects.all()[0]
    template_data = {
        'user': user,
        'contact_refs': user.contact_refs.all(),
        'educations': user.educations.all(),
        'languages': user.languages.all(),
        'interests': user.interests.all(),
        'skills': user.skills.all(),
        'experiences': user.experiences.all(),
        'extra_sections': user.extra_sections.all()
    }

    return render(request, 'indexcv.html', template_data)
