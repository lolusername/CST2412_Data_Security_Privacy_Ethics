# Quick Lab (Defensive): Trust Boundaries and Injection Risk

## Duration
20-25 minutes (in class)

## Purpose
Apply Chapter 3, 4, and early 5 concepts to realistic request samples. Your goal is defensive analysis, not exploitation.

## Rules
- Work only with the sanitized samples below.
- Do not test against live systems.
- No exploit development steps.
- Use class vocabulary (CIA, complete mediation, least privilege, trust boundary).

## Individual Workflow
1. Read each sample carefully.
2. Classify flaw type and CIA impact.
3. Propose one mitigation and assign owner.
4. Mark urgency and justify in one sentence.

## Sample A: Parameter Tampering
```http
GET /order?custID=101&part=555A&qy=20&price=1&ship=boat&shipcost=5&total=25 HTTP/1.1
Host: example-shop.edu
```

## Sample B: SQL Injection Pattern
```http
POST /login HTTP/1.1
Host: example-portal.edu
Content-Type: application/x-www-form-urlencoded

username=student1&password=' OR '1'='1
```

## Sample C: Path Traversal
```http
GET /download?file=../../../../winnt/system32/autoexec.nt HTTP/1.1
Host: files.example.edu
```

## Required Output (For Each Sample)
1. Likely flaw type
2. Why this is exploitable
3. Primary CIA impact
4. One concrete mitigation
5. Control owner (developer, system admin, policy lead)
6. Urgency (now / sprint / backlog) with one-sentence reason


## Reflection Prompt (1 minute)
Which mitigation would most reduce risk fastest across all three samples, and why?
