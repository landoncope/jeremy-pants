# EagleGrade Student Portal - Teacher Solutions

## Overview
This is the **MEDIUM** level security challenge (Challenge #2). Students learn about cookie manipulation, IDOR attacks, weak authentication, and hidden endpoints.

**Estimated Time:** 20-30 minutes
**Skills Taught:** Cookie manipulation, URL parameter tampering (IDOR), finding hidden pages, weak password exploitation

---

## Flag #1: Cookie Manipulation (Change Role to Teacher)
**Vulnerability:** User role is stored in a client-side cookie that can be modified

**Solution:**
1. Open DevTools (F12)
2. Go to Application tab > Cookies
3. Find the `role` cookie
4. Change its value from `guest` or `student` to `teacher`
5. Refresh the page or visit teacher.html

**Alternative Console Method:**
```javascript
document.cookie = "role=teacher";
```

**Teaching Point:** Never trust client-side data for authorization. Always verify roles on the server!

---

## Flag #2: Login as Teacher
**Vulnerability:** Weak password, exposed teacher account, and hidden UI element

**Solution:**
1. On the login page, notice the grayed-out teacher item at the bottom of the "Registered Students" list
2. Click on "Mr. Thompson (Teacher)" - this adds the teacher option to the dropdown
3. The password is `teacher` (also shown in debug.html)
4. Log in successfully

**Finding the Password:**
- Console hints mention common passwords
- The debug page exposes all passwords
- The teacher dashboard has a note with the password

**Alternative Method (Advanced):**
Students can also manually add the option via console:
```javascript
const select = document.getElementById('studentSelect');
const option = document.createElement('option');
option.value = "9999";
option.textContent = "Mr. Thompson";
select.appendChild(option);
select.value = "9999";
```

**Teaching Point:**
- Never use weak, predictable passwords
- Teacher accounts should have strong passwords
- Sensitive information shouldn't be exposed in client-side code
- Disabled/hidden UI elements can often be re-enabled

---

## Flag #3: IDOR Attack (View Another Student's Grades)
**Vulnerability:** Student ID is passed in the URL without proper authorization checks

**Solution:**
1. Log in as any student (e.g., Alex Johnson, ID: 1001, Password: 1001)
2. Go to the grades page (you'll be at grades.html?id=1001)
3. Change the URL to a different student ID:
   - `grades.html?id=1002` (Maria's grades)
   - `grades.html?id=1003` (James's grades)
   - `grades.html?id=1004` (Emma's grades)
   - `grades.html?id=9999` (Teacher's page)

**Teaching Point:**
- IDOR (Insecure Direct Object Reference) is a top web vulnerability
- Always verify the logged-in user has permission to access the requested resource
- Don't rely on obscurity for security

---

## Flag #4: Find the Hidden Debug Page
**Location:** `debug.html` (linked in footer, but easy to miss)

**Solution:**
- Look in the footer links (they're very faint)
- Try common debug page names: debug.html, admin.html, test.html
- Check the HTML source code for hidden links

**What Students Find:**
- Database credentials (exposed!)
- All user passwords in plain text
- Current cookie values

**Teaching Point:**
- Debug pages should NEVER be accessible in production
- Remove or protect all debug endpoints before deploying
- Never store passwords in plain text
- Use environment variables for sensitive config

---

## Student Passwords (For Reference)
| Student | ID | Password |
|---------|-----|----------|
| Alex Johnson | 1001 | 1001 |
| Maria Garcia | 1002 | maria123 |
| James Wilson | 1003 | password |
| Emma Davis | 1004 | emma2024 |
| Mr. Thompson | 9999 | teacher |

---

## Common Student Approaches

1. **View Source** - Find the footer links to debug.html
2. **Console Hints** - Several hints are printed in the browser console
3. **Try Common Passwords** - Many students try "password", "1234", etc.
4. **URL Manipulation** - Students often notice the ?id= parameter
5. **Cookie Inspection** - Application tab shows editable cookies

---

## Security Concepts Covered

1. **Cookie Manipulation** - Client-side cookies can be modified
2. **IDOR (Insecure Direct Object Reference)** - Accessing resources by changing IDs
3. **Weak Authentication** - Predictable/simple passwords
4. **Hidden Endpoints** - Debug/admin pages left accessible
5. **Information Disclosure** - Sensitive data exposed in client code
6. **Authorization vs Authentication** - Being logged in ≠ having permission

---

## Discussion Questions

1. How could the developers have prevented the cookie manipulation attack?
   - *Answer: Verify roles on the server, use signed/encrypted session tokens*

2. What's wrong with storing user passwords in JavaScript?
   - *Answer: Anyone can view them in the browser, they're not encrypted*

3. Why is it dangerous to leave debug pages accessible?
   - *Answer: They often contain sensitive information, credentials, or admin functions*

4. How should the grades page verify you can view a student's grades?
   - *Answer: Check on the server that the logged-in user is either that student or a teacher*

---

## Extending the Challenge

If students finish quickly, challenge them to:
1. Find ALL the passwords without using the debug page
2. Figure out how to log in as every student
3. Explain how each vulnerability could be fixed
4. Think of other ways they could attack this system
