from flask import Flask
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from graphene_file_upload.flask import FileUploadGraphQLView

from .schema import schema
from .database import db_session

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "jh876876g66236990990909%16777#ff992n623TG33fg545455"
app.config['REFRESH_EXP_LENGTH'] = 30
app.config['ACCESS_EXP_LENGTH'] = 10
app.config['JWT_SECRET_KEY'] = "Bearer"

auth = GraphQLAuth(app)
app.add_url_rule("/graphql",
                 view_func=FileUploadGraphQLView.as_view(
                     "grahql",
                     schema = schema,
                     graphiql = True
                 ))
@app.teardown_appcontext
def shuwdown_session(exception = None):
    db_session.remove()