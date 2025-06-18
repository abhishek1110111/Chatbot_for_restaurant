from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import generic_helper
app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    
    webhook_response = await request.json()
    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = webhook_response['queryResult']['intent']['displayName']
    parameters = webhook_response['queryResult']['parameters']
    output_contexts = webhook_response['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])
    
    intent_handler_dict = {
        'order.add-context:ongoing-order': add_order,
        'order.remove-context:ongoing-order': remove_order,
        'order.complete-context:ongoing-order': complete_order,
        'track.order-context:ongoing-tracking': track_order
    }

    return intent_handler_dict[intent](parameters, session_id)
    
    def add_order(parameters: dict, session_id: str):
        pass

    def remove_order(parameters: dict, session_id: str):
        pass

    def complete_order(parameters: dict, session_id: str):
        pass

    def track_order(parameters: dict, session_id: str):
        pass