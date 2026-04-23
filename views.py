from django.shortcuts import render, redirect
from .models import Issue
 
def report_step1(request):
    if request.method == 'POST':
        request.session['issue_type'] = request.POST.get('issue_type')
        return redirect('report_step2')
    return render(request, 'report_step1.html', {
        'issue_types': Issue.ISSUE_TYPES
    })
 
def report_step2(request):
    if request.method == 'POST':
        request.session['location'] = request.POST.get('location')
        request.session['description_step2'] = request.POST.get('description', '')
        return redirect('report_step3')
   
    context = {
        'location': request.session.get('location', ''),
        'description': request.session.get('description_step2', '')
    }
    return render(request, 'report_step2.html', context)
 
def report_step3(request):
    if request.method == 'POST':
        issue_type = request.session.get('issue_type')
        location = request.session.get('location')
        description = request.POST.get('description', '')
 
        if issue_type and location:
            issue = Issue.objects.create(
                issue_type=issue_type,
                location=location,
                description=description or request.session.get('description_step2', ''),
            )
 
           
            for key in ['issue_type', 'location', 'description_step2']:
                request.session.pop(key, None)
 
            return render(request, 'report_step3.html', {
                'success': True,
                'reference': issue.reference_number,
                'issue': issue
            })
 
    
    context = {
        'success': False,
    }
    return render(request, 'report_step3.html', context)
 
def track_issue(request):
    if request.method == 'POST':
        ref = request.POST.get('reference_number', '').strip()
        try:
            issue = Issue.objects.get(reference_number=ref)
            return render(request, 'track.html', {'issue': issue})
        except Issue.DoesNotExist:
            return render(request, 'track.html', {'error': True, 'reference': ref})
    return render(request, 'track.html')