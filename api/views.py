from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import openai

openai.api_key = settings.OPENAI_API_KEY

def register_page1(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        job_title = request.POST.get('job_title')
        experience = request.POST.get('experience')
        satisfaction = request.POST.get('satisfaction')
        education = request.POST.get('education')
        return render(request, 'page2.html', {
            'branch': branch,
            'job_title': job_title,
            'experience': experience,
            'satisfaction': satisfaction,
            'education': education
        })
    return render(request, 'page1.html')

def register_page2(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        job_title = request.POST.get('job_title')
        experience = request.POST.get('experience')
        satisfaction = request.POST.get('satisfaction')
        education = request.POST.get('education')
        skills = get_skill_suggestions(branch, job_title, experience, satisfaction, education)
        return render(request, 'page2.html', {
            'branch': branch,
            'job_title': job_title,
            'experience': experience,
            'satisfaction': satisfaction,
            'education': education,
            'skills': skills
        })
    return render(request, 'page2.html')

def get_skill_suggestions(branch, job_title, experience, satisfaction, education):
    prompt = (
        f"Based on the following details, suggest at least 3 relevant skills:\n"
        f"Branch: {branch}\n"
        f"Job Title: {job_title}\n"
        f"Experience: {experience}\n"
        f"Satisfaction: {satisfaction}\n"
        f"Education: {education}\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    suggestions = response.choices[0].message['content'].strip().split('\n')
    return suggestions
