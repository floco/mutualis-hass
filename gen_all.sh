#!/bin/bash

source /Volumes/config/env/bin/activate
python ./templates/gen_from_template.py --source-csv "links.csv" --template "dashmachine.template" --output "./templates/config.ini"
python ./templates/gen_from_template.py --source-csv "links.csv" --template "weblinks.template" --output "./dwains-dashboard/addons/more_page/weblinks/page2.secret"


exit
