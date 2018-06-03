# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_price_list_update"
app_title = "Actualizacion Lista Precio"
app_publisher = "Diamo"
app_description = "Price List updated by percentage"
app_icon = "octicon octicon-file-directory"
app_color = "#318BB8"
app_email = "contacto@diamo.com.ar"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_price_list_update/css/erpnext_price_list_update.css"
# app_include_js = "/assets/erpnext_price_list_update/js/erpnext_price_list_update.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_price_list_update/css/erpnext_price_list_update.css"
# web_include_js = "/assets/erpnext_price_list_update/js/erpnext_price_list_update.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_price_list_update.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_price_list_update.install.before_install"
# after_install = "erpnext_price_list_update.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_price_list_update.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_price_list_update.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_price_list_update.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_price_list_update.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_price_list_update.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_price_list_update.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_price_list_update.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_price_list_update.event.get_events"
# }

