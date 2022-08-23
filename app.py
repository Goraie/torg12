import pdfkit
options = {
	'page-size': 'A4',
	'orientation': 'landscape'
}
pdfkit.from_file('index.html', 'index.pdf', options=options)