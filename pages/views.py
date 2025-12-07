from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .forms import PaperSubmissionForm
from .models import PaperSubmission
from .models import Photo


def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about_9acee.html')

def hosts(request):
    return render(request, 'pages/hosts.html')

def fees(request):
    return render(request, 'pages/fees.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def venue(request):
    return render(request , 'pages/venue.html' )

def Accommodations(request):
    return render(request , 'pages/accommodations.html' )

def Conference_Themes_and_Topics(request):
    return render(request,'pages/themes.html')

def keynote_speaker(request):
    return render(request, 'pages/keynote_speaker.html')

def invited_speaker(request):
    return render(request, 'pages/invited_speaker.html')

def photos(request):
    return render(request , 'pages/photos.html' )

def program(request):
    return render(request,'pages/program.html')

def paperformat(request):
    return render(request , 'pages/paper_format_and_agenda.html')


class PaperSubmissionView(LoginRequiredMixin, View):
    def get(self, request):
        form = PaperSubmissionForm()
        return render(request, "pages/submit_form.html", {"form": form})

    def post(self, request):
        form = PaperSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect("paper-download", submission.pk)
        return render(request, "pages/submit_form.html", {"form": form})

def download_submission(request, pk):
    submission = PaperSubmission.objects.get(pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="submission_{pk}.pdf"'

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Paper Submission Details")
    pdf.drawString(100, 780, f"Full Name: {submission.author_fullname}")
    pdf.drawString(100, 760, f"Affiliation: {submission.affiliation}")
    pdf.drawString(100, 740, f"Designation: {submission.designation}")
    pdf.drawString(100, 720, f"Country: {submission.country}")
    pdf.drawString(100, 700, f"Email: {submission.email}")
    pdf.drawString(100, 680, f"Phone: {submission.phone}")
    pdf.drawString(100, 660, "Author List:")
    pdf.drawString(100, 640, submission.author_list[:80])
    pdf.drawString(100, 620, f"Presenting Author: {submission.presenting_author}")

    pdf.showPage()
    pdf.save()
    return response



def photos(request):
    all_photos = Photo.objects.all()
    return render(request, 'pages/photos.html', {'photos': all_photos})
