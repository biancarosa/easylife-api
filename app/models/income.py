from mongoengine import Document, DecimalField, StringField

class Income(Document):

    reference_month = StringField()
    amount = DecimalField()

    def to_json(self):
        return {
            "reference_month": self.reference_month,
            "amount" : self.amount
        }
