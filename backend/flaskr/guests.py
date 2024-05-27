from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.rsvp import login_required
from flaskr.db import get_db

bp = Blueprint('guests', __name__, url_prefix='/guests')

@bp.route('/guestlist', methods=(["GET"]))
def guestlist():
    db = get_db()
    guests = db.execute(
        'SELECT * FROM guests'
    ).fetchall()
    return render_template('guests/guestlist.html', guests=guests)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        fullname = request.form['fullnames']
        familyGroup = request.form['familyGroup']
        friday = request.form['friday']
        accommodation = request.form['accommodation']
        attendance = request.form['attendance']
        email = request.form['email']

        error = None

        if not fullname or not familyGroup or not friday or not accommodation or not attendance or not email:
            error = 'Missing argument.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO guests (fullname, familyGroup, friday, accommodation, attendance, email)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (fullname, familyGroup, friday, accommodation, attendance, email)
            )
            db.commit()
            return redirect(url_for('guests.index'))

    return render_template('guests/create.html')

@bp.route('/find_guest', methods=["GET"])
def find_guest():
    if request.method == 'GET':
        if request.args.get('format') == 'json':
            print('finding guest...')
            data = {'message': 'json message'}
            return jsonify(data)

@bp.route('/update_guest_attendance', methods=["POST"])
def update_guest_attendance():
    if request.method == 'POST':
        print('Saving guest attendance...')
        if request.args.get('format') == 'json':
            data = {'message': 'json message'}
            return jsonify(data)

@bp.route('/update_guest_accommodation', methods=["POST"])
def update_guest_accommodation():
    if request.method == 'POST':
        if request.args.get('format') == 'json':
            print('Saving guest accommodation...')
            data = {'message': 'json message'}
            return jsonify(data)

@bp.route('/update_guest_email', methods=["POST"])
def update_guest_email():
    if request.method == 'POST':
        if request.args.get('format') == 'json':
            print('Saving Guest Email...')
            data = {'message': 'json message'}
            return jsonify(data)