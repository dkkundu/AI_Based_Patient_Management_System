
import tempfile

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


def render_pdf(request, template, context, file_name: str):
    """
    @type request: request
    @type template: template name (HTML Template File)
    @type context: Dictionary Key Value For Template
    @type file_name: str pdf file name
    """
    html_string = render_to_string(
        template, context
    )
    html = HTML(
        string=html_string,
        base_url=request.build_absolute_uri()
    )
    result = html.write_pdf()

    # Creating http response

    response = HttpResponse(content_type='appointment/pdf;')
    response[
        'Content-Disposition'] = 'inline; filename=' + file_name + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
