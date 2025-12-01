# Learning Process Documentation
## Citizen Wellness Portal™ - PROCESS.md

**Citizen Name:** Joshua Eckman  
**Date Started:** [11/25/25]  
**Date Completed:** [12/1/2025]  
**Total Time Spent:** [? hours]

---

## Part 1: Initial Understanding

### What I Knew Before Starting
> Before this assignment, my understanding of Streamlit was:
> - I have done some Streamlit in my Python class, but it has been a while and I don't remember much ot it.

### First Impressions
> After reading the assignment and doing initial research:
> - From the last time I vibe-coded, the prompting and iteration seemed to be hit or miss when it comes to functionality, but there were results that worked.
> - Learning a new library can be pretty difficult, espesialy for me.

---

## Part 2: LLM-Assisted Learning

Document at least 4-5 significant prompts you used. Show iteration where you refined your questions.

### Prompt 1: [Topic - e.g., "Understanding Streamlit's Execution Model"]

**Initial Prompt:**
```
[I'm a Flask developer learning Streamlit. Explain the key differences in how these frameworks work. Specifically: 1. How does Streamlit handle user interactions vs Flask's routes? 2. What happens when a user clicks a button in Streamlit? 3. Why do I need st.session_state when I didn't need anything special for variables in Flask?]
```

**Key Insights from Response:**
> [A lot of it was simmiler to what we learned in class, Flask being a Request/response model and requires HTML knowledge. While Sreamlit is mostly Python providing both its functionality and UI.]

**Follow-up Prompt (if any):**
```
[If you needed clarification or went deeper]
```

**What I Understood After This Exchange:**
> [Summarize your understanding]

---

### Prompt 2: [Topic - e.g., "Session State Basics"]

**Initial Prompt:**
```
[Show me how st.session_state works in Streamlit. I need to:
1. Store whether a user is logged in (boolean)
2. Store the logged-in username (string)
3. Make these persist when the user clicks buttons or interacts with the app Include a minimal example.]
```

**Key Insights from Response:**
> [Session state keys must be initalized first if you intend for them to persist between reruns, ChatGPT also
> recomends using if statments to ensure the key exists before creating them to avoid something called a KeyError.]

**Follow-up Prompt (if any):**
```
[If you needed clarification]
```

**What I Understood After This Exchange:**
> [Summarize]

---

### Prompt 3: [Topic - e.g., "Building the Login Form"]

**Initial Prompt:**
```
[I'm building a Streamlit app with login/registration. I want to store 
users in st.session_state as a dictionary. Show me how to:
1. Initialize the users dict if it doesn't exist
2. Add a new user during registration
3. Check credentials during login
4. Handle errors (user already exists, wrong password, etc.)]
```

**Key Insights from Response:**
> [The result was that it did more then I indended, as it created a tab based menu containing a
> Login menu, Registration menu, and a Debug menu. The Debug menu contains the user profiles created
> during the runtime of the program.]

**What Worked vs. What I Had to Modify:**
> [The code worked and did more than I prompted for it to do. \[See above\]]

---

### Prompt 4: [Topic - e.g., "Debugging an Issue"]

**The Problem I Was Facing:**
> [As far I a am awware, there ar not many problems, or at least the problems that are present have
> been adressed in previous iterations.]

**Prompt I Used:**
```
[Your prompt asking for help]
```

**Solution/Insight:**
> [What fixed it?]

---

### Prompt 5: [Additional Topic]

**Prompt:**
```
[Your prompt]
```

**What I Learned:**
> [Key takeaway]

---

## Part 3: Challenges and Resolutions

Document at least 2-3 significant challenges you faced.

### Challenge 1: [Double Click Buttons]

**What Happened:**
> [For some reson you had to press the buttons twice for them to work.]

**What I Tried That Didn't Work:**
> [List approaches that failed - this is valuable!]
> - Attempt 1: I asked my AI of choice to fix it, though it didn't seems
> - to solve the problem and just messed up the layout of the application.
> - Attempt 2: ...

**What Finally Worked:**
> [I decited to revert to the original program before it attempted to "fix" the problem.]

**What I Learned:**
> [Not every prompt will solve the problem you asked it to fix.]

---

### Challenge 2: [Above and Behond]

**What Happened:**
> [Though it wasn't exactly a challenge, the AI did seem to do more than it was asked,
> resulting in me having to skip steps and reorienting in the step I was on.]

**What I Tried:**
> [There wasn't much for me to do unless I asked it specifically to avoid doing more than asked.]

**Resolution:**
> [I decided to go along with it and do what I could to finish the assignment.]

**Lesson Learned:**
> [Insight]

---

### Challenge 3: [Brief Title]

**What Happened:**
> [Description]

**Resolution:**
> [What worked]

---

## Part 4: Flask vs Streamlit Comparison

### Similarities I Noticed
> [What felt familiar coming from Flask?]
> - Aside from using a command to start the program I am not really sure.
> - ...

### Key Differences
> [What's fundamentally different?]
> - Definitely the amout of HTML used
> - Also I seemed to understand the Streamlit functions a lot more.

### What Surprised Me Most
> [I was caught offguard when it programed more than I asked for it to do.
> \(Sorry I keep mentioning this\)]

### When I'd Choose Streamlit Over Flask
> [Based on your experience, when would each be better?]
> - Streamlit is better for: ...
> - Flask is better for: ...

---

## Part 5: Reflection

### What I'd Do Differently Next Time
> [I would ask the AI for more specific outputs rather than accept the ones
> that do more than I asked for.]

### Most Valuable Thing I Learned
> [Having defind expectation for what you want from you functions can help ensure smooth development.]

### Questions I Still Have
> [None that I can think of.]

### Self-Assessment of Learning Process
> Rate yourself (1-5) on each:
> - Prompt quality/iteration: [3] / 5
> - Persistence when stuck: [4] / 5
> - Documentation thoroughness: [2] / 5
> - Understanding vs. copying: [3] / 5

---

## Part 6: Resources Used

### AI Tools
- [ChatGPT]
- [4-5]

### Documentation Referenced
- [List any official docs, Stack Overflow, tutorials, etc.]

### Help from Others
- [Mr. Norris]

---

**Note:** This document is worth 30% of your grade. Thorough, honest documentation of your learning process demonstrates the metacognitive skills this assignment is designed to develop.
