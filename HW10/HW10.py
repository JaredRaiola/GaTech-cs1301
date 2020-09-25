#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - OOP - due Tuesday, November 21, 2017
"""
__author__ = "Jared Raiola"
__collaboration__ = """ I worked on the homework assignment alone, using only this semester's course materials. """


class User:

    """
    Write a constructor for a User below.
    It should have the following attributes:
    name: string
    skills: dictionary that is empty by default if not specified during instantiation
    company: should be None until user is hired by a company (see Company class)
    connections: list that is empty to begin with 

    The function header has been given to you below.
    """
    def __init__(self, name, skills = None):
        self.name = name
        self.skills = skills
        self.company = None
        self.connections = []

    """
    Function Name: __repr__
    Return a string representation of a User
    """
    def __repr__(self):
        if self.skills != None:
            count = 0
            for i in self.skills.keys():
                if count == 0:
                    skill = i
                    hm = len(self.skills[i])
                    count += 1
                elif (len(self.skills[i]) == hm) and i < skill:
                    skill = i
                    hm = len(self.skills[i])
                elif len(self.skills[i]) > hm:
                    skill = i
                    hm = len(self.skills[i])
        connections = len(self.connections)
        if self.company == None and self.skills == None:
            return "A User named {}, unemployed, with {} connections".format(self.name, connections)
        elif self.company == None:
            return "A User named {}, unemployed, skilled in {}, with {} connections".format(self.name, skill, connections)
        elif self.skills == None:
            return "A User named {}, employed by {}, with {} connections".format(self.name, self.company.name, connections)
        else:
            return "A User named {}, employed by {}, skilled in {}, with {} connections".format(self.name, self.company.name, skill, connections)
    
    """
    Function Name: endorse
    Endorse another user for a skill. If the other user does not already have this skill,
    add it to their dictionary along with the endorsement.
    """
    def endorse(self, other, skill):
        if other.skills == None:
            other.skills = {}
        if skill not in other.skills:
            other.skills = {}
            other.skills[skill] = [self]
        else:
            other.skills[skill].append(self)

    """
    Function Name: connect
    Connect with another User object. Add the other user to your network and add yourself
    to their network. If you are already connected, nothing should happen.
    """
    def connect(self, other):
        if other not in self.connections:
            self.connections.append(other)
            other.connections.append(self)

    """
    Function Name: add_skill
    Add a skill to a users dictionary of skills. Skills begin with no endorsements.
    Nothing should happen if the skill is already in a user's skills.
    """
    def add_skill(self, skill):
        self.skills = {}
        if skill not in self.skills:
            self.skills[skill] = []

    """
    Function Name: connect_with_coworkers
    Connect with all the users in the network who work for the same company (if not already connected).
    Nothing should happen if the user is unemployed.
    """
    def connect_with_coworkers(self, network):
        for user in network.users:
            if self.company == user.company and self.company != None:
                connect(user)

    
class Company:


    """
    Write a constructor for a Company below.
    It should have the following attributes:
    name: string
    preferred skills: list of skills
    employees: a list of all the User objects employed at the company. Should begin as empty.

    The function header has been given to you below.
    """
    def __init__(self, name, preferred_skills):
        self.name = name
        self.preferred_skills = preferred_skills
        self.employees = []


    """
    Function Name: __repr__
    Return a string representation of a Company
    """
    
    def __repr__(self):
        return "A Company called {} with {} employee(s)".format(self.name, len(self.employees))

    """
    Function Name: recruit
    Return a list of all the users in a network that have at least one of the 
    company's preferred skills
    """
    def recruit(self, network):
        userlist = []
        for user in network.users:
            if user.skills != None:
                for skill in  user.skills.keys():
                    if skill in self.preferred_skills:
                        userlist.append(user)
                        break
        return userlist
                    
                

    """
    Function Name: hire
    Add a user to the Company's list of employees. Also change the user's employer attribute
    to Company. Do nothing if the user is already an employee at the Company
    """
    def hire(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            employee.company = self


    """
    Function Name: fire
    Remove a user to the Company's list of employees. Also change the user's employer attribute
    to None. Do nothing if the user is not an employee of Company
    """
    def fire(self, employee):
        if employee.company.name == self.name:
            self.employees.remove(employee)
            employee.company = None

    """
    Function Name: downsize
    Find the employees with the fewest total endorsements for their
    skills (if there are ties, get the ones with names earliest in the
    alphabet) and fire them until Company is down to target_num employees.
    If the target_num is greater than the current number of employees, 
    nothing should happen
    """
    def downsize(self, target_num):
        while len(self.employees) > target_num:
            first = 0
            for employee in self.employees:
                count = 0
                for value in employee.skills.values():
                    count += len(value)
                if first == 0:
                    smallest = count
                    person = employee
                elif count == smallest and person.name < employee.name:
                    smallest = count
                    person = employee
                elif count < smallest:
                    smallest = count
                    person = employee
            self.employees.remove(person)
            person.company = None


class LinkedIn:

    """
    Write a constructor for the LinkedIn class below.
    It should have the following attributes:
    users: a list of users in the LinkedIn network. The list should begin as an empty list when the LinkedIn object is instantiated

    The function header has been given to you below.
    """
    def __init__(self):
        self.users = []

    """
    Function Name: __repr__
    Return a string representation of a LinkedIn object
    """
    def __repr__(self):
        return "A LinkedIn network with {} users.".format(self.users)

    """
    Function Name: search
    Return list of User objects with specified skill endorsed more than num times
    """
    def search(self, skill, num):
        have_more = []
        for i in self.users:
            if skill not in i.skills:
                continue
            else:
                if len(i.skills[skill])>num:
                    have_more.append(i)
        return have_more

    """
    Function Name: find_unemployed
    Return list of all the User objects that are unemployed
    """
    def find_unemployed(self):
        unemp = []
        for i in range(len(self.users)):
            if self.users[i].company == None:
                unemp.append(self.users[i])
        return unemp

    """
    Function Name: strengthen_network
    Return the number of User objects that have less than 3 connections
    """
    def strengthen_network(self):
        count = 0
        for user in self.users:
            if len(user.connections) < 3:
                count += 1
        return count

    """
    Function Name: add_to_network
    Add all User objects in users to LinkedIn network if they arenâ€™t already in it.
    Do not add duplicates.
    """
    def add_to_network(self, users):
        for i in users:
            if i not in self.users:
                self.users.append(i)


    """
    Function Name: get_employees
    Return list of all the User objects that work for the specified company
    """
    def get_employees(self, company):
        work = []
        for i in range(len(self.users)):
            if self.users[i].company == company:
                work.append(self.users[i])
        return work
