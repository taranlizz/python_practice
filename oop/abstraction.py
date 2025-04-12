"""
Abstraction:
the process of hiding complex implementation details
and exposing only the essential features of an object or a system.
In Python abstract classes and abstract methods are used to enforce abstraction.
"""


class EmailService:

    @staticmethod
    def _connect():
        print("Connecting to email server")

    @staticmethod
    def _authenticate():
        print("Authenticating")

    @staticmethod
    def _disconnect():
        print("Disconnecting from email server...")

    @staticmethod
    def send_mail():
        EmailService._connect()
        EmailService._authenticate()
        print("Sending email...")
        EmailService._disconnect()


EmailService.send_mail()
