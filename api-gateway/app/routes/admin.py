from jinja2 import TemplateNotFound

from flask import Blueprint, request, render_template

admin_router = Blueprint('admin', __name__, url_prefix='/admin')


@admin_router.route('/')
def getDashboard():
    return render_template('admin/ui-icons.html')
    
@admin_router.route('/<template>')
def route_template(template):
    try:
        if not template.endswith( '.html' ):
            template ='admin/' + template + '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('admin/page-404.html'), 404
    
    except:
        return render_template('templates/page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
