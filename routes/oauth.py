from flask import Blueprint,redirect,request,Response
from controllers.oauth_controller import  OAuthController

blueprint = Blueprint("oauth",__name__)

oauth_controller = OAuthController()


@blueprint.route('/api/oauth/authorization', methods=["GET"])
def get_authorization_url():
    return redirect(oauth_controller.get_authorization_url())


@blueprint.route('/api/oauth/callback', methods=["GET"])
def callback_oauth():
    user_code = request.args.get('code')

    response = oauth_controller.fill_user_data(user_code)

    return Response(
        response,
        mimetype="application/json",
        status=200
    )
