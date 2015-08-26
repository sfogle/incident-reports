from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

from flask_wtf import Form
from wtforms import StringField

from incidentreports.models import Report

reports = Blueprint('reports', __name__, template_folder='templates')


class ReportForm(Form):
    name = StringField('name')


class MapView(MethodView):
    def get(self):
        form = ReportForm()
        return render_template('map.html', form=form)

    def post(self, id):
        context = self.get_context(id)
        form = context.get('form')
        return render_template('map.html')


# Register the urls
# posts.add_url_rule('/reports/', view_func=ListView.as_view('list'))
# posts.add_url_rule('/reports/<id>/', view_func=DetailView.as_view('detail'))
reports.add_url_rule('/maps/', view_func=MapView.as_view('example'))
