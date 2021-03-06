from django.test import TestCase
from finances.models import Invoice, Transaction


class InvoiceTestCase(TestCase):
    """
    Test case for the Invoice class.
    """

    def test_invoice_has_been_paid_with_exact_amount(self):
        """
        Tests if the method 'has_been_paid' returns True when an invoice's
        amount has been covered by one or more transactions.
        """
        invoice = Invoice.objects.create(total=100.00)
        invoice.save()

        Transaction.objects.bulk_create([
            Transaction(invoice=invoice, amount=10.00),
            Transaction(invoice=invoice, amount=20.00),
            Transaction(invoice=invoice, amount=30.00),
            Transaction(invoice=invoice, amount=40.00)
        ])

        self.assertTrue(invoice.has_been_paid(), "Method should state invoice has been paid.")

    def test_invoice_has_not_been_paid(self):
        """
        Tests if the method 'has_been_paid' returns False when an invoice's
        amount hasn't been covered by one or more transactions.
        """
        invoice = Invoice.objects.create(total=100.00)
        invoice.save()

        Transaction.objects.bulk_create([
            Transaction(invoice=invoice, amount=10.00),
            Transaction(invoice=invoice, amount=20.00),
        ])

        self.assertFalse(invoice.has_been_paid(), "Method should state invoice has not been paid.")
