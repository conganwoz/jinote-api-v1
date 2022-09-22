from datetime import datetime, timezone
import pytz
import hashlib
import random

from passlib.hash import pbkdf2_sha256

def is_empty(value):
    return (value=='undefined'
			or value=='null'
			or value==''
			or (value is None))


def convert_to_vn_time(utc_dt):
    if is_empty(utc_dt):
        return None

    return utc_dt.astimezone(pytz.timezone('Asia/Bangkok'))


def format_datetime(dt):
    if is_empty(dt):
        return None

    return dt.strftime('%H:%M:%S %d-%m-%Y')


def passlib_encryption(raw_password):
	if raw_password:
		encrypted = pbkdf2_sha256.hash(raw_password)
	else:
		encrypted = None

	return encrypted


def passlib_pbkdf2_sha256_encrypt(raw_password):
	# generate new salt, and hash a password
	salt_size = 32
	rounds = 12000

	if raw_password:
		encrypted = pbkdf2_sha256.encrypt(raw_password, rounds, salt_size)
	else:
		encrypted = None

	return encrypted


def passlib_encryption_verify(raw_password, enc_password):
	if raw_password and enc_password:
		# verifying the password
		response = pbkdf2_sha256.verify(raw_password, enc_password)
	else:
		response = None;

	return response


