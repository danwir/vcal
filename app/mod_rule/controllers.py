from flask import Flask, render_template, request, redirect, abort, \
    Blueprint
import logging
import json

# Import the database object from the main app module
from app import db


from app.mod_rule.models import Rule

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_rule = Blueprint('rule', __name__)


# Log everything, and send it to stderr.
logging.basicConfig(filename="error.log",level=logging.INFO,format='%(asctime)s %(message)s')

@mod_rule.route("/rule/", methods=['POST', 'GET'])
def rule():
    try:
        if request.method == 'POST':
            d = request.get_json()
            gid = d['group_id']
            rule_definition = d['definition']
            r = Rule(gid, json.dumps(rule_definition))
            Rule.query.filter_by(group_id=gid).delete()
            db.session.add(r)
            db.session.commit()
            return 'rule saved'
        elif request.method == 'GET':
            return render_template('rule/{0}.html'.format('rule'))
        else:
            return abort(404)
    except Exception, e:
        logging.exception(e)
        return render_template("oops.html")
