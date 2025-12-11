# CryptoVault Bank - Teacher Solutions

## Overview
This is the **HARD** level security challenge. Students learn about cookie manipulation, IDOR vulnerabilities, and combining multiple exploits.

**Estimated Time:** 40-60 minutes
**Skills Taught:** Cookie manipulation, IDOR attacks, privilege escalation, hidden endpoints

---

## Flag #1: Cookie Manipulation (Become Admin)
**Vulnerability:** User role stored in client-side cookie

**Solution:**
1. Open DevTools (F12)
2. Go to Console
3. Type: `document.cookie = "user_role=admin"`
4. Refresh the page
5. Visit `admin-panel.html`

**Alternative - Application Tab:**
1. Go to Application > Cookies
2. Find `user_role` cookie
3. Change value from `user` to `admin`
4. Refresh

**Teaching Point:** Never use client-side cookies for authorization decisions. Always verify roles on the server!

---

## Flag #2: IDOR (Access Other Accounts)
**Vulnerability:** Account ID passed in URL with no server-side validation

**Solution:**
1. Login with any account (e.g., Account 1001, PIN: 1234)
2. Go to dashboard
3. Change URL from `?account=1001` to `?account=1002`
4. View Jane Smith's account without her PIN!

**Accessing Admin Account:**
```
dashboard.html?account=9999
```

**Teaching Point:** IDOR (Insecure Direct Object Reference) is a top OWASP vulnerability. Always validate that users can only access their own data!

---

## Flag #3: Hidden Debug Page
**Location:** `debug.html`

**Vulnerability:** Debug/development page left accessible in production

**Solution:**
1. Look at the footer links on the main page
2. Notice `debug.html` link
3. Visit `/debug.html`
4. See all user credentials exposed!

**What's Exposed:**
- All account PINs
- Admin PIN: `0000`
- Admin Account ID: `9999`

**Teaching Point:** Always disable debug endpoints before going to production. Use environment variables to control access.

---

## Flag #4: Admin Account Access
**Vulnerability:** Combination of debug info + IDOR + hidden UI element

**Solution:**
1. Learn admin credentials from debug.html
   - Account: 9999
   - PIN: 0000
2. On the login page, click the grayed-out "Admin Account" item to unlock it in the dropdown
3. Enter PIN: 0000 to login as admin, OR
4. Just change URL to `?account=9999` (IDOR attack)

**Alternative Console Method:**
```javascript
const select = document.getElementById('accountSelect');
const option = document.createElement('option');
option.value = "9999";
option.textContent = "System Admin";
select.appendChild(option);
select.value = "9999";
```

---

## Flag #5: Ultimate Hack (Transfer from Admin)
**Vulnerability:** Transfer function doesn't verify ownership

**Solution:**
1. Access admin dashboard via `?account=9999`
2. Use the transfer form
3. Transfer any amount to any account
4. The system "processes" the transfer

**Teaching Point:** Every action that modifies data should verify:
- User identity
- User permissions
- Ownership of the source resource

---

## All Account Credentials

| Account | Name | PIN | Balance |
|---------|------|-----|---------|
| 1001 | John Doe | 1234 | $5,000.00 |
| 1002 | Jane Smith | 5678 | $12,500.50 |
| 1003 | Bob Wilson | 9999 | $750.25 |
| 9999 | System Admin | 0000 | $999,999.99 |

---

## Attack Chain Example

A skilled attacker might chain these vulnerabilities:

1. **Reconnaissance**: Find `debug.html` and get all credentials
2. **Privilege Escalation**: Set `user_role=admin` cookie
3. **IDOR Attack**: Access `?account=9999`
4. **Data Exfiltration**: Transfer admin funds to attacker-controlled account

---

## Console Hints Available

Each page has console hints:
```javascript
// index.html
"Try: document.cookie = 'user_role=admin'"

// dashboard.html
"Check the URL - what's in ?account=XXXX?"

// debug.html
"Admin PIN: 0000"
```

---

## Security Concepts Covered

1. **Cookie-Based Authorization Flaws**
   - Cookies can be modified by users
   - Role information should be verified server-side

2. **IDOR (Insecure Direct Object Reference)**
   - CWE-639
   - Access control must verify object ownership

3. **Information Disclosure**
   - Debug endpoints expose sensitive data
   - Development tools left in production

4. **Privilege Escalation**
   - Becoming admin through cookie manipulation
   - Accessing admin resources via IDOR

5. **Broken Access Control**
   - OWASP Top 10 #1
   - Transfer function lacks authorization checks

---

## Discussion Questions for Class

1. In a real application, where should user roles be stored?
2. How could the transfer function be made secure?
3. What's the difference between authentication and authorization?
4. Why is "the client can be trusted" a dangerous assumption?
5. How would a penetration tester report these vulnerabilities?

---

## Real-World Examples

- **IDOR:** Instagram bug allowed viewing private photos by changing photo IDs
- **Cookie Manipulation:** Old versions of many PHP apps stored user roles in cookies
- **Debug Pages:** Numerous breaches from exposed debug endpoints
