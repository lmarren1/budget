class PromptSystem:
    def __init__(self):
        pass

    def welcome(self):
        print('-'*40
              + '\nWelcome to your automated budgeter!'
              + "\n\nType 'exit' to stop."
              + "\nType 'back' to go back a prompt"
              + "\nType 'help' for input options.\n"
              + '-'*40
              + '\n')

class Prompt(PromptSystem):
    def __init__(self):
        super().__init__(self)
        self._response = ''
        self._next = None
        self._prev = None

    def check_control_flow(self, answer):
        match answer:
            case 'exit':
                return
            case 'back':
                return
            case 'help':
                return
            
class FreePrompt(Prompt):
    def __init__(self):
        pass

    SOURCE = 'What was the source of this transaction? I.e., where did you purchase/earn from?\n'
    EXPENSE_NAME = 'What was the name of what you purchased?\n'
    TRANSACTION_AMOUNT = 'How much money was involved? Answer in $$$$.$$ format.\n'
    DESCRIPTION = 'Would you like to add a description? (ENTER/n)\n'
        
class SetPrompt(Prompt):
    def __init__(self):
        pass

    INCOME_EXPENSE = {'''Was this transaction an income or an expense?
                      Type (i/e).\n''': ['i', 'e']}
    INCOME_TYPE = {"""What income type was this?
                   Type 'help' for a list of income types.\n""": ['wages', 'loan', 'misc']}
    NECESSITY_LEVEL = {'''Was this expense necessary?
                       (ENTER/n/invest)\n''': ['', 'n', 'invest']}
    NECESSARY = {"""Great job for paying off a necessary expense.
                \nWhat NECESSARY expense type was this?
                Type 'help' for a list of necessary expense types.\n""": ['rent', 'utilties', 'groceries', 'travel']}
    UNNECESSARY = {"""Reflect on whether or not you're executing financial discipline.
                  \nWhat UNNECESSARY expense type was this?
                  Type 'help' for a list of unnecessary expense types.\n""": ['entertainment', 'restaurants', 'travel', 'merchandise']}
    INVESTMENT = {"""Self-investment is crucial.
                 \nWhat INVESTMENT expense type was this?
                  Type 'help' for a list of investment expense types.\n""": ['tennis', 'gym', 'academics']}

    def validate_response(self, prompt):
        question = ''
        valid_answers = []
        for key, value in prompt.items():
            question = key
            answers = value
        answer = input(question).lower().strip()
        if answer not in valid_answers:
            self.check_control_flow(answer)
        return answer
            
class PromptChain:
    def __init__(self, prompt):
        new_prompt = prompt
        self._head = new_prompt
        self._tail = new_prompt
        self._length = 1

    def append(self, prompt):
        new_prompt = prompt
        self._tail._next = new_prompt
        self._tail = new_prompt
        self._length += 1
        return True

    def print_prompts(self):
        temp = self._head
        while temp:
            print(temp._prompt)
            temp = temp._next

prompt_1 = FreePrompt()    
prompt_chain = PromptChain(prompt_1)
prompt_2 = SetPrompt()
prompt_chain.append(prompt_2)

temp = prompt_chain._head
while temp:
    response = temp.check_control_flow(FreePrompt.SOURCE)
    match response:
        case 'back':
            temp = temp._prev
        case 'exit':
            temp = prompt_chain._tail._next
        case 'help':
            temp = temp
        case _:
            temp = temp._next

