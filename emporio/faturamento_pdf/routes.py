from flask import render_template, Blueprint, request, Response
from emporio import db, Collaborator, Service, ServiceCollaborator
from datetime import datetime, time
from fpdf import FPDF

faturamento_pdf = Blueprint('faturamento_pdf', __name__)


@faturamento_pdf.route("/faturamento_pdf")
def home():
    result = {}
    collaborators = db.session.execute(
        db.select(Collaborator.collaborator_id, Collaborator.collaborator_name)).all()
    result['collaborators'] = collaborators
    return render_template('faturamento_pdf/home.html', result=result)


@faturamento_pdf.route("/faturamento_pdf/download", methods=['POST'])
def download_pdf():
    faturamento_pdf_form = request.get_json()
    start = datetime.strptime(faturamento_pdf_form['start'], '%Y-%m-%d')
    end = datetime.combine(datetime.strptime(faturamento_pdf_form['end'], '%Y-%m-%d'), time.max)
    collaborator = db.session.execute(
        db.select(Collaborator.collaborator_name)
        .where(Collaborator.collaborator_id == faturamento_pdf_form['collaborator'])).scalar()

    result = db.session.execute(
        db.select(ServiceCollaborator.client_name,
                  Service.service_name, Service.service_price,
                  ServiceCollaborator.service_collaborator_date)
        .join(Service)
        .join(Collaborator)
        .where(ServiceCollaborator.collaborator_id == faturamento_pdf_form['collaborator'])
        .where(ServiceCollaborator.service_collaborator_date >= start)
        .where(ServiceCollaborator.service_collaborator_date <= end)).all()
    pdf = FPDF()
    pdf.add_page()

    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font('Times', 'B', 14)
    pdf.cell(page_width, 0.0, collaborator, align='C')
    pdf.ln(10)

    pdf.set_font('Courier', '', 6)
    col_width = page_width / 4
    pdf.ln(1)
    th = pdf.font_size
    total = 0.0
    for row in result:
        pdf.cell(col_width, th, row[0], border=1)
        pdf.cell(col_width, th, row[1], border=1)
        pdf.cell(col_width, th, str(row[2]), border=1)
        pdf.cell(col_width, th, row[3].strftime("%d/%m/%Y"), border=1)
        pdf.ln(th)
        total += row[2]

    pdf.ln(10)

    pdf.set_font('Times', 'B', 14)
    pdf.cell(page_width, 0.0, f'Total: {calculate_percentage(total)}', align='C')
    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf')


def calculate_percentage(total):
    return float(format(total * 0.4, '.2f'))
