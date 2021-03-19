from flask import Blueprint,redirect,request,Response
from controllers.deals_controller import DealsController

blueprint = Blueprint("deals", __name__)

deals_controller = DealsController()


@blueprint.route('/api/deals', methods=["GET"])
def get_deals():
    username = request.get_json()['username']
    print(request.get_json())
    response = deals_controller.get_deals(username)
    return Response(
        response,
        mimetype='application/json',
        status=200
    )