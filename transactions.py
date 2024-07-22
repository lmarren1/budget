

class TransactionSystem:
    def __init__(self):
        self.transactions = []

    def get_transactions(self):
        return self.transactions
    
    def get_categories(self):
        return self.categories

# class Category: 
#     def __init__(self):
#         self._income_categories = ['wages', 'loan', 'misc']
#         self._expense_categories = {'necessary': ['rent', 'utilties', 'groceries', 'travel'],
#                                    'unnecessary': ['entertainment', 'restaurants', 'travel', 'merchandise'],
#                                    'self-investment': ['tennis', 'gym', 'academics']}
#     def __str__(self):
#         pass
    
class Transaction:
    def __init__(self, date='None', source='None', amount='None', description='None'):
        self._date = date
        self._source = source
        self._amount = amount 
        self._description = description
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = value
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value

    def print_transaction(self):
        max_length = 0
        title = 'Transaction Summary:'

        for key, value in self.__dict__.items():
            if key != '_data' and value != 'None':
                key = key[1:]
                line = key + ' = ' + value
                if len(line) > max_length:
                    max_length = len(line)
        if len(title) > max_length: 
            max_length = len(title)

        top_bottom = '+' + '-' * (max_length + 2) + '+'
        print(top_bottom)
        print(f'| {title.ljust(max_length)} |')
        print(top_bottom)
        
        for key, value in self.__dict__.items():
            if key != '_data' and value != 'None':
                key = key[1:]
                line = key.capitalize() + ' = ' + value
                print(f'| {line.ljust(max_length)} |')
                
        print(top_bottom)

class Income(Transaction):
    def __init__(self, date='None', source='None', amount='None', description='None', income_type='None'):
        super().__init__(date, source, amount, description)
        self._income_type = income_type
    
    @property
    def income_type(self):
        return self._income_type
    
    @income_type.setter
    def income_type(self, value):
        self._income_type = value
    
class Expense(Transaction):
    def __init__(self, date='None', source='None', amount='None', description='None', expense_name='None', necessity_level='None'):
        super().__init__(date, source, amount, description)
        self._expense_name = expense_name
        self._necessity_level = necessity_level
  
    @property
    def expense_name(self):
        return self._expense_name
    
    @expense_name.setter
    def expense_name(self, value):
        self._expense_name = value
    
    @property
    def necessity_level(self):
        return self._necessity_level
    
    @necessity_level.setter
    def necessity_level(self, value):
        self._necessity_level = value
    
r = Income('1998')
r.print_transaction()
t = Transaction()
t.print_transaction()
s = Expense()
s.print_transaction()
