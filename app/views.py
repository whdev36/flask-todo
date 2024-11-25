from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import TaskForm
from .models import Todo
from . import database as db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    tasks = Todo.query.all()
    return render_template('home.html', tasks=tasks)

@views.route('/create', methods=['GET', 'POST'])
def create():
    form = TaskForm()
    if form.validate_on_submit():
        task = Todo(task=form.task.data)
        db.session.add(task)
        db.session.commit()
        flash('A new task has been created.', 'success')
        return redirect(url_for('views.home'))
    else:
        flash('Something went wrong.', 'danger')
    return render_template('create.html', form=form)

@views.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    form = TaskForm(task=todo.task)
    if form.validate_on_submit():
        todo.task = form.task.data
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template('update.html', form=form)

@views.route('/delete/<id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('views.home'))