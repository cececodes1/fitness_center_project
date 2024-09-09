from flask import jsonify, request
from app import app, db
from models import Member, WorkoutSession


@app.rout('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    new_member = Member(data['name'], data['email'], data['phone_number'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member created succesfully'}), 201

@app.route('/members', methods=['GET'])
def get_all_members():
    members = Member.query.all()
    output = []
    for member in members:
        member_data = {'id': member.id, 'name': member.name, 'email': member.email, 'phone_number': member.phone_number}
        output.append(member_data)
    return jsonify({'members': output})

@app.route('/members/<id>', methods=['GET'])
def get_member(id):
    member = Member.query.get(id)
    if member is None:
        return jsonify({'message': 'Member not found'}), 404
    member_data = {'id': member.id, 'name': member.name, 'email': member.email, 'phone_number': member.phone_number}
    return jsonify({'member': member_data})

@app.route('/members/<id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get(id)
    if member is None:
        return jsonify({'message': 'Member not found'}), 404
    data = request.get_json()
    member.name = data['name']
    member.email = data['email']
    member.phone_number = data['phone_number']
    db.session.commit()
    return jsonify({'message': 'Member updated successfully'})

@app.route('/members/<id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if member is None:
        return jsonify({'message': 'Member not found'}), 404
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'})


# Create a new workout session
@app.route('/workout-sessions', methods=['POST'])
def create_workout_session():
    data = request.get_json()
    new_workout_session = WorkoutSession(data['member_id'], data['date'], data['duration'], data['intensity'])
    db.session.add(new_workout_session)
    db.session.commit()
    return jsonify({'message': 'Workout session created successfully'}), 201

# Get all workout sessions
@app.route('/workout-sessions', methods=['GET'])
def get_all_workout_sessions():
    workout_sessions = WorkoutSession.query.all()
    output = []
    for workout_session in workout_sessions:
        workout_session_data = {'id': workout_session.id, 'member_id': workout_session.member_id, 'date': workout_session.date, 'duration': workout_session.duration, 'intensity': workout_session.intensity}
        output.append(workout_session_data)
    return jsonify({'workout_sessions': output})

# Get a workout session by ID
@app.route('/workout-sessions/<id>', methods=['GET'])
def get_workout_session(id):
    workout_session = WorkoutSession.query.get(id)
    if workout_session is None:
        return jsonify({'message': 'Workout session not found'}), 404
    workout_session_data = {'id': workout_session.id, 'member_id': workout_session.member_id, 'date': workout_session.date, 'duration': workout_session.duration, 'intensity': workout_session.intensity}
    return jsonify({'workout_session': workout_session_data})

# Update a workout session
@app.route('/workout-sessions/<id>', methods=['PUT'])
def update_workout_session(id):
    workout_session = WorkoutSession.query.get(id)
    if workout_session is None:
        return jsonify({'message': 'Workout session not found'}), 404
    data = request.get_json()
    workout_session.member_id = data['member_id']
    workout_session.date = data['date']
    workout_session.duration = data['duration']
    workout_session.intensity = data['intensity']
    db.session.commit()
    return jsonify({'message': 'Workout session updated successfully'})

# Delete a workout session
@app.route('/workout-sessions/<id>', methods=['DELETE'])
def delete_workout_session(id):
    workout_session = WorkoutSession.query.get(id)
    if workout_session is None:
        return jsonify({'message': 'Workout session not found'}), 404
    db.session.delete(workout_session)
    db.session.commit()
    return jsonify({'message': 'Workout session deleted successfully'})