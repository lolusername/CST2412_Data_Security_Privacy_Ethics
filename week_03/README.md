# Week 3: Data Security, Privacy, and Ethics

## Week focus
This week connects three ideas into one practical workflow:
- Security fundamentals and trust boundaries
- Injection risk and defensive coding patterns
- Ethical and operational responsibilities when handling user data

## Colab lab (updated)
Use this link for the live notebook lab (same lab content, now in Colab):
- https://colab.research.google.com/drive/1vU2M_mLeBN3H8gbfL9Y0uD_bot4KW9n6?usp=sharing

Local notebook copy:
- `week_03/sql_parameterization_security_demos.ipynb`

## Parts of class (recommended flow)
### Part 1: Context and concepts (15-20 min)
Use slides to introduce:
- Why input validation and parameterization matter
- Trust boundaries in web/database workflows
- CIA impact of injection-style flaws

Primary file:
- `week_03/data_security_privacy_ethics.pptx`

### Part 2: Guided demo (20-25 min)
Run the SQL parameterization notebook live.
Show insecure and secure versions side by side, then discuss why behavior changes.

Primary file/link:
- Colab link above
- `week_03/sql_parameterization_security_demos.ipynb`

### Part 3: Student lab activity (20-25 min)
Students classify flaws, CIA impact, mitigation, owner, and urgency for each sample.

Primary file:
- `week_03/quick_lab_handout.md`

### Part 4: Debrief and synthesis (10-15 min)
Whole-class share-out:
- What control prevents the most risk fastest?
- Where parameterization applies and where allowlists are needed
- How least privilege reduces blast radius

### Part 5: Wrap-up and assessment (5-10 min)
Use quick reflections or exit tickets tied to:
- Complete mediation
- Least privilege
- Secure defaults for input handling

## Week 3 teaching files
- `week_03/data_security_privacy_ethics.pptx`
  Main lecture deck.
- `week_03/data_security_privacy_ethics.pdf`
  PDF export of lecture deck.
- `week_03/notes.md`
  Instructor prep notes and deeper references.
- `week_03/quick_lab_handout.md`
  Student-facing lab sheet.
- `week_03/sql_parameterization_security_demos.ipynb`
  Local notebook version of the SQL/input-safety lab.

## Instructor-only notes
Files prefixed with `answer_` are intended as private instructor keys and are ignored by git via `.gitignore`.
