# Introduction to GitHub Workshop
#### Created by Kyle Gavin

## Overview
This repository hosts an introductory GitHub workshop focusing on basic GitHub operations from a **group perspective**. In this workshop we will be operating in teams to explore concepts like commits, pushing, branching, pull requests, merge conflicts, and collaboration best practices.

The repository consists of 3 files, main.py, majors.py, and students.py. main.py is where our script is reached in the terminal and is the root for execution. Within the main.py, we have our `if __name__ == '__main__': ` statement that allows us to execute functions or modify variables within main.py. majors.py and students.py are [object class files](https://docs.python.org/3/tutorial/classes.html) that determine the shape and attributes of students and majors. All the content within the 3 python files are for tutorial purposes for commiting (recording changes), pushing (submitting changes to a branch), and createing pull requests (merging two branches). 

In this tutorial, we will be using the PyCharm IDE by JetBrains to complete our tasks, if you do not already have pycharm community or pycharm professional installed, you can install the community version [here](https://www.jetbrains.com/pycharm/download/).

**Group sizes for this tutorial should be around 3-5 students!**

## Task One - Cloning the repository and adding collaborators
For this first task, we need to first elect a group leader to host the repository on their account. The established group leader or host will clone this template repository to their account, and set the visibility to public. Once the repository is cloned, the host will add all group members to the repo via the "collaborators" tab in the repo settings. Once group members have accepted the invitation, they will be able to clone and modify the hosts template and commit/push their changes. 

## Task Two - Accessing our remote repository in PyCharm IDE
For this task, we need to [generate access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to our personal github account to access our remote repository within the IDE. **This Task will be demonstrated live**

## Task Three - Our first commit and push - Resolving Merge Conflicts
A commit is a record or bookmark representing some change (addition or deletion) of code. Generally, commits should be small bite-sized changes (no pun intended). Commits are local changes, that can be reversed (this is more advanced material). A collection of commits that is working as intended can be pushed (sent to the remote repository as an official change). 

Lets get to work! 

Too start, each groupmember create a new branch from the main branch. Name this branch "add_[your name here]_to_students". Remember to "Checkout" your branch. When you checkout a branch, all your local commits will be sent to that respective branch, and your pushes will be sent to the remote branch. When you've checked out the new branch, in main.py there is a function called `student_init ` each group member go to the student_init function and add a new variable that stores a new student object with your information following the syntax for the Student object. For example: `new_student = Student("10643123","Kyle","Gavin",22,list_of_majors[0])` Note that in PyCharm if you hover above the object class reference you can see the structure, and type hints. Once your variable with your object are complete, lets record our first commit. After commiting that change, at the end of the `student_init` function add your new variable to the .extend function within the list parameter. Now, commit this change too. Once you're finished push your changes to the branch. Within the IDE, or on the GitHub web page, you will see a message that informs collaborators there is recent changes to a branch, GitHub offers you to create a pull request and merge. A pull request is a formal request to merge changes from a branch to the main branch. Pick a group member to submit their changes first, the changes will automatically merge into the main branch. Now, pick a second group member to create a pull request and merge their changes to the main branch. Notice on the GitHub or IDE interface there is a problem! The pull request has a merge conflict and cannot be automatically merged into the main branch. This happens when two branches modify the same file in two different branches. This goes against GitHub best practice! Now for the rest of the merge requests, we will need to manually resolve all these conflicts. For each group member with a merge conflict, click on the option to resolve, and inspect the differences between the main branch versus the branch we are trying to merge. Work on fixing this conflict with your group.  Once a conflict is manually resolved, you can merge, **however** you will typically want to pull your updated main and test it after resolving a merge conflict because there is no guarentee the code still works. As a group, work together on resolving all the merge conflicts and making the main branch have each group members student object variable, test your code at the end by using the `display_students ` function to see if there is any issues. 

## Task Four - Divide and Conquer - Feature Branching

In this task, assign group members to complete 1 task from the list, remember that each group member should create a new branch from main to complete the task.

- [ ] Add a department chair attribute to the "Major" class, make it an optional value. `self.department_chair = None`
- [ ] Add a active_courses attribute to the "Student" class to store a list of active courses `self.active_courses = []`
- [ ] Create a new class python file called "courses" that represents courses, include attributes such as instructor, course number, department code, classroom, meeting days and times. (see example below)
```
class Course:
  def __init__(self, crn: int, course_name: str, instructor_first_name: str, instructor_last_name: str,
               course_number: int, department_code: str):
               self.crn = crn
               self.course_name = course_name
               self.instructor_first_name = instructor_first_name
               self.instructor_last_name = instructor_last_name
               self.course_number = course_number
               self.department_code = department_code
               self.classroom = None
               self.meeting_days = None
               self.meeting_times = None
```
Notice that classroom, meeting days and times are optional because some courses do not have these.



After each task is completed, commit and push your code to each respective branch. Then, create a pull request and merge your changes to the main branch. Notice that since we are modifying two seperate files through this branching process, there is no merge conflict. Once these changes are all merged into main.

## Task Five - Expanded our features

At this point in the workshop, all the previous branches should be merged into main. Together as a group, we will work in a single branch to complete the next part of the courses feature we added in the previous step. 

Have one group member create a new branch and have each groupmember checkout the new branch. One group member will complete 1 task below in the new branch, commit and push their changes to the branch. When a sub-task has been completed, inform the rest of the group to "pull" changes from the new branch we created, and then have the next group member start the next task and repeat. During this process, you will notice that the code your group pushes will appear in your local repository. Push and pull basically synchronizes changes between locals, and allows us to work concurrently on the same file (as long as group members arent modifying the same functions or variables at the same time). 


- [ ] Add set_courses to students.py class
```
    def set_courses(self, course_list: list):
        self.active_courses = course_list
```
- [ ] Add add_courses to students.py class
```
    def add_courses(self, courses_to_add: list):
        self.active_courses.extend(courses_to_add)
```
- [ ] add a print formatter to the courses.py class

```
def __str__(self):
  return f"Course: {self.department_code}{self.course_number} | {self.course_name} | {self.crn} \nInstructor: {self.instructor_first_name} {self.instructor_last_name} \n ============================ "

```
Once these tasks, are completed, have one group member create a pull request and merge these new features into the main branch. 

## Task Six - Putting it all together

The final task is to implement our recent changes into our main.py file. For this task, similarly to task 5, have one group member create a new branch. In this branch practice collaborating as a team, and committing and pushing changes, and have the entire group pull changes after each change is pushed. 

- [ ] import the courses.py file in the main.py to interact and create new courses `from courses import Course`

- [ ] Implement the create_new_course function in main.py under the `create_new_major` and `create_new_student` functions.
```
def create_new_course(crn: int,course_name: str, instructor_first_name: str, instructor_last_name: str,
                      course_number: int, department_code: str) -> Course:
    new_course = Course(crn,course_name,instructor_first_name,instructor_last_name,course_number,department_code)
    return new_course
```
- [ ] Create a list to store pre-defined or newly added courses in the main.py file `list_of_courses = []`

- [ ] Create a `course_init` function with the `student_init` and `major_init` and create a set of pre-defined courses to work with.
```
def course_init():
  course_var_a = Course(11033,"Elements I","Marwan","Rasamny",120,"CSCI")
  course_var_b = Course(11021,"Elements II","Shilpa","Patel",121,"CSCI")
  course_var_b = Course(12041,"Data Structures II","Fatima","Boukari",210,"CSCI")
  course_var_d = Course(12095,"Computer Networking","Marwan","Rasamny",340,"CSCI")
  list_of_courses.extend([course_var_a, course_var_b, course_var_c, course_var_d])
```
- [ ] Create a `display_courses` function like the `display_students` and `display_majors` to print out all the courses. The print formatter recently added to the courses.py will allow them to be displayed nicely in the console. 

```
def display_courses():
  for course in list_of_courses:
    print(course)
    
```

- [ ] In the `if __name__ == '__main__':` statement, create a new student, and a new course. Use the set_courses method to initalize the students courses. 
Example:
```
    list_of_active_students.append(create_new_student("10643123","Kyle","Gavin",22,create_new_major(720392,"Computer Science","PEMACS")))
    print(list_of_active_students[0])
    list_of_courses.append(create_new_course(11011,"Elements II","Marwan","Rasamny",121,"CSCI"))
    print(list_of_courses[0])

    test_add_course = list_of_active_students[0]
    test_add_course.set_courses(list_of_courses)
    test_add_course.display_courses()
```

- [ ] In the `if __name__ == '__main__':` statement, practice adding additonal courses (without overwriting) by using the add_course method. 
Example:
```
    test_add_course.add_courses([create_new_course(11033,"Elements I","Marwan","Rasamny",120,"CSCI")])
    test_add_course.display_courses()
```


With these last touches complete, create a pull request and merge the final changes into main. 



## Summary and Conclusion

Awesome work, with this tutorial, you should be familar with the concepts of commiting, pushing, pulling, pull requests, merging, resolving merge conflicts, and feature branching!

You may have noticed that there was some features in majors.py and courses.py we never interacted with. As a bonus, continue working on implementing additonal features below for more practice!

- [ ] Add a set function for the Major class to set or replace a department chair.
- [ ] Add a set function for the Course class to set a classroom number.
- [ ] Add an add function for the Course class to add additional classroom numbers.
- [ ] Add a set function for the Course class to set meeting times.
- [ ] Add an add function for the Course class to add additional meeting times.
- [ ] Add a set function for the Course class to set the meeting days. 
- [ ] Add an add function for the Course class to add additional meeting days. 












