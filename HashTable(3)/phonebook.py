class PhoneRecord:
    def __init__(self, name, organisation, phone_numbers):
        self.name = name
        self.organisation = organisation
        self.phone_numbers = phone_numbers

    def get_name(self):
        return self.name

    def get_organisation(self):
        return self.organisation

    def get_phone_numbers(self):
        return self.phone_numbers


class HashTableRecord:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.next = None

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


class PhoneBook:
    HASH_TABLE_SIZE = 263

    def __init__(self):
        self.hash_table = [None] * PhoneBook.HASH_TABLE_SIZE

    def read_records_from_file(self,file):
        lines = []
        with open(file) as f:
            x = f.readlines()
            lines.append(x)
            lines = lines[0]
        
        for i in range(len(lines)):
            curline = lines[i].split(',')
            pres = PhoneRecord(curline[0],curline[-1].strip(),curline[1:-1])
            name = pres.get_name().split(' ')
            for e in name:
                key = self.compute_hash(e)
                hr = HashTableRecord(key,pres)
                if self.hash_table[key] is None:
                    self.hash_table[key] = hr
                else:
                    itr = self.hash_table[key]
                    while itr.next is not None:
                        itr = itr.next
                    itr.set_next(hr)
                    
    def create_phone_record(self, contact_info):
        name, num, org = contact_info.split(",")
        return PhoneRecord(name.strip(), org.strip(), [num.strip()])

    def compute_hash(self, string):
        sum = 0
        m = 263
        p = 1000000007
        x = 263
        for i in range(len(string)):
            sum += ord(string[i])*pow(x,i)%p
        return sum%m
        # Implement a hash function for strings
        # You can use Python's built-in hash function or implement a custom one

    def add_contact(self, record):
        name = record.get_name().split(' ')
        for e in name:
            key = self.compute_hash(e)
            hr = HashTableRecord(key,record)
            if self.hash_table[key] is None:
                self.hash_table[key] = hr
            else:
                itr = self.hash_table[key]
                while itr.next is not None:
                    itr = itr.next
                itr.set_next(hr)
        # Implement adding a contact to the phone book
        # You need to compute the hash for the record's name and insert it into the hash table

    def delete_contact(self, name):
        # Implement deleting a contact from the phone book
        # You need to find the record with the given name and remove it from the hash table
        lst = self.fetch_contacts(name)
        if len(lst)==0:
            return False
        target = lst[0]
        name = target.get_name().split(' ')
        for i in name:
            key = self.compute_hash(i)
            itr = self.hash_table[key]
            if itr.get_record() == target:
                self.hash_table[key] = itr.get_next()
            elif itr is not None:
                while itr.get_next() is not None:
                    if itr.get_next().get_record()==target:
                        itr.set_next(itr.get_next().get_next())
                        break
                    else:
                        itr = itr.get_next()
        return True

    def fetch_contacts(self, query):
        # Implement fetching contacts based on the query
        # You may need to split the query into words and hash them separately
        # Then, retrieve and merge the records from the appropriate hash table slots
        # Sort and return the merged records
        final = []
        query = query.split(' ')
        result = [[] for x in range(len(query))]
        def freq_apply(hr,num):
            if hr not in result[num]:
                result[num].append(hr)
            else:
                freq_apply(hr,num+1)
        for e in query:
            key = self.compute_hash(e)
            #print(key)
            itr = self.hash_table[key]
            while itr is not None:
                if e in itr.get_record().get_name().split(' '):
                    freq_apply(itr.get_record(),0)
                    #print(result)
                itr = itr.next
        for i in range(len(result)-1,-1,-1):
            for j in range(len(result[i])):
                if result[i][j] is not []:
                    final.append(result[i][j])
                    for k in range(i):
                        result[k].remove(result[i][j])
        return final