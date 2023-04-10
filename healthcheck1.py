#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails
import os


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_memory_usage():
    """Verifies that there's enough free memory"""
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "student-02-e130edcab998@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    


# If there's not enough disk, or not enough CPU, print an error
if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    print(subject)
    send_email(subject)

if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    print(subject)

if not check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    print(subject)
    send_email(subject)

if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    send_email(subject)
