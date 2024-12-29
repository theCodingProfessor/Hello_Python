"""
The Lookup App
Dictionary for Quick Reference of Technology Terms
Lookup and add new definitions by keyword.
Author: Clinton Garwood
Date: November 2024
License: MIT
ChangeLog: Dictionary Values are appended with update method
"""
import os
import pickle


class Terms:
    """
    CLASS Terms built from Design Document
    """
    def __init__(self, term_keyword, as_defined):
        self.term_name = term_keyword
        self.definition = [as_defined]

    def set_term_name(self, term_name):
        self.term_name = term_name

    def set_definition(self, new_define):
        self.definition = new_define

    def get_term_name(self):
        return self.term_name

    def get_definition(self):
        return self.definition


def terms_menu():
    print(f"\n\t1) Lookup a Term")
    print(f"\t2) Add a Term")
    print(f"\t3) Update a Term")
    print(f"\t4) Exit")
    return


def main():
    print("\nTechnical Term Lookup App")
    pickle_filename = 'terms_dict.pkl'
    terms_dict = load_terms_dict(pickle_filename)

    while True:
        terms_menu()
        user_choice = get_terms_choice()

        if user_choice == '1':
            get_term(terms_dict)
        elif user_choice == '2':
            add_term(terms_dict)
        elif user_choice == '3':
            update_term(terms_dict)
        elif user_choice == '4':
            save_terms_dict(terms_dict, pickle_filename)
            print(f"\tExiting...")
            break
        else:
            print(f"\tInvalid choice. Please select again.")

    return


def load_terms_dict(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as read_file:
            terms_dict = pickle.load(read_file)
            print(f"\tLoaded terms from {filename}")
    else:
        terms_dict = {}
        print(f"\tNo existing data found. Starting fresh.")
    return terms_dict


def save_terms_dict(terms_dict, filename):
    with open(filename, 'wb') as save_terms:
        pickle.dump(terms_dict, save_terms)
        print(f"\tData saved to {filename}")
    return


def get_terms_choice():
    user_choice = input("\tPlease select: ")
    return user_choice


def add_term(terms_dict):
    term_name = input(f"\tPlease enter the term-name: ").strip()
    new_define = input(f"\tPlease enter the definition: ")
    if term_name in terms_dict:
        print(f"\tTerm {term_name}, already exists. Consider updating the term instead.")
    else:
        terms_dict[term_name] = [new_define]
        print(f"\tTerm {term_name}, added successfully.")
    return


def update_term(terms_dict):
    term_name = input(f"\tPlease enter the term-name: ").strip()
    if term_name in terms_dict:
        new_define = input("\tPlease enter the new definition: ")
        terms_dict[term_name].append(new_define)
        print(f"\tDefinition added to {term_name}")
    else:
        print(f"\tTerm {term_name}, not found. Consider adding the term first.")
    return


def get_term(terms_dict):
    term_name = input(f"\tPlease enter the term-name: ")
    if term_name in terms_dict:
        print(f'\n\t{term_name} : {terms_dict[term_name]}')
    else:
        print(f"\tTerm {term_name} not found.")
    return


if __name__ == '__main__':
    main()
