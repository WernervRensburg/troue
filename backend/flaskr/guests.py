from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, make_response, jsonify
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
        fullname = request.form['fullname']
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
            return redirect(url_for('guests.guestlist'))

    return render_template('guests/create.html')

@bp.route('/find_guest', methods=["POST"])
def find_guest():
    print('finding guest...')
    try:

        if request.args.get('format') == 'json':
            data = request.get_json()
            print(data)

            guest_name = data.get('name')
            if not guest_name:
                return jsonify({'error': 'guest_name_required'}), 400

            db = get_db()
            guest = db.execute(
                'SELECT * FROM guests WHERE fullname = ?', (guest_name,)
            ).fetchone()

            if guest is None:
                return jsonify({'error': 'guest_not_found'}), 404

            family_group = guest['familyGroup']
            familyGuests = db.execute(
                'SELECT * FROM guests WHERE familyGroup = ?', (family_group,)
            ).fetchall();

            guests_list = [dict(row) for row in familyGuests]

            return jsonify(guests_list), 200
        else:
            response_data = {'message': 'format not json'}
            return jsonify(response_data), 400
    except Exception as e:
        print('Error:', str(e))
        return make_response('Internal Server Error', 500)

@bp.route('/update_guest_attendance', methods=["POST"])
def update_guest_attendance():
    print('Saving guest attendance...')
    try:
        data = request.get_json()
        print(data)
        format_value = request.args.get('format')
        print('Format query parameter:', format_value)
        if request.args.get('format') == 'json':
            response_data = {'message': 'json message'}
            return jsonify(response_data), 200
        else:
            response_data = {'message': 'format not json'}
            return jsonify(response_data), 400  # Bad Request
    except Exception as e:
        print('Error:', str(e))
        return make_response('Internal Server Error', 500)


@bp.route('/update_guest_accommodation', methods=["POST"])
def update_guest_accommodation():
    try:
        data = request.get_json()
        print(data)
        format_value = request.args.get('format')
        print('Format query parameter:', format_value)
        if request.args.get('format') == 'json':
            response_data = {'message': 'json message'}
            return jsonify(response_data), 200
        else:
            response_data = {'message': 'format not json'}
            return jsonify(response_data), 400  # Bad Request
    except Exception as e:
        print('Error:', str(e))
        return make_response('Internal Server Error', 500)


@bp.route('/update_guest_email', methods=["POST"])
def update_guest_email():
    try:
        data = request.get_json()
        print(data)
        format_value = request.args.get('format')
        print('Format query parameter:', format_value)
        if request.args.get('format') == 'json':
            response_data = {'message': 'json message'}
            return jsonify(response_data), 200
        else:
            response_data = {'message': 'format not json'}
            return jsonify(response_data), 400  # Bad Request
    except Exception as e:
        print('Error:', str(e))
        return make_response('Internal Server Error', 500)
