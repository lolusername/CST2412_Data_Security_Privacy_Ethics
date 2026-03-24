# Week 6 Individual Lab: HTTPS, Trust, and What Still Leaks

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual  
**What you submit:** 1 document with screenshots + short answers  
**Rule:** You are not hacking anything. You are only inspecting what your browser already shows you.

## What you’ll learn
By the end you should be able to explain:
- what HTTPS/TLS protects (and what it doesn’t)
- what a certificate is trying to prove
- why “we use Let’s Encrypt” is not the same as “we respect privacy”
- how third-party services can create privacy boundaries even on HTTPS pages

---

## Pick 1 target website
Pick **ONE** website you can legally visit.
- It must start with `https://`
- Use a school site, your portfolio site, a store, or any site you use

Write the URL at the top of your submission.

---

## Part 1 — What HTTPS protects (simple + concrete)
Answer in **1–2 sentences each**.

1) When you visit an HTTPS site, what does encryption protect **while data moves over the internet**?  
2) What does HTTPS *not* protect if the website owner decides to collect a lot of data?

**Checkpoint (required):**  
Write **one example** of a privacy harm that could happen even if the site uses HTTPS correctly.

---

## Part 2 — Certificate check (Let’s Encrypt connection)
You will find basic certificate facts using your browser.

### Step A: Open the certificate viewer
Click the lock icon → “Connection is secure” → “Certificate” (wording varies).

### Step B: Take screenshots (required)
Capture screenshots showing:
- **Issuer** (who issued it)
- **Expiration date** (valid until)
- **Domain name(s)** it covers (SANs or “Subject Alternative Names”)

### Step C: Short answers
1) Is the issuer **Let’s Encrypt** or something else?  
2) If the certificate expires, what do users typically see? (plain English)  
3) Why would a site prefer Let’s Encrypt? (pick one: cost, automation, ease, other)

---

## Part 3 — “Secure page” vs “who else is involved?”
Even when the page is HTTPS, it can load resources from other companies.

### Step A: Open DevTools
- Chrome: View → Developer → Developer Tools  
- Click the **Network** tab  
- Reload the page

### Step B: Find third-party domains
Look at the domain/host for requests (or click a request and find “Request URL”).

List up to **3 domains** that are **NOT** the main site domain.

Example format:
- `your-site.com` = first party  
- `google-analytics.com` = third party  
- `cdn.somevendor.net` = third party

If you only see 1–2 third parties, list what you see.

### Step C: Explain the boundary (short but clear)
Answer:
1) What is a “third party” in this context?  
2) Why is a third-party request a privacy boundary, even on HTTPS?

**Checkpoint:**  
Pick **ONE** third-party domain you found and write one sentence on what data it might learn by default (examples: IP address, device/browser type, time, which page loaded it).

---

## Part 4 — Cookies (intro version)
Cookies are one of the most common ways websites remember things.

### Step A: Check if the site sets cookies
DevTools → Application (or Storage) → Cookies → select the site.

### Step B: Answer
1) Does the site set cookies? (yes/no)  
2) If yes, list any **two cookie names** (names only).  
3) If no cookies: write “No cookies observed” and one sentence explaining what that might mean.

**Checkpoint:**  
In one sentence: how can cookies affect privacy?

---

## Part 5 — Short scenario: “HTTPS is not privacy”
Read this scenario and answer the questions.

### Scenario
A college says:

> “Our student portal is secure because it uses HTTPS and Let’s Encrypt.”

But the portal also:
- sends analytics data to a third-party company
- keeps server logs for an unknown amount of time
- uses that data later to rank students for “student success interventions”

### Questions (short answers)
1) Name **two things** HTTPS protects in this situation.  
2) Name **two privacy risks** that still exist.  
3) Write **one rule** you would require before using portal data to rank students (examples: purpose limitation, retention limit, student notice, opt-out, review process).

---

## Part 6 — Mini memo (graded writing)
Write **180–250 words**:

**Does “we use HTTPS/Let’s Encrypt” make the college portal automatically privacy-respecting? Why or why not?**

Requirements:
- Include one thing HTTPS does well
- Include one thing HTTPS does not address
- Mention **third parties** OR **retention**
- End with **one concrete recommendation** (one sentence)

---

## What to submit
Your document must include these headings:
- Part 1: HTTPS protects / doesn’t protect  
- Part 2: Certificate evidence + answers  
- Part 3: Third-party domains + boundary explanation  
- Part 4: Cookies  
- Part 5: Scenario answers  
- Part 6: Mini memo  

Plus screenshots for Part 2.

---

## Grading rubric (simple)
Full credit if you:
- include required screenshots
- correctly explain what HTTPS does and doesn’t do
- identify real third-party domains from the Network tab (if any exist)
- write a clear memo with a concrete recommendation