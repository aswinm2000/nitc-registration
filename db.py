from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tuition_fee(db.Model):
    transaction_id = db.Column(db.String(110),primary_key=True)
    user_id = db.Column(db.Integer)
    payment_amount = db.Column(db.String(150))
    payment_date = db.Column(db.Date)
    bank = db.Column(db.String(150))
    mode_of_payment = db.Column(db.String(150))
    verifier_id = db.Column(db.Integer)

    def __init__(self,transaction_id, user_id, payment_amount, payment_date, bank, mode_of_payment, verifier_id):
        self.transaction_id = trasaction_id
        self.user_id = user_id
        self.payment_amount = payment_amount
        self.payment_date = payment_date
        self.bank = bank
        self.mode_of_payment = mode_of_payment
        self.verifier_id = verifier_id


class application(db.Model):
    application_id = db.Column(db.String(110),primary_key=True)
    submission_date = db.Column(db.Date)
    submitted_by = db.Column(db.Integer)
    status = db.Column(db.String(150))
    last_updated = db.Column(db.Date)
    verified_by = db.Column(db.Integer)

    def __init__(self,application_id, submission_date, submitted_by, status, last_updated, verified_by):
        self.application_id = application_id
        self.submission_date= submission_date
        self.submitted_by = submitted_by
        self.status = status
        self.last_updated = last_updated
        self.verified_by = verified_by

class user(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(150))
    email_id = db.Column(db.String(150))
    hashed_password = db.Column(db.String(150))
    contact_no = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    m_init = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    role = db.Column(db.String(150))
    semester = db.Column(db.Integer)
    department = db.Column(db.String(150))
    category = db.Column(db.String(150))

    def __init__(self, user_id, user_name, email_id, hashed_password, contact_no, first_name, m_init, last_name, role, semester, department, category):
        self.user_id = user_id
        self.user_name = user_name
        self.email_id = email_id
        self.hashed_password = hashed_password
        self.contact_no = contact_no
        self.first_name = first_name
        self.m_init = m_init
        self.last_name = last_name
        self.role = role
        self.semester = semester
        self.department = department
        self.category = category

class dues(db.Model):
    due_id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    due_type = db.Column(db.String(150))
    updated_date = db.Column(db.Date)

    def __init__(self, due_id, amount, user_id, due_type, updated_date):
        self.due_id = due_id
        self.amount = amount
        self.user_id = user_id
        self.due_type = due_type
        self.updated_date = updated_date
        self.mode_of_payment = mode_of_payment
