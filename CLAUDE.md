# CLAUDE.md - AI Assistant Instructions for Computer Science Class

## Project Context
This is Brother Cope's "Exploring Computer Science" class materials repository. The class is for high school students (grades 9-12) with mixed experience levels. Brother Cope has a casual, engaging teaching style with lots of hands-on activities.

## Class Information
- **Teacher**: Brother Cope (Landon Cope)
- **Class Name**: Exploring Computer Science
- **Repository**: jeremy-pants (inside joke from Day 1)
- **Students**: Mix of freshmen through seniors, varying tech experience
- **Class Duration**: 75 minutes with a 5-minute break
- **Teaching Style**: Casual, uses real-world examples, lots of live demos, minimal lecturing

## Main Index Page (GitHub Pages)

### Purpose
The `index.html` file in the root directory serves as the main landing page for GitHub Pages, providing centralized access to all class materials.

### Structure
- **Header**: Class title, subtitle, and repository info
- **Day Cards Grid**: Visual cards for each class day showing:
  - Day number and title
  - Topics covered
  - Completion status (checkmark for completed days)
  - Links to materials (slides, tutorials, etc.)
- **Resources Section**: Quick links to external tools (ChatGPT, GitHub, Grok, VS Code, W3Schools)
- **Footer**: Class mantras and last updated date

### Updating the Index
When creating new day materials:
1. Change the day card from `upcoming` to `completed` class
2. Update the topics list if needed
3. Add links to the new materials in the materials section
4. Primary links use `material-link` class
5. Secondary links use `material-link secondary` class

### File Organization
```
jeremy-pants/
├── index.html (main landing page)
├── CLAUDE.md (this file)
├── day 1/
│   └── binary-cats-tutorial.html
├── day 2/
│   └── day2_slides.html
└── day X/
    └── dayX_slides.html
```

## Slide Deck Creation Guidelines

### Technical Specifications
- Create single-file HTML presentations (no external dependencies)
- Store slides in "day X" folders (e.g., "day 2", "day 3")
- Filename format: `dayX_slides.html`
- Include keyboard navigation (arrow keys and spacebar)
- Make slides mobile-responsive
- Test all interactive elements before delivery

### Design Standards
```css
Primary Colors:
- Purple gradient: #667eea to #764ba2
- Success: #4caf50
- Error: #f44336
- Background: white slides on gradient background
- Text: #333 for main content
```

### Essential CSS Fixes
Always include these to ensure readability:
```css
.quiz-option {
    color: #333;  /* Ensures quiz text is visible */
}

button {
    color: white;  /* Button text should be white */
}
```

### Slide Structure Template
Each slide deck should include:
1. **Title Slide** - Day number, topic, fun emoji
2. **Review Slide** - Quick quiz from previous day
3. **Vocabulary Slides** - 3-5 terms with relatable definitions
4. **Content Slides** - Main lesson with interactions
5. **Activity Slides** - Hands-on exercises
6. **Summary Slide** - Recap and preview next class

### Interactive Elements to Include
- Binary calculators with toggle bits
- Quiz questions with immediate feedback
- Fill-in-the-blank exercises
- Visual demonstrations (file trees, paths, etc.)
- Live coding areas where applicable
- "Fun Facts" boxes with interesting tidbits

### Teaching Preferences
- Use analogies students understand (TikTok, Fortnite, etc.)
- Include "Brother Cope stories" when relevant
- Add humor but keep it appropriate
- Make complex concepts simple
- Always include hands-on activities
- Reference previous lessons and inside jokes (Jeremy pants, etc.)

### Vocabulary Format
```html
<div class="vocab-term">Term Name</div>
<div class="vocab-def">Simple definition with real-world analogy</div>
```

### Activity Box Format
```html
<div class="activity-box">
    <p><strong>Activity Name!</strong> Description of what students will do</p>
</div>
```

### Quiz Implementation
```javascript
function checkAnswer(button, isCorrect) {
    // Disable all options after selection
    // Add visual feedback (✓ or ✗)
    // Change colors (green for correct, red for incorrect)
}
```

## Daily Topics Overview

### Day 1 (Completed)
- GitHub introduction
- Binary basics
- AI tools (Grok for video generation)
- Created "jeremy-pants" repository
- **Materials**: binary-cats-tutorial.html

### Day 2 (Completed)
- Binary addition/subtraction
- Operating systems
- Files and folders
- File paths
- RAM vs Storage
- **Materials**: day2_slides.html (interactive presentation)

### Future Topics to Cover (from syllabus)
- Web Development (HTML/CSS basics)
- AI and Machine Learning
- Programming with Python
- Physical computing
- Cybersecurity basics
- Career exploration in tech

## Code Examples for Slides

### Binary Calculator HTML Structure
```html
<div class="bit-container">
    <div class="bit">
        <div class="bit-value">128</div>
        <button class="bit-button" onclick="toggleBit(this)">0</button>
    </div>
    <!-- Repeat for other bits -->
</div>
```

### File Tree Visualization
```html
<div class="file-tree">
    <pre>
<span class="folder">📁 FolderName/</span>
    ├── <span class="file">📄 file.txt</span>
    └── <span class="folder">📁 SubFolder/</span>
    </pre>
</div>
```

## Testing Checklist
Before delivering slides, verify:
- [ ] All quiz buttons show text clearly (color: #333)
- [ ] Interactive elements work (binary calculators, etc.)
- [ ] Navigation works (arrows, spacebar)
- [ ] Slide numbers update correctly
- [ ] All code examples are tested
- [ ] Mobile view is responsive
- [ ] No broken animations

## Common Issues and Fixes

### Text Not Visible in Buttons
Add `color: #333;` to button/option CSS

### Slides Not Changing
Check that JavaScript is properly incrementing `currentSlide`

### Interactive Elements Not Working
Ensure onclick handlers are properly defined and functions exist

## Brother Cope's Preferences
- Loves puzzles and riddles
- Former Adobe employee, now entrepreneur
- Has 5 kids (Mona, Holden, Abby, Charlie, Lucy)
- Emphasizes practical skills over theory
- Requires AI use in class
- Focuses on skills that will get jobs
- Likes to show personal photos/stories
- Big on spreadsheets ("every job needs them")
- Racquetball and pickleball enthusiast

## Quiz Question Style
- Mix of technical and fun questions
- Include logic puzzles occasionally
- Reference class inside jokes
- Keep difficulty appropriate for mixed skill levels
- Always provide immediate feedback

## Remember
- This is an introductory class - keep it accessible
- Students have varying backgrounds
- Make it fun and engaging
- Less lecturing, more doing
- Real-world applications are key
- AI is a tool to enhance, not replace, learning