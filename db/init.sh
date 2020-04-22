#!/bin/bash
mongo <<EOF

use pythonsetupcode;
db.createCollection("clp");

EOF
