# PollDaddy Voter

The original file is created by Alex Beals, git username: dado3212.

It was then edited to add tor functionality


This is pretty easy to use.  Just download the Python script, and customize the variables for what form/answer/number of votes.
Be sure to add your tor hash password found in torrc file.  

It needs Python 2.7.6. // Updated to Python 3.
Also be sure to do pip install requests and pip install TorRequest

### Disclaimer
This script will **may not -- I have not tested it with new tor functionality** work on polls that do not allow multiple votes from one person.  The useragents and proxy settings will help try and mask your mass voting, but they will not get you around IP blocks.  If someone wants to give a shot at forking this and adding that functionality, I will be happy to merge it in.

### Example
You want to vote on this poll: https://polldaddy.com/poll/9206448/ for the answer "It's a great way to keep kids in line during a crazy time of year.", and you want to vote 1000 times.  The poll_id comes from the url: <code>https://polldaddy.com/poll/<b>9206448</b>/</code>.  The answer_id comes from the looking at the source code for the associated checkbox: <code>\<input type="radio" name="PDI_answer" id="PDI_answer41930288" value="**41930288**"></code>.


Thus, you would want the variables to be set to:
```
poll_id = 9206448
answer_id = 41930288
number_of_votes = 1000
```
