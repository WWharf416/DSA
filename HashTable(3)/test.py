import unittest

# Import your PhoneBook and PhoneRecord classes here
from phonebook import PhoneBook, PhoneRecord

class TestPhoneBook(unittest.TestCase):

    # students need to have the functions, (i) create_phone_record and (ii) read records from the file (details.txt) in the
    # phonebook class implemention itself.

    def setUp(self):
        # Create a PhoneBook instance and load data from Details.txt
        self.phone_book = PhoneBook()
        # Students are requested to implement the read_records_from_file() method in your PhoneBook class
        self.phone_book.read_records_from_file("Details.txt")

    def test_add_and_fetch_contact(self):
        # Test adding a new contact and then fetching it
        new_contact_info = "John Doe,1234567890,Company ABC"
        new_contact = self.phone_book.create_phone_record(new_contact_info)
        self.phone_book.add_contact(new_contact)
        contacts = self.phone_book.fetch_contacts("John Doe")
        self.assertIn(new_contact, contacts)

    def test_add_and_delete_contact(self):
        # Test adding a new contact and then deleting it
        new_contact_info = "John Doe,1234567890,Company ABC"
        new_contact = self.phone_book.create_phone_record(new_contact_info)
        self.phone_book.add_contact(new_contact)
        self.assertTrue(self.phone_book.delete_contact("John Doe"))
        contacts = self.phone_book.fetch_contacts("John Doe")
        self.assertNotIn(new_contact, contacts)

    def test_delete_nonexistent_contact(self):
        # Test deleting a contact that doesn't exist (should not delete)
        nonexistent_contact_info = "Nonexistent Name,0000000000,Nonexistent Org"
        nonexistent_contact = self.phone_book.create_phone_record(nonexistent_contact_info)
        initial_contacts = self.phone_book.fetch_contacts("Nonexistent Name")
        self.assertFalse(self.phone_book.delete_contact("Nonexistent Name"))
        contacts_after_delete = self.phone_book.fetch_contacts("Nonexistent Name")
        self.assertEqual(initial_contacts, contacts_after_delete)

    def test_fetch_nonexistent_contact(self):
        # Test fetching a contact that doesn't exist (should return an empty list)
        contacts = self.phone_book.fetch_contacts("Nonexistent Name")
        self.assertEqual(len(contacts), 0)

    def test_add_multiple_contacts(self):
        # Test adding multiple contacts with different names
        new_contacts_info = [
            "Alice Smith,1111111111,Company X",
            "Bob Johnson,2222222222,Company Y",
        ]
        new_contacts = [self.phone_book.create_phone_record(info) for info in new_contacts_info]
        for contact in new_contacts:
            self.phone_book.add_contact(contact)
        for contact in new_contacts:
            contacts = self.phone_book.fetch_contacts(contact.get_name())
            self.assertIn(contact, contacts)

    def test_delete_multiple_contacts(self):
        # Test deleting multiple contacts with different names
        
        # fetch contacts with the name and store the first contact in the list in a variable
        first_contact_priya = self.phone_book.fetch_contacts("Priya Das")[0]
        first_contact_rohit = self.phone_book.fetch_contacts("Ritu Kumar")[0]

        self.assertTrue(self.phone_book.delete_contact("Priya Das"))
        self.assertTrue(self.phone_book.delete_contact("Ritu Kumar"))

        # Get the first contact again if any contacts are returned after fetching
        contacts_priya_after_delete = self.phone_book.fetch_contacts("Priya Das")
        contacts_rohit_after_delete = self.phone_book.fetch_contacts("Ritu Kumar")

        if len(contacts_priya_after_delete) > 0:
            first_contact_priya_after_delete = contacts_priya_after_delete[0]
        if len(contacts_rohit_after_delete) > 0:
            first_contact_rohit_after_delete = contacts_rohit_after_delete[0]

        # Check that the first contact after delete (if exists) is not the same as the first contact before deleting
        if len(contacts_priya_after_delete) > 0:
            self.assertNotEqual(first_contact_priya, first_contact_priya_after_delete)
        if len(contacts_rohit_after_delete) > 0:
            self.assertNotEqual(first_contact_rohit, first_contact_rohit_after_delete)

        # Also check that other contacts with the same names are not deleted
        contacts_priya_das = self.phone_book.fetch_contacts("Gupta")
        contacts_rohit_srivastava = self.phone_book.fetch_contacts("Kumar")
        self.assertGreaterEqual(len(contacts_priya_das), 1)
        self.assertGreaterEqual(len(contacts_rohit_srivastava), 1)

    def test_add_delete_fetch_combination(self):
        # Test a combination of add, delete, and fetch operations
        new_contact_info = "New Contact,9999999999,Test Company"
        new_contact = self.phone_book.create_phone_record(new_contact_info)
        self.phone_book.add_contact(new_contact)
        self.assertTrue(self.phone_book.delete_contact("New Contact"))
        contacts_after_delete = self.phone_book.fetch_contacts("New Contact")
        self.assertEqual(len(contacts_after_delete), 0)

    def test_fetch_contacts_with_multiple_words(self):
        # Test fetching contacts with multiple words in the query
        contacts = self.phone_book.fetch_contacts("Kumar")
        self.assertGreaterEqual(len(contacts), 1)

    def test_search_with_middle_name(self):
        # Test searching with a middle name
        contacts = self.phone_book.fetch_contacts("Kumar Mishra")
        self.assertGreaterEqual(len(contacts), 1)



if __name__ == '__main__':
    unittest.main()