import os
import shutil
from flask import jsonify
import ..confifg.extensions as extensions

import ..utils.organize as organize

router = Blueprint('api', __name__, url_prefix='/api')

@router.route('/organize', methods=['POST'])
organize():