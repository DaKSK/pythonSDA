class Contact:
    def __init__(self, name, home_phone=None, mobile_phone=None, email=""):

        if home_phone is None and mobile_phone is None:
            raise ValueError

        if not home_phone.startswith("+372"):
            raise ValueError

        if "@" in email:
            self.email = email
        else:
            self.email = ""

    @property
    def country_code(self):
        if self.home_phone is not None:
            code = self.home_phone[0:2]
            return code

    @property
    def mobile_phone_wo_code(self):
        mobile = self.mobile_phone[3:]
        return mobile

    def has_email(self):
        return self.email is not None

    def country_from_code(self):
        country_code_data = {"372": "Estonia"}
        country = country_code_data[self.country_code]
        return country
