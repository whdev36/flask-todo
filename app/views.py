from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import TaskForm
from .models import Todo
from . import database as db

views = Blueprint('views', __name__)

def get_todo_or_404(todo_id):
    """Helper function to fetch a Todo item or return a 404."""
    return Todo.query.get_or_404(todo_id)

@views.route('/')
def home():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()  # Order by newest first
    return render_template('home.html', todos=todos)

@views.route('/create', methods=['GET', 'POST'])
def create():
    form = TaskForm()
    if form.validate_on_submit():
        try:
            task = Todo(task=form.task.data)
            db.session.add(task)
            db.session.commit()
            flash('A new task has been created.', 'success')
            return redirect(url_for('views.home'))
        except Exception as e:
            flash(f'Error creating task: {str(e)}', 'danger')
    return render_template('create.html', form=form)

@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = get_todo_or_404(id)
    form = TaskForm(task=todo.task)
    if form.validate_on_submit():
        try:
            todo.task = form.task.data
            db.session.commit()
            flash('Task has been updated.', 'success')
            return redirect(url_for('views.home'))
        except Exception as e:
            flash(f'Error updating task: {str(e)}', 'danger')
    return render_template('update.html', form=form)

@views.route('/delete/<int:id>')
def delete(id):
    todo = get_todo_or_404(id)
    try:
        db.session.delete(todo)
        db.session.commit()
        flash('Task has been deleted.', 'success')
    except Exception as e:
        flash(f'Error deleting task: {str(e)}', 'danger')
    return redirect(url_for('views.home'))

@views.route('/toggle/<int:id>')
def toggle(id):
    todo = get_todo_or_404(id)
    try:
        todo.completed = not todo.completed
        db.session.commit()
        flash(f'Task marked as {"completed" if todo.completed else "not completed"}.', 'info')
    except Exception as e:
        flash(f'Error toggling task: {str(e)}', 'danger')
    return redirect(url_for('views.home'))
