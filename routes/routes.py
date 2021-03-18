from flask import Blueprint,Response
from usecases.create_example import  CreateExample
from serializers.entity import EntityJsonEncoder
import json

blueprint = Blueprint("entity",__name__)

usecase = CreateExample()


@blueprint.route('/example', methods=["GET"])
def example():
    entity = usecase.create_example()
    return Response(
        json.dumps(entity, cls=EntityJsonEncoder),
        mimetype="application/json",
        status=200
    )

