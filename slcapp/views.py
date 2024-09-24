from flask import render_template, request, abort, redirect, url_for, send_file, flash, session, g, current_app
#import paramiko
import os

@current_app.route('/')
def index():
  return render_template("index.html")