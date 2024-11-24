from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return 'Home'

@views.route('/create')
def create():
    return 'Create'

@views.route('/update/<id>')
def update(id):
    return 'Update'

@views.route('/delete/<id>')
def delete(id):
    return 'Delete'