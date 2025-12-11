# Pixel Pets - Teacher Solutions

## Overview
This is the **MEDIUM** level security challenge. Students learn about client-side storage manipulation and hidden endpoints.

**Estimated Time:** 25-35 minutes
**Skills Taught:** LocalStorage manipulation, URL parameters, JavaScript inspection, finding hidden pages

---

## Flag #1: LocalStorage Manipulation (9000+ Coins)
**Vulnerability:** Game state stored in localStorage can be modified

**Solution:**
1. Open DevTools (F12)
2. Go to Application tab > Local Storage
3. Find `pixelPetsGame`
4. Edit the JSON and change `coins` to 10000 or more
5. Refresh the page

**Alternative Console Method:**
```javascript
let game = JSON.parse(localStorage.getItem('pixelPetsGame'));
game.coins = 99999;
localStorage.setItem('pixelPetsGame', JSON.stringify(game));
location.reload();
```

**Teaching Point:** Never trust client-side storage for anything important. Validate all values on the server!

---

## Flag #2: Get the Dragon Pet
**Vulnerability:** Can modify localStorage to add items you didn't purchase

**Solution:**
1. Edit localStorage `pixelPetsGame`
2. Add `"dragon"` to the `items` array
3. Refresh the page

**Alternative:** Get 9999+ coins first, then buy it legitimately

---

## Flag #3: Max Out All Stats
**Vulnerability:** Stats can be directly modified in localStorage

**Solution:**
```javascript
let game = JSON.parse(localStorage.getItem('pixelPetsGame'));
game.happiness = 100;
game.energy = 100;
game.hunger = 0;  // 0 hunger = full
localStorage.setItem('pixelPetsGame', JSON.stringify(game));
location.reload();
```

---

## Flag #4: Admin Panel Access
**Location:** `admin.html` (link hidden at bottom of main page)

**Vulnerability:**
1. Hidden admin link in footer
2. Weak password stored in JavaScript
3. Common passwords also work

**Solutions:**
- Password: `pixelpets` (main password)
- Also accepts: `admin`, `admin123`, `password`

**Finding the Password in Code:**
1. Open DevTools > Sources
2. Find admin.html JavaScript
3. Search for "PASSWORD"
4. Find: `const ADMIN_PASSWORD = "pixelpets";`

**Teaching Point:**
- Never hide important links by making them small
- Never store passwords in JavaScript
- Never use weak/guessable passwords

---

## URL Parameter Tricks

### Debug Mode
Add `?debug=true` to the URL:
```
index.html?debug=true
```
This reveals hints in the console.

### Coin Manipulation
Add coins via URL (though less effective than localStorage):
```
index.html?coins=99999
```

---

## Common Student Approaches

1. **Inspect Element** - Can see the tiny admin link
2. **View Source** - Find the admin.html reference
3. **Console Hints** - Several hints printed to console
4. **Network Tab** - Can see all page resources

---

## Security Concepts Covered
1. **Client-Side Storage Attacks** - LocalStorage can be modified
2. **Hidden Endpoints** - Small links are still visible
3. **JavaScript Password Storage** - Passwords in JS are exposed
4. **Weak Authentication** - Easy-to-guess passwords
5. **URL Parameter Injection** - User input from URLs
