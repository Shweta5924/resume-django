from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# home
def home(request):
    return render(request, 'resume/home.html')



def about_us(request):
    return render(request, 'about.html')


# to call temp1
def temp1(request):
    return render(request, 'resume/temp1.html')

def temp3(request):
    return render(request, 'resume/temp3.html')

# to generate temp1
def generate_pdf(request):
    template_path = 'resume/resume_template.html'
    context = {
        'full_name': request.POST.get('full_name'),
        'address': request.POST.get('address'),
        'phone_number': request.POST.get('phone_number'),
        'email_address': request.POST.get('email_address'),
        'about_yourself': request.POST.get('about_yourself'),
        'experience': request.POST.get('experience'),
        'technical_skills': request.POST.get('technical_skills'),
        'soft_skills': request.POST.get('soft_skills'),
    }
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#to call temp 2
def temp2(request):
    return render(request, 'resume/temp2.html')

# to generate temp2
def generate_pdf2(request):
    if request.method == 'POST':
        template_path = 'resume/resume_temp2.html'
        context = {
            'full_name': request.POST['full_name'],
            'address': request.POST['address'],
            'phone_number': request.POST['phone_number'],
            'email_address': request.POST['email_address'],
            'skills':request.POST['skills'],
            'about_yourself': request.POST['about_yourself'],
            'experience': request.POST['experience'],
            'technical_skills': request.POST['technical_skills'],
            'soft_skills': request.POST['soft_skills'],
        }
        name=request.POST['full_name']
        # Create a Django template and render it to HTML
        template = get_template(template_path)
        html = template.render(context)

        # Create a PDF object and return it as response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="name.pdf"'

        # Convert HTML to PDF using xhtml2pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response
        )

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    return HttpResponse("Only POST requests are allowed")


def temp3(request):
    return render(request, 'resume/temp3.html')

# tem3

# def generate_pdf3(request):
#     template_path = 'resume/resume_temp1.html'
#     context = {
#         'full_name': request.POST.get('full_name'),
#         'address': request.POST.get('address'),
#         'phone_number': request.POST.get('phone_number'),
#         'email_address': request.POST.get('email_address'),
#         'about_yourself': request.POST.get('about_yourself'),
#         'experience': request.POST.get('experience'),
#         'technical_skills': request.POST.get('technical_skills'),
#         'soft_skills': request.POST.get('skills'),
#     }
#     template = get_template(template_path)
#     html = template.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def generate_pdf3(request):
#     if request.method == "POST":
#         # Extract data from the form
#         context = {
#             'name': request.POST.get('name'),
#             'dob': request.POST.get('dob'),
#             'language': request.POST.get('language'),
#             'marital_status': request.POST.get('marital_status'),
#             'address': request.POST.get('address'),
#             'phone': request.POST.get('phone'),
#             'social': request.POST.get('social'),
#             'personal_skills': request.POST.get('personal_skills'),
#             'professional_skills': request.POST.get('professional_skills'),
#             'education': request.POST.get('education'),
#             'employment': request.POST.get('employment'),
#             'profile': request.POST.get('profile'),
#         }

#         # Load the template
#         template = get_template('resume/resume_temp1.html')  # Use the provided PDF template HTML
#         html = template.render(context)

#         # Generate the PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#         pisa_status = pisa.CreatePDF(html, dest=response)

#         if pisa_status.err:
#             return HttpResponse(f'Error generating PDF: {pisa_status.err}')

#         return response

#     # Redirect to the form if the request is not POST
#     return render(request, 'input_form.html')


from django.template.loader import render_to_string
from xhtml2pdf import pisa

def generate_pdf3(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        skills = [skill.strip() for skill in request.POST.get('skills', '').split(',')]

        education = []
        for edu in request.POST.get('education', '').split('\n'):
            if edu.strip():
                try:
                    degree, university, year = edu.split(' - ')
                    education.append({'degree': degree.strip(), 'university': university.strip(), 'year': year.strip()})
                except ValueError:
                    continue

        experience = []
        for exp in request.POST.get('experience', '').split('\n'):
            if exp.strip():
                try:
                    job_title, company, years = exp.split(' - ')
                    experience.append({'job_title': job_title.strip(), 'company': company.strip(), 'years': years.strip()})
                except ValueError:
                    continue

        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'skills': skills,
            'education': education,
            'experience': experience,
        }

        # Generate PDF
        html = render_to_string('resume/resume_temp1.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="resume.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generating PDF', status=500)

        return response

    return render(request, 'resume.temp3.html')



