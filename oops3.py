class DataValidator():
    def __init__(self):
        self.error = []

    def validate_email(self,email):
        if '@' not in email:
            self.error.append(f'Invalid email : {email}')
            return False
        return True

    def validate_age(self,age):
        if age < 0 or age > 100:
            self.error.append(f'Invalid Age: {age}')
            return False
        return True

    def get_errors(self):
        return self.error

validator = DataValidator()

validator.validate_email('darshangmail.com')

validator.validate_age(101)

validator.get_errors()
        