from flask import jsonify

def success_response(data, status_code=200):
    return jsonify({
        'status': 'success',
        'data': data,
        'statusCode': status_code,
    })

def error_response(message="Error", status_code=400):
    return jsonify({
        'status': 'error',
        'message': message,
        'statusCode': status_code,
    })

def validation_error_response(errors):
    return error_response(errors, 400)

def not_found_response(resource="Resource"):
    return error_response(f"Resource '{resource}' not found", 404)

def unauthorized_response(message="Unauthorized", status_code=401):
    return error_response(message=message, status_code=status_code)

def forbidden_response(message="Forbidden", status_code=403):
    return error_response(message=message, status_code=status_code)
