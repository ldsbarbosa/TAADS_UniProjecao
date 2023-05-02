from django.contrib.staticfiles import finders
from io import BytesIO
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Paciente, CondicaoDeSaude

def link_callback(uri, rel):
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
        mUrl = settings.MEDIA_URL
        mRoot = settings.MEDIA_ROOT

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
    if not os.path.isfile(path):
        raise Exception('media URI must start with %s or %s' % (sUrl, mUrl))
    return path

class GeraPDF:
    def render_to_pdf(template_end, context_dict={}):
        response = HttpResponse(content_type='application/pdf')
        if 'condicoesDeSaude' in context_dict:
            response['Content-Disposition'] = 'attachment; filename="Relatório de Condições de Saúde.pdf"'
        elif 'pacientes' in context_dict:
            response['Content-Disposition'] = 'attachment; filename="Relatório de Pacientes.pdf"'
        else:
            response['Content-Disposition'] = 'attachment; filename="Relatório.pdf"'
        template = get_template(template_end)
        html = template.render(context_dict)
        try:
            pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
            return response
        except Exception as e:
            print(e)
            return HttpResponse(e)