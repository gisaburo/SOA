def lambda_handler(event, context):
    response = {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": event["templateParameterValues"]["DeletionPolicy"]
    }
    return response
