from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import generic_helper
from helper.helper import track_order, add_order,\
    complete_order, remove_order, add_address


app = FastAPI()
@app.post("/")    
async def handle_request(request: Request):
    """Handle incoming requests from Dialogflow webhook."""
    # Retrieve the JSON data from the request
    webhook_response = await request.json()
    print(webhook_response)
    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = webhook_response['queryResult']['intent']['displayName']
    parameters = webhook_response['queryResult']['parameters']
    output_contexts = webhook_response['queryResult']['outputContexts']
    session_id = generic_helper.fetch_session_id(output_contexts[0]["name"])
    
    if intent == 'track.order-context:ongoing-tracking':
        response = track_order(parameters)
        return JSONResponse(content={"fulfillmentText": response})
    elif intent == 'order.add-context:ongoing-order':
        response = add_order(parameters, session_id)  
        return JSONResponse(content={"fulfillmentText": response}) 
    elif intent == 'order.add-address-context:ongoing-order':
        response = add_address(parameters, session_id)
        return JSONResponse(content={"fulfillmentText": response})
    elif intent == 'order.complete-context:ongoing-order':
        response =complete_order(session_id)   
        return JSONResponse(content={"fulfillmentText": response})  
    elif intent == 'order.remove-context:ongoing-order':
        response = remove_order(parameters, session_id)
        return JSONResponse(content={"fulfillmentText": response})