import csv
import datetime as dt

now = dt.datetime.now()
today = now.strftime('%y-%m-%d') 

def record_set_response(response_data, question, prompt, answer_options = []):
    datum = input(prompt).lower().strip()
    if datum == '':
        datum = 'y'
        print(f'Your choice of was confirmed.')
    while datum not in answer_options:
        match datum:
            case 'back':
                question = question[-2]
                return
            case 'help':
                print('The answer options are:\n')
                for element in answer_options:
                    print(element)
                print('')
                record_set_response(response_data, prompt, answer_options)
                return
            case 'exit':
                print('You have exited your automated budgeter.')
                question = 'end'
                return
            case _:
                datum = input('You entered an invalid answer.\n' + prompt).lower().strip()
    response_data.append(datum)
    return 'valid'

def record_free_response(response_data, prompt):
    data = []
    datum = input(prompt).lower().strip()
    if (datum == 'exit'):
        return 'exit'
    if (datum == 'back'):
        return 'back'
    record_set_response(data, f'Are you sure this is what you want to input? ("{datum}") - Press ENTER or type n.\n', ['y', 'n'])
    if (data[0] == 'y'):
        response_data.append(datum)
        return 'valid'
    record_free_response(response_data, prompt)
    return 'valid'

def check_response(response):
    match response:
        case 'valid':
            question = 'next'
        case 'exit':
            transaction_data.clear()
            transaction_prompts.clear()
            question = 'end'
        case 'back':
            if len(transaction_data) > 0:
                transaction_data.pop(len(transaction_data) - 1)
            question = ''
    
# Prompt user to enter data
print('-'*40
      + '\nWelcome to your automated budgeter!'
      + "\n\nType 'exit' to stop."
      + "\nType 'back' to go back a prompt"
      + "\nType 'help' for input options.\n"
      + '-'*40
      + '\n')

transaction_data = []
transaction_prompts = []
date = ''

def collect_transaction(transaction_data):
    transaction_prompts.append('source')
    if transaction_prompts[-1] == 'source':
        check_response(record_free_response(transaction_data, 'What was the source of this transaction? I.e., where did you purchase/earn from?\n'))

    if record_set_response(transaction_data, 'Was this transaction an income or an expense? Type (i/e).\n', ['i', 'e']): 
        transaction_data.clear()
        transaction_prompts.clear()
        return
    transaction_prompts.append('income/expense: ')
    if transaction_data[1] == 'i':
        if record_set_response(transaction_data, "What income type was this? Type 'help' for a list of income types.\n", 
                       ['wages', 'loan', 'misc']): 
            transaction_data.clear()
            transaction_prompts.clear()
            return
        transaction_prompts.append('income type: ')
    else:
        if record_free_response(transaction_data, 'What was the name of what you purchased?\n'):
            transaction_data.clear()
            transaction_prompts.clear()
            return
        transaction_prompts.append('expense name: ')
        if record_set_response(transaction_data, "Was this expense necessary? (ENTER/n/invest)\n",
                              ['y', 'n', 'invest']): 
            transaction_data.clear()
            transaction_prompts.clear()
            return
        transaction_prompts.append('necessity level: ')
        match transaction_data[3]:
            case 'yes':
                if record_set_response(transaction_data, "Great job for paying off a necessary expense.\nWhat NECESSARY expense type was this? Type 'help' for a list of necessary expense types.\n",
                               ['rent', 'utilties', 'groceries', 'travel']): 
                    transaction_data.clear()
                    transaction_prompts.clear()
                    return
            case 'no': 
                if record_set_response(transaction_data, "Reflect on whether or not you're executing financial discipline.\nWhat UNNECESSARY expense type was this? Type 'help' for a list of unnecessary expense types.\n",
                               ['entertainment', 'restaurants', 'travel', 'merchandise']): 
                    transaction_data.clear()
                    transaction_prompts.clear()
                    return
            case 'invest':
                if record_set_response(transaction_data, "Self-investment is crucial.\nWhat INVESTMENT expense type was this? Type 'help' for a list of investment expense types.\n",
                               ['tennis', 'gym', 'academics']): 
                    transaction_data.clear()
                    transaction_prompts.clear()
                    return
        transaction_prompts.append('expense category: ')
    if record_free_response(transaction_data, 'How much money was involved? Answer in $$$$.$$ format.\n'): 
        transaction_data.clear()
        transaction_prompts.clear()
        return
    transaction_prompts.append('transaction amount: ')
    return

collect_transaction(transaction_data)

if len(transaction_data) > 0:
    check_data = []


def transaction_summary(transaction_prompts, transaction_data):
    msg = '-'*40 + '\nTransaction Summary:\n' + '-'*40
    for i in range(len(transaction_data)):
        msg += '\n'
        msg += transaction_prompts[i]
        msg += transaction_data[i]
    msg += '\n'
    msg += '-'*40
    msg += '\n'
    print(msg)

transaction_summary(transaction_prompts, transaction_data)
record_set_response(check_data, 'Would you like to add this to the dataset? (y/n)\n', ['y', 'n'])
if (check_data[0] == 'n'): 
    check_data.clear()
    record_set_response(check_data, 'Would you like to redo the transaction or exit? (redo/exit)\n', ['redo', 'exit'])
    if (check_data[0] == 'redo'):
        check_data.clear()
        transaction_data.clear()
        collect_transaction(transaction_data)
if (check_data[0] == 'y'):
    # start csv

    check_data.clear()
    record_set_response(check_data, 'Would you like to record another transaction? Type ENTER if yes, no if no.\n', ['y', 'no'])
    if (check_data[0] == 'y'):
        transaction_data.clear()
        collect_transaction(transaction_data)

    filepath = 'C:/Users/Luke\ Marren/OneDrive/Desktop/projects/budget/' + date + '.csv'