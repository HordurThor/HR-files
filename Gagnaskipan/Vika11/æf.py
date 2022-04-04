from sortedcontainers import SortedDict

class Contact:
    __slots__ = 'name', 'phone_number', 'email'
    
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactList:

    def __init__(self):
        self.main_map = dict()
        self.name_map = SortedDict()
        self.phone_map = dict()
        self.email_map = dict()


    def add_contact(self, name, phone, email):
        new_id = self._generate_id()
        self.main_map[new_id] = Contact(name, phone, email)
        self.name_map[name] = new_id
        self.phone_map[phone] = new_id
        self.email_map[email] = new_id

    def _generate_id(self):
        if len(self.main_map) == 0:
            return 0
        heighest_id = max(self.main_map.keys())
        heighest_id += 1
        return heighest_id

    def get_by_name(self, name):
        cont_id = self.name_map[name]
        return self.main_map[cont_id]

    def get_by_phone(self, phone):
        cont_id = self.phone_map[phone]
        return self.main_map[cont_id]

    def get_by_email(self, email):
        cont_id = self.email_map[email]
        return self.main_map[cont_id]

    def get_by_id(self, id):
        return self.main_map[id]

    def remove(self, id):
        cont = self.main_map[id]
        del self.name_map[cont.name]
        del self.phone_map[cont.phone_number]
        del self.email_map[cont.email]
        del self.main_map[id]

    def get_contacts_ordered_by_name(self):
        cont_list = []
        for name in self.name_map:
            cont_list.append(self.main_map[self.name_map[name]])
        return cont_list

contact_list = ContactList()
contact_list.add_contact("Hanna Hönnudóttir", "1234567", "hanna@hanna.is")
contact_list.add_contact("Jón Jónsson", "2345678", "jon@jon.is")
contact_list.add_contact("Anna Önnudóttir", "3456789", "anna@anna.is")
contact_list.add_contact("Guðmundur Guðmundsson", "4567890", "gummi@gummi.is")
contact_list.add_contact("Bryndís Bryndísardóttir", "0123456", "disa@disa.is")
some_contact_1 = contact_list.get_by_name("Anna Önnudóttir")
some_contact_2 = contact_list.get_by_phone("4567890")
some_contact_3 = contact_list.get_by_email("hanna@hanna.is")
ordered_contact_list = contact_list.get_contacts_ordered_by_name()
for contact in ordered_contact_list:
    print(contact.name)